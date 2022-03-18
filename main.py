import speech_recognition
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = speech_recognition.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with speech_recognition.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('the current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'morning' in command:
        talk('good morning sir')

    elif 'single' in command:
        talk('I am in a commited relationship with the wifi router')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('Please say the command again please.')
    

while True:
    try: 
        run_jarvis()

    except UnboundLocalError:
        print("No command detected! Jarvis has stopped working")
        break