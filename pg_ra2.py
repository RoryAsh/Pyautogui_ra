import pyautogui as pg
import time
pg.hotkey('winleft','ctrl','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',0.5)
pg.hotkey('winleft','up')
pg.typewrite('youtube.com\n',0.5)
time.sleep(3)
pg.hotkey('ctrl','t')
pg.typewrite('gcds.net\n',0.5)
pg.moveTo(1212, 185, 2)
pg.click(1101, 191, 1)
pg.typewrite('upper school\n',0.5)

