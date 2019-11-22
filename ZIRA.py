from tkinter import *
import tkinter.messagebox
import keyboard
import stopwatch
import subprocess
import ZIRAbackend       
import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as tts
from playsound import playsound
import misc

mainwindow = Tk(screenName="ZIRA")
mainwindow.configure(background = "#0C4C5D")
misc.wishMe()
engine = tts.init()
engine.say('I am your personal assistant Zira.')
engine.runAndWait()

photo = PhotoImage(file = r"C:\Users\anshc\OneDrive\Documents\ZIRA\rsz_apollobutton.png")
mainwindow.title("ZIRA")
headinglabel = Label(mainwindow, text="ZIRA - THE VIRTUAL ASSISTANT", bg= '#0C4C5D', fg= "white", font='Bahnschrift 24 bold')

btncreateitems = Button(mainwindow, text='Click here to ask me anything', image = photo ,width=300, font='times 20 bold', command=ZIRAbackend.zira)

                
headinglabel.place(relx=0.5, rely=0.1, anchor=CENTER)
btncreateitems.place(relx=0.5, rely=0.5, anchor=CENTER)


width = 800
height = 500
screenwidth = mainwindow.winfo_screenwidth()
screenheight = mainwindow.winfo_screenheight()

# Make it center screen
x = str(int(screenwidth / 2 - width / 2))
y = str(int(screenheight / 2 - height / 2))
s = '800x500+' + x + '+' + y
mainwindow.geometry(s)
mainwindow.resizable(width=False, height=False)

mainwindow.mainloop()


