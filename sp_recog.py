import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

engine.say('ALEXA INITIALISING......')
engine.say('What can I do for you.......?')
engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('say something............')
            voice = listener.listen(source)
            command = listener.recognize(voice)
            command = command.lower()
            if 'alexa' in command:
             command = command.replace('alexa', '')
             print(command)
    except:
        pass
        return command
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing.....' + song)
        print('playing.....' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%p')
        talk('current time is....' + time)
        print('current time is....' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
        print(info)

    elif 'date' in command:
        print(datetime.date.today())
        talk(datetime.date.today())

    elif 'jokes' in command:
        talk(pyjokes.get_joke('en'))

    elif 'single' in command:
        talk('sorry, i am in relationship with your wifi')

    else:
        talk('sorry, i did not understand, can you speak again')

while True:
    run_alexa()
