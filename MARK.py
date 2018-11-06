import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as tts

print("Hello World!")
a = input('Enter your name:')
engine = tts.init()
engine.say('Hello',a)
engine.say("I am your personal assistant 'MARK'. Its nice to meet you!")
engine.runAndWait()


for i in range(1,1000000):
    Username = input("Enter username:")
        
    if Username == "Ansh":
        
        for i in range(1000000):
            Password = input("Enter Password:")
    
            if Password == "":
                print("Welcome Ansh!")
                break 
        break            
        
    elif Username == "administrator":
        
        for i in range(1000000):
            Password = input("Enter Password:")
        
            if Password == "":
                print("Welcome administrator!")
                break
        break

    else:
        print("Enter the correct Username")


for i in range (10000000000):
        
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

        elif task == "say a hindi tongue twister":
            engine = tts.init()
            engine.say("Kaccha paapad, pakka paapad, kaccha paapad, pakka paapad, kaccha paapad, pakka paapad.")
            engine.runAndWait()

        elif task == "am i fat":
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
        
        elif task == "set reminder":
            rmd = input("what do you want me to remind you of?")
            print ("I will remind you of that!")
            prompt = input ("Do you want me to remember something else?")
        
            if prompt == "yes":
                rmd1 = input("What else do you want me to remind you of?")
                print("Sure!")
        
            else:
                print("Okay")
        
        elif task == "Did i ask you to remember something?":
            print ("These are the things you asked me to remind you of :")
            print (rmd)
            print (rmd1)
        
        elif task == "shutdown":
            engine = tts.init()
            engine.say("Okay I'll stop")
            engine.runAndWait()
            break
        
        else:
            engine = tts.init()
            engine.say("Opening Google Chrome")
            engine.runAndWait()
            
            wb.open("https://www.google.com/?#q="+task, new = 2, autoraise = True)

