import pyttsx3
import sys 
import main

sys.path.append("..")

audio = pyttsx3.init()
audio.setProperty('rate', 200)
audio.setProperty('volume', 0.9)

audio.save_to_file(main.comments, 'textToSpeechAudio.mp3')
audio.runAndWait()