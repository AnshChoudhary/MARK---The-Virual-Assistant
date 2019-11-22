import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as tts
from playsound import playsound
from os import popen
import yagmail
from sys import exit
import keyboard
import stopwatch
import subprocess
import wikipedia

def zira():
            engine = tts.init()
            engine.say('Yes sir')
            engine.runAndWait()
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Speak anything you want me to do:")
                playsound('D:\double-beep.mp3')
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print("You said : {}".format(text))
                except:
                    print("Sorry could not recognize what you said")
                    text = "what can you do"
                task = text
            
            if task == "weather report":
                engine = tts.init()
                engine.say('Thunderstorms will move through your area. The high will be 28 and low will be 23.')
                engine.runAndWait()
            
            elif task == "what is 0 + 0":
                engine = tts.init()
                engine.say("Zero plus Zero is nothing. Zero")
                engine.runAndWait()
            
            elif task == "what can you do":
                engine = tts.init()
                engine.say("I can perform various functions like sending e-mails, downloading songs and cracking a joke!")
                engine.runAndWait()

            elif task == "knock knock":
                engine = tts.init()
                engine.say("Who's there?")
                engine.runAndWait()
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio)
                        print("You said: "+ text)
                    except:
                        text = "Baahubali"
                
                if text == "kya bol rahe ho baccho":
                    engine = tts.init()
                    engine.say("That is Raahull Sir")
                    engine.runAndWait()

                else:
                    engine = tts.init()
                    engine.say("Try again")
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
            
            elif task == "Hindi tongue twister":
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

            elif task == "send a mail":
                engine = tts.init()
                engine.say("Fill out the following details to send the mail.")
                engine.runAndWait()
                yagmail.register("anshc19@gmail.com", "mark1901")
                yag = yagmail.SMTP('anshc19@gmail.com')
                to = input("Recipient's email: ")
                subject = input("Subject: ")
                body = input("Content: ")
                yag.send(to = to, subject = subject, contents = body)
                engine = tts.init()
                engine.say("Mail sent.")
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
            
            elif task == "search on Google":
                engine = tts.init()
                engine.say("Please type ehat you want to search on Google: ")
                engine.runAndWait()
                searchTerm = input("Search on google: ")
                wb.open("https://www.google.com/?#q="+searchTerm)

            elif task == "Ek joke Bata":
                engine = tts.init()
                engine.say("Haathi paani mein se kaise nikla....... Geela hoke")
                engine.runAndWait()

            elif task == "f*** you":
                engine = tts.init()
                engine.say("Haters gonna hate")
                engine.runAndWait()

            elif task == "locate a place":
                address = input("Enter the address: ")
                engine = tts.init()
                engine.say("Locating {}".format(address))
                engine.runAndWait()
                wb.open('https://www.google.com/maps/place/' + address)         
                
            elif task == "what is the meaning of life":
                engine = tts.init()
                engine.say("All evidence to date suggests it's chocolate")
                engine.runAndWait()

            elif task == "what is your name":
                engine = tts.init()
                engine.say("My name is Zira. ")
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
                
            elif task == "locate a place":
                address = input("Enter the address: ")
                engine = tts.init()
                engine.say("Locating {}".format(address))
                engine.runAndWait()
                wb.open('https://www.google.com/maps/place/' + address)    

            elif task == "send a mail":
                engine = tts.init()
                engine.say("Fill out the following details to send the mail.")
                engine.runAndWait()
                yagmail.register("anshc19@gmail.com", "mark1901")
                yag = yagmail.SMTP('anshc19@gmail.com')
                to = input("Recipient's email: ")
                subject = input("Subject: ")
                body = input("Content: ")
                yag.send(to = to, subject = subject, contents = body)
                engine = tts.init()
                engine.say("Mail sent.")
                engine.runAndWait()

            elif task == "download song":
                engine = tts.init()
                engine.say("Type the name of the song, artist or album you want to download")
                engine.runAndWait()
                music = input("Enter song to be downloaded: ")
                cmd = "spotdl --song '{}'".format(music)    
                returned_value = subprocess.call(cmd, shell=True)
                print('returned value:', returned_value)    
            
            elif task == "shutdown":
                engine = tts.init()
                engine.say("Okay I'll stop")
                engine.runAndWait()
                ansh = "0"

            elif task == "mute":
                engine = tts.init()
                engine.say("All systems turning mute")
                engine.runAndWait()
                filepath = "C:/Users/anshc/OneDrive/Documents/ZIRA/mute.bat"
                subprocess.Popen(filepath, shell=True)

            elif task == "unmute":
                filepath = "C:/Users/anshc/OneDrive/Documents/ZIRA/unmute.bat"
                subprocess.Popen(filepath, shell=True)
            
            elif task == "stop":
                engine = tts.init()
                engine.say("Okay I'll stop")
                engine.runAndWait()
                ansh = "0"
                
            elif task[0:19] == "tell me more about ":
                result = wikipedia.summary("{}".format(task[19:]),sentences=3)
                engine = tts.init()
                engine.say(result)
                engine.runAndWait()

            else:
                result = wikipedia.summary("{}".format(task),sentences=1)
                wb.open("https://www.google.com/?#q="+task, new = 2, autoraise = True)
                engine = tts.init()
                engine.say(result)
                engine.say("Do you wanna know more about {}".format(task))
                engine.runAndWait()
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    playsound('D:\double-beep.mp3')
                    audios = r.listen(source)
                    prompt = r.recognize_google(audios)
                    try:
                        if prompt =="yes please" or prompt == "sure":
                            result = wikipedia.summary("{}".format(task),sentences=3)
                            engine = tts.init()
                            engine.say(result)
                            engine.runAndWait()
                        else:
                            engine = tts.init()
                            engine.say("Okay")
                            engine.runAndWait()
                    except:
                        engine = tts.init()
                        engine.say("Okay")
                        engine.runAndWait()



