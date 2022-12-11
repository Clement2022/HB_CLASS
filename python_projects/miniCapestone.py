import speech_recognition as don
import pyttsx3
import pywhatkit
import wikipedia
import datetime 

listener = don.Recognizer()
speaking = pyttsx3.init()

def talk_back(text):
    speaking.say(text)
    speaking.runAndWait()

def take_command():
    try:
        with don.Microphone() as source:
            print('listening...........')
            voice = listener.listen(source)
            say_a_command = listener.recognize_google(voice)
            say_a_command = say_a_command.lower()
            if 'clement' in say_a_command:
                say_a_command = say_a_command.replace('clement', '')
                print(say_a_command)

    except:
        pass
    return take_command()

def received_run():
    say_a_command = take_command()
    print(say_a_command)
    if 'play' in say_a_command:
        song = say_a_command.replace('play', '')
        talk_back('playing ' + song)
        pywhatkit.playonyt(song)

received_run()