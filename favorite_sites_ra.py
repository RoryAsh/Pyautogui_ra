import webbrowser
import pyautogui as pg

videos = ["https://www.youtube.com/watch?v=N-NS66JgTeI","https://www.youtube.com/watch?v=DreM0FFFcjI&index=25&list=PLygx92anSc9L5JdsEj4Y-xfi7YxXZcn54"]

music = ["https://www.youtube.com/watch?v=7Ig_Dlhwx0U","https://www.youtube.com/watch?v=wkJrShaOaz0"]

answer = pg.prompt(
"""
What do you want to do?
a) videos
b) music

"""

    )
if answer == "a":
    for i in videos:
        webbrowser.open(i)
elif answer == "b":
    for i in music:
        webbrowser.open(i)
