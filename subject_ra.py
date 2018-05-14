import pyautogui as pg
import webbrowser as wb
answer = pg.prompt("""
What's for homework today?
a) English
b) History
c) CME
d) YouTube
""")
if answer == "a":
    wb.open("https://classroom.google.com/c/NTA4OTE5Mjg4MVpa")
elif answer == "b":
    wb.open("https://classroom.google.com/c/NTU1MTQ5OTg4NFpa")
elif answer == "c":
    wb.open("https://sites.google.com/gcds.net/cme/home?authuser=0")
elif answer == "d":
    wb.open("https://www.youtube.com/watch?v=Kk6Y-qaaY-Q")
