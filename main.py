from gtts import gTTS 
import os 
import pyttsx3

mytext = input("Enter the Sentence or word: ")
Gender = input("select a gender 'M' or 'F': ")
audio = pyttsx3.init()
language = 'en'

if Gender == 'F':
    output = gTTS(text=mytext, lang=language, slow=False)
    output.save("output.mp3")
    os.system("start output.mp3") 
elif Gender == 'M':
    audio.setProperty('rate',150)
    audio.setProperty('volume',1)
    audio.say(mytext)
    audio.runAndWait()
else:
    print("You have entered Nothing")
    

