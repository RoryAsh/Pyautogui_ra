import win32com.client as win
import pyautogui as pg
import webbrowser as wb
import speech_recognition as sr

speak = win.Dispatch("SAPI.SpVoice")



r = sr.Recognizer()
with sr.Microphone() as source:
    speak.Speak("Hey, Rory! What should we search for today? Just kidding, I do the real work, you just talk.")
    print("Checking that you're not a robot ...")
    audio = r.listen(source)
    print("Double checking ...")
    print("Triple checking ...")


try:
    words = r.recognize_google(audio)
    speak.Speak("Ok Rory, you have proved you are not a robot! Searching for " + r.recognize_google(audio)) 
    wb.open("https://www.youtube.com/results?search_query=" + words)


except sr.UnknownValueError:
    print("Turn's out, you're a robot. No but actually, I could not understand you. Try again!")
except sr.RequestError as e:
    print("Couldn't connect to Internet. Or you are secretly a robot.")
