[![Twitter: @NorowaretaGemu](https://img.shields.io/badge/X-@NorowaretaGemu-blue.svg?style=flat)](https://x.com/NorowaretaGemu)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  
  <br>
<div align="center">
  <a href="https://ko-fi.com/cursedentertainment">
    <img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="ko-fi" style="width: 20%;"/>
  </a>
</div>
  <br>

<div align="center">
  <img alt="Python" src="https://img.shields.io/badge/python%20-%23323330.svg?&style=for-the-badge&logo=python&logoColor=white"/>
</div>
<div align="center">
    <img alt="Git" src="https://img.shields.io/badge/git%20-%23323330.svg?&style=for-the-badge&logo=git&logoColor=white"/>
  <img alt="PowerShell" src="https://img.shields.io/badge/PowerShell-%23323330.svg?&style=for-the-badge&logo=powershell&logoColor=white"/>
  <img alt="Shell" src="https://img.shields.io/badge/Shell-%23323330.svg?&style=for-the-badge&logo=gnu-bash&logoColor=white"/>
  <img alt="Batch" src="https://img.shields.io/badge/Batch-%23323330.svg?&style=for-the-badge&logo=windows&logoColor=white"/>
  </div>
  <br>

# kida-chatbot_openrouter-elevenlabs

## How to Run:

### Get OpenRouter and ElevenLabs API Keys

1. **Get your API keys** from:
   - [OpenRouter](https://openrouter.ai/)
   - [ElevenLabs](https://elevenlabs.io/)

2. **Save the keys in text files:**
   - Paste your **OpenRouter** key into the file named: `openrouter-api-key.txt`
   - Paste your **ElevenLabs** key into the file named: `elevenlabs-api-key.txt`


### FFMpeg Setup (Windows)

1. **Download FFMpeg**  
   Visit the following link and download the latest static build:  
   https://www.gyan.dev/ffmpeg/builds/

2. **Extract the Archive**  
   Unzip the downloaded archive to `C:\`.

3. **Rename and Organize**  
   Rename the extracted folder to `ffmpeg`, and ensure the following folder structure:

```bash
C:\ffmpeg\bin
├── ffmpeg.exe
├── ffplay.exe
└── ffprobe.exe
```

4. **Set Environment Variable (Optional for Global Access)**  
   To make `ffmpeg` accessible system-wide:

   - Open **System Properties** > **Environment Variables**
   - Under **User variables** (for your PC username), find and select **Path**
   - Click **Edit** > **New** and paste:

     ```
     C:\ffmpeg\bin
     ```

   - Click **OK** to apply the changes
  
5. Test it
     Close and reopen your terminal (CMD), then type:

    ```
    ffmpeg -version
    ```
    If it prints the version info, you're good.

6. The code below will automatically append `C:\ffmpeg\bin` to the runtime path, so no need to set environment variables manually. 

```bash
# === CONFIG ===

# Path fix for ffmpeg
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin"
```

### FFMpeg Setup (Linux)

Debian/Ubuntu/Kubuntu/Linux Mint:
```bash
sudo apt update
sudo apt install ffmpeg
```
Fedora:
```bash
sudo dnf install ffmpeg
```
Arch/Manjaro:
```bash
sudo pacman -S ffmpeg
```

### Install Requirements

Using Python directly:

```bash
pip install -r requirements.txt
```
Or run: 
- `install_requirements.bat` - Windows
- `install_requirements.sh` - Debian/Ubuntu/Kubuntu/Linux Mint
  
<br>

### Run main.py

Using Python directly:

```bash
python kida-chatbot.py
```

Using provided scripts:

Windows:
- `.\run.bat`
or
- `.\run.ps1`

Unix-like systems (Linux/macOS):
- `.\run.sh`

  <br>

## Requirements:

FFMpeg

```bash
whisper
SpeechRecognition
pygame
requests
elevenlabs==0.2.26
torch
torchaudio
```

<br>
<div align="center">
© Cursed Entertainment 2025
</div>
<br>
<div align="center">
<a href="https://cursed-entertainment.itch.io/" target="_blank">
    <img src="https://github.com/CursedPrograms/cursedentertainment/raw/main/images/logos/logo-wide-grey.png"
        alt="CursedEntertainment Logo" style="width:250px;">
</a>
</div>
