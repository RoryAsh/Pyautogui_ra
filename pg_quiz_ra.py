import pyautogui as pg
import time
import webbrowser
points = 0
answer = pg.prompt(
"""
Which would you rather do?

a) Sketch
b) Read a book
c) Write a public speaking piece
d) Surf the internet for sports videos

"""
    )

if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3
elif answer == "d":
    points +=4
answer = pg.prompt(
"""
What is your favorite place?

a) Art studio
b) Library
c) Theater
d) Gym

"""
    )

if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3
elif answer == "d":
    points +=4
answer = pg.prompt(
"""
Out of the following, what is your favorite word?

a) Visual
b) Language
c) Performance
d) Drive

"""
    )

if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3
elif answer == "d":
    points +=4


#END OF SURVEY
pg.alert("You are...")

#Artist
if points < 5:
    pg.alert("Leonardo Da Vinci")
    webbrowser.open("https://www.biography.com/.image/c_fill%2Ccs_srgb%2Cg_face%2Ch_170%2Cq_80%2Cw_300/MTQ1NDY3NjE3MTc0MzY1OTY5/leonardo-da-vinci---notebooks.jpg")
#Author
if points >= 5 and points <8:
    pg.alert("Leo Tolstoy")
    webbrowser.open("https://images-na.ssl-images-amazon.com/images/I/51BPFtEJLnL._SX322_BO1,204,203,200_.jpg")
#Actor
if points >=8 and points <12:
    pg.alert("Shakespeare")
    webbrowser.open("http://www.quotespie.com/wp-content/uploads/2016/02/shakespeare_quote_5b_post_cards-r189b5d924a1549caace5185a09775e33_vgbaq_8byvr_512.jpg")
#Athlete
if points >=12:
    pg.alert("Julius Erving")
    webbrowser.open("http://www.azquotes.com/picture-quotes/quote-attitude-is-altitude-julius-erving-56-22-78.jpg")
