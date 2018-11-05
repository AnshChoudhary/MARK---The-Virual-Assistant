import speech_recognition as sr

print("Hello World!")
a = input('Enter your name:')
print ('Hello',a)
print ("I am your personal assistant 'Cortana'. Its nice to meet you!")

for q in range(1,1000000):
    Username = input("Enter username:")
    if Username == "Ansh" or "administrator":
        if Username == "Ansh":
            for i in range(1000000):
                Password = input("Enter Password:")
                if Password == "mark1902":
                    print("Welcome Ansh!")
                    break 
        elif Username == "administrator":
            for i in range(1000000):
                Password = input("Enter Password:")
                if Password == "1902":
                    print("Welcome administrator!")
                    break
        break
    else:
        print("Enter the correct Username")


for i in range (1,1000000):
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
        print ("I cannot do that. There are a lot of other things that I can do for you :)")


