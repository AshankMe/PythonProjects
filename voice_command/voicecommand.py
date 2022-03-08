import speech_recognition as sr
from gtts import gTTS
import os 
import playsound as p
from webbrowser import open_new_tab as ont # put url here

recog = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak!")
    audio = recog.listen(source)
    print('Analyzing...')
try:
    text = recog.recognize_google(audio)
    print(text)
except: 
    print('Please speak again!')

def speak1(text1):
    language = 'en'
    speak = gTTS(text =  text1,lang = language, slow = False)
    speak.save('Welcome.mp3')
    p.playsound('Welcome.mp3')
    
if text == 'how are you':
    text1 = 'I am fine, what about you?'
    #text1 = speech
    speak1(text1)


if text == 'who are you':
    text1 = 'I am JARVIS. I will help you manage everything you need along with help you out and talk to you to make it so you are living easy.'
    speak1(text1)
if text == 'Are you alive':
    text1 = 'No. I am a robot'
    speak1(text1)
if text == 'turn off':
    text1 = 'Ok. I am not yet capable of turning myself off, but you can do CTRL + S to save your code and then Alt + F4 to exit.'
    speak1(text1) 
if text == 'who is your owner':
    text1 = 'I am coded and created by AshankMe.'
    speak1(text1)
if text == 'how can i pass time in my class':
    text1 = 'try to pay attention because if you are engaged in the class it will go by faster'
    speak1(text1)
