import pyautogui as pg
import webbrowser as wb
answer = pg.confirm(text="How do you feel right now?", title="Describe your emotion", buttons=['sadness', 'suicidal', 'fear', 'anger', 'regret', 'contentment'])
if answer == "suicidal":
    pg.confirm(text="Put your hand over your heart, can you feel it? That is called your purpose. You are alive for a reason, so do not give up.")
    wb.open("https://suicidepreventionlifeline.org/")   
elif answer == "anger":
    pg.confirm(text="He who angers you conquers you.")
    wb.open("https://www.youtube.com/watch?v=L7WeJ2LTQag")
elif answer == "sadness":
        pg.confirm(text="It will all be okay in the end. If it's not okay, it's not the end.")
        wb.open("https://www.youtube.com/watch?v=96kI8Mp1uOU")
elif answer == "fear":
    pg.confirm(text="Courage is resistance to fear, mastery of fear, not absence of fear.")
    wb.open("https://www.youtube.com/watch?v=Hhk4N9A0oCA")
elif answer == "regret":
    pg.confirm(text="We all have mistakes, have struggles, and even regret things in our past. But you are not your mistakes, you are not your struggles, and you are here now with the power to shape your day and your future.")
    wb.open("https://www.youtube.com/watch?v=LhpsXSIGnPk")
elif answer == "contentment":
    pg.confirm(text="Happiness is not a state to arrive at, but a manner of traveling.")
    wb.open("https://www.youtube.com/watch?v=ZbZSe6N_BXs")
