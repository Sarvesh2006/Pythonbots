import speech_recognition as sr
import pyttsx3
import os
import calendar
import time
import datetime
from datetime import date


current_date = datetime.datetime.now()
current_time = time.time()

speech = sr.Recognizer()

try:
   engine = pyttsx3.init()
except ImportError:
   print('Requested driver is not found')
except RuntimeError:
       print('Driver fails to initialize')

voices = engine.getProperty('voices')

for voice in voices:
    print(voice.id)
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSSpeech_TTS_en-US_ZiraPro.msi')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate)



def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()

def read_voice_cmd():
    voice_text = ''
    print('Listening...')
    with sr.Microphone() as source:
        audio = speech.listen(source)
    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
         pass
    except sr.RequestError as e:
        print('Network error.')
    return voice_text


if __name__ == "__main__":
    speak_text_cmd('Hello Mr Sarvesh. This is JARVIS, as your Artificial Intelligence.')

    while True:

        voice_note = read_voice_cmd()
        print('cmd: {}'.format(voice_note))

        if 'hello' in voice_note:
            speak_text_cmd('Hello sir. How can i help you?')
            print('JARVIS: Hello sir. How can I help you?')
            continue
        elif 'display date and time' in voice_note:
            print(current_date)
            continue
        elif 'thank you' in voice_note:
            speak_text_cmd('You are welcome sir')
            print('You are welcome sir')
            continue          
        elif 'bye' in voice_note:
            speak_text_cmd('Bye, Mr. Sarvesh . Happy to help you . Have a good day')
            print('Bye, Mr.Sarvesh. Happy to help you. Have a good day')
            exit()
