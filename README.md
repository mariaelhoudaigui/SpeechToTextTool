# Descritption 

This project is a simple tool to record audio using a microphone and convert it into text using Google's Speech Recognition API. 
The tool is currently set up for the French language but can be adapted for other languages.


## Features
- **Audio Recording**: Records audio from the microphone and saves it as a `.wav` file.
- **Speech-to-Text Conversion**: Converts the recorded audio into text using Google's Speech Recognition API.
- **Text Saving**: Saves the converted text to a `.txt` file.

## Requirements
Ensure you have the following libraries installed:
- `sounddevice`
- `scipy`
- `speechrecognition`

Install them using:
```bash
pip install sounddevice scipy speechrecognition  
```

Change Language :
```
text = recognizer.recognize_google(audio, language="fr-FR")
```
For English, use "en-US". <br>
For Spanish, use "es-ES".<br>
For Arabic, use "ar-SA".
