import pyttsx3

audio = pyttsx3.init()
audio.setProperty('rate', 200)
audio.setProperty('volume', 0.9)

myAudio = "sample"

audio.save_to_file(myAudio, 'textToSpeechAudio.mp3')
audio.runAndWait()