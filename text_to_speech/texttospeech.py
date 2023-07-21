from gtts import gTTS
import os 
import playsound as p
speech = input('Enter the sentence you want to say.')
if speech == 'How are you?':
    text1 = 'I am fine, what about you?'
text1 = speech
language = 'en'#JAPANESE: ja, HINDI: hi
speak = gTTS(text =  text1,lang = language, slow = False)
speak.save(r'C:\Users\ashan\Documents\GitHub\PythonProjects\text_to_speech\Welcome.mp3')
p.playsound(r'C:\Users\ashan\Documents\GitHub\PythonProjects\text_to_speech\Welcome.mp3')
