import speech_recognition as sr
import webbrowser as wb

print("Hello World!")
a = input('Enter your name:')
print ('Hello',a)
print ("I am your personal assistant 'MARK'. Its nice to meet you!")


for i in range (1):
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
        print ('Thunderstorms will move through your area. The high will be 28 and low will be 23.')
    elif task == "what is zero plus zero":
        print ("Zero plus Zero is nothing. Zero")
    elif task == "how are you":
        print ("I am in good health! Thank you for asking!")
    elif task == "how old are you":
        print("I was created on 15th August 2018 by Ansh Choudhary. Feels like only yesterday :)")
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
    elif task == "shut down":
        print("Okay I'll stop")
        break
    else:
        wb.open("https://www.google.com/?#q="+task, new = 2, autoraise = True)

