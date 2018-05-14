import win32com.client as win
import pyautogui as pg


speak = win.Dispatch("SAPI.SpVoice")
    
speak.Speak("What's your favorite musical genre?")

answer = pg.prompt("Enter your favorite genre below.")

if answer == "rock":
    speak.Speak("I like to rock out, too.")

elif answer == "jazz":
    speak.Speak("Groovy, soulful saxophone.")
