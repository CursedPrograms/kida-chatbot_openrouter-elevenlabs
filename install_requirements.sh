#!/bin/bash

# Equivalent of @echo off (just don't print each command)
set +x

# Install dependencies
pip install -r requirements.txt

# Pause until user presses Enter
read -p "Press Enter to continue..."