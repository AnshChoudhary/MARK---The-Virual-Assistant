import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as tts
from os import popen

print("Hello!")
engine = tts.init()
engine.say('Hello. I am your personal assistant. How can I help you?')
engine.runAndWait()

ansh = "1010"
print("Voice actication required")
while ansh == "1010":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
        except:
            text = "not point break"

    while text == "point break":
            engine = tts.init()
            engine.say('Yes sir')
            engine.runAndWait()        
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Speak anything you want me to do:")
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print("You said : {}".format(text))
                except:
                    print("Sorry could not recognize what you said")
                task = text
            
            if task == "weather report":
                engine = tts.init()
                engine.say('Thunderstorms will move through your area. The high will be 28 and low will be 23.')
                engine.runAndWait()
            
            elif task == "what is 0 + 0":
                engine = tts.init()
                engine.say("Zero plus Zero is nothing. Zero")
                engine.runAndWait()
            
            elif task == "tell me a joke":
                engine = tts.init()
                engine.say("What did the green peas say? Nothing. They just mutter'ed.")
                engine.runAndWait()

            elif task == "give me menu ideas":
                engine = tts.init()
                engine.say("Toss some bhel and sprouts together for breakfast, keep it simple with a sandwich for lunch and have vegetable fajitas with soy rice for dinner.")
                engine.runAndWait()

            elif task == "give me a gross fact":
                engine = tts.init()
                engine.say("Breaking news! Farts can travel at speeds of up to 10 feet per second.")
                engine.runAndWait()
            
            elif task == "start stopwatch":
                engine = tts.init()
                engine.say("press Enter to start")
                engine.runAndWait()
                stopwatch()
            
            elif task == "say a hindi tongue twister":
                engine = tts.init()
                engine.say("Kaccha paapad, pakka paapad, kaccha paapad, pakka paapad, kaccha paapad, pakka paapad.")
                engine.runAndWait()

            elif task == "am I fat":
                engine = tts.init()
                engine.say("I would prefer not to say")
                engine.runAndWait()

            elif task == "what are you wearing":
                engine = tts.init()
                engine.say("Aluminosilcate glass and Alcantara. Nice,huh?")
                engine.runAndWait()

            elif task == "what is the best laptop":
                engine = tts.init()
                engine.say("The one you're using.")
                engine.runAndWait()

            elif task == "will you marry me":
                engine = tts.init()
                engine.say("Lets just be friends. OK?")
                engine.runAndWait()

            elif task == "open spotify":
                engine = tts.init()
                engine.say("Opening Spotify")
                engine.runAndWait()
                popen('spotify')

            elif task == "tell me a story":
                engine = tts.init()
                engine.say("Once upon a time.... No, it's too silly.")
                engine.runAndWait()

            elif task == "how are you":
                engine = tts.init()
                engine.say("I am in good health! Thank you for asking!")
                engine.runAndWait()
            
            elif task == "how old are you":
                engine = tts.init()
                engine.say("I was created on 15th August 2018 by Ansh Choudhary. Feels like only yesterday.")
                engine.runAndWait()
            
            elif task == "what is the meaning of life":
                engine = tts.init()
                engine.say("All evidence to date suggests it's chocolate")
                engine.runAndWait()
            
            elif task == "take notes":
                engine = tts.init()
                engine.say("I'm listening")
                engine.runAndWait()
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    audio = r.listen(source)
                    try:
                        note1 = r.recognize_google(audio)
                        print("You said : {}".format(note1))
                    except:
                        print("Sorry could not recognize what you said")
                        note1 = "No notes"
                engine = tts.init()
                engine.say("Note taken!")
                engine.runAndWait()
            
            elif task == "what were my notes":
                engine = tts.init()
                engine.say("These are the things you asked me to note down for you :")
                engine.say(note1)
                engine.runAndWait()
                
            
            elif task == "shutdown":
                engine = tts.init()
                engine.say("Okay I'll stop")
                engine.runAndWait()
                ansh = "1011"
                break
            
            elif task == "stop":
                engine = tts.init()
                engine.say("Okay I'll stop")
                engine.runAndWait()
                ansh = "1011"
                break

            else:
                engine = tts.init()
                engine.say("Opening Google Chrome")
                engine.runAndWait()
                
                wb.open("https://www.google.com/?#q="+task, new = 2, autoraise = True)

