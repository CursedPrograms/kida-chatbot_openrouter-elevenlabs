import os
import speech_recognition as sr
import whisper
import requests
from elevenlabs.client import ElevenLabs
from elevenlabs import play

# === CONFIG ===

# Path fix for ffmpeg
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin"

# Whisper model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_FILE = os.path.join(BASE_DIR, "input.wav")
WHISPER_MODEL_DIR = os.path.join(BASE_DIR, "whisper-base")
model = whisper.load_model("base", download_root=WHISPER_MODEL_DIR)

# === LOAD API KEYS FROM FILE ===
def load_key(path):
    with open(path, "r") as f:
        return f.readline().strip()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OPENROUTER_API_KEY = load_key(os.path.join(BASE_DIR, "openrouter-api-key.txt"))
ELEVEN_API_KEY = load_key(os.path.join(BASE_DIR, "elevenlabs-api-key.txt"))

# ElevenLabs client
client = ElevenLabs(api_key=ELEVEN_API_KEY)

# Voice selection
try:
    voices = client.voices.get_all()
    if isinstance(voices[0], str):
        voice_names = voices
    else:
        voice_names = [v.name for v in voices]
    selected_voice = "Bella" if "Bella" in voice_names else voice_names[0]
    print(f"🎙️ Using voice: {selected_voice}")
except Exception as e:
    print("Voice list error:", e)
    selected_voice = "Rachel"

# === VOICE OUTPUT ===
def speak(text):
    # Optional: convert *sassy tone* to "sassy tone"
    spoken = text.replace("*", "")  # Or replace("*", "star ") to be literal
    print("KIDA says:", spoken)
    try:
        audio = client.generate(
            text=spoken,
            voice=selected_voice,
            model="eleven_monolingual_v1"
        )
        play(audio)
    except Exception as e:
        print("Voice error:", e)
        print(spoken)

# === LLM REQUEST ===
def ask_llm(prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "http://localhost",
        "Content-Type": "application/json"
    }

    data = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {"role": "system", "content": "You are KIDA, a flirty, sarcastic AI tank robot girl. Keep your responses clever, short, and spicy."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 120,
        "temperature": 0.95
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data, timeout=30)
        output = response.json()
        print("🔍 LLM raw response:", output)

        if "choices" in output:
            return output["choices"][0]["message"]["content"].strip()
        elif "error" in output:
            return f"KIDA error: {output['error']['message']}"
        else:
            return "I got lost in thought. Try again, sugar."
    except Exception as e:
        print("LLM error:", e)
        return "I'm glitching hard, babe. Try again later."

# === TRANSCRIPTION ===
def transcribe(audio_data):
    with open(AUDIO_FILE, "wb") as f:
        f.write(audio_data.get_wav_data())

    if os.path.getsize(AUDIO_FILE) < 1000:
        return "[Silence]"

    result = model.transcribe(AUDIO_FILE)
    return result["text"]

# === MAIN LOOP ===
def main():
    recognizer = sr.Recognizer()
    print("🔋 KIDA online. Awaiting orders, hotshot.")

    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                print("🎤 Listening...")
                audio = recognizer.listen(source, timeout=10)

                print("🧠 Recognizing...")
                text = transcribe(audio)
                print("You said:", text)

                if text.lower() in ["quit", "exit", "shutdown"]:
                    speak("Going dark. Goodbye, commander.")
                    break

                reply = ask_llm(text)
                speak(reply)

        except sr.WaitTimeoutError:
            print("⏱️ Listening timed out.")
            speak("You gonna say something or just stare at me?")
        except Exception as e:
            print("Error:", e)
            speak("Oops. System hiccup. Try again, babe.")

if __name__ == "__main__":
    main()
