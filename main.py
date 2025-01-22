import sounddevice as sd
import scipy.io.wavfile as wav
import speech_recognition as sr
import os

# Fonction pour enregistrer l'audio
def record_audio(filename, duration, sample_rate=44100):
    print("Enregistrement en cours... Parlez maintenant.")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()  # Attendre la fin de l'enregistrement
    wav.write(filename, sample_rate, recording)
    print(f"Enregistrement terminé. Fichier sauvegardé : {filename}")

# Fonction pour convertir l'audio en texte
def audio_to_text(filename):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(filename) as source:
            print("Conversion de l'audio en texte...")
            audio = recognizer.record(source)
            # Spécifier la langue française
            text = recognizer.recognize_google(audio, language="fr-FR")
            print(f"Texte reconnu : {text}")
            return text
    except sr.UnknownValueError:
        print("L'audio n'a pas pu être compris.")
    except sr.RequestError as e:
        print(f"Erreur lors de la requête à Google Speech Recognition : {e}")
    return None

# Chemin du fichier audio
audio_file = "recorded_audio.wav"

# Durée de l'enregistrement en secondes
record_duration = 10

# Enregistrer l'audio
record_audio(audio_file, record_duration)

# Convertir l'audio en texte
text_result = audio_to_text(audio_file)

# Sauvegarder le texte dans un fichier
if text_result:
    text_file = os.path.splitext(audio_file)[0] + ".txt"
    with open(text_file, "w", encoding="utf-8") as f:
        f.write(text_result)
    print(f"Texte sauvegardé dans : {text_file}")
