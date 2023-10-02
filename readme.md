# Translator

An assemblage of FOSS language and translation tools that work offline.

## Pre-requirements for Linux (run before python requirements)

### install espeak

```bash
sudo apt install espeak
```

### install tesseract

```bash
sudo apt install tesseract-ocr
```

### search for tesseract languages and install them

```bash
apt-cache search tesseract-ocr | grep languagename
sudo apt install tesseract-ocr-langcode
```

### install ffmpeg

```bash
sudo apt install ffmpeg
```

## Create venv and install python requirements

```bash
python -m venv .env
pip -r install requirements.txt
```

this may take time

## Download models

- [Argos](./res/models/argos/readme.md)
- [Vosk](./res/models/vosk/readme.md)

## Edit Config

[config](./src/core/config.py)

## Run tests

```bash
cd src
./run-tests
```