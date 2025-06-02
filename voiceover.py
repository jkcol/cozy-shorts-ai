from gtts import gTTS
import os

def generate_voice(text, filename="voice.mp3"):
    tts = gTTS(text)
    tts.save(filename)
    print("Voiceover saved.")
