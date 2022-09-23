import pyttsx3

audio = pyttsx3.init()
audio.setProperty('rate', 200)
audio.setProperty('volume', 0.9)

postTitle = main.postTitle

audio.save_to_file(postTitle, 'textToSpeechAudio.mp3')
audio.runAndWait()