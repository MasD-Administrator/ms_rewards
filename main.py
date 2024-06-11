import pyautogui as pg
from time import sleep

import searching
import major_points


def open_browser():
    pg.hotkey("win", "r")
    pg.write("microsoft-edge: --start-maximized")
    pg.press("enter")
    sleep(1)


accounts_opened = 0

def open_next_account():
    global accounts_opened

    accounts_opened += 1

    pg.hotkey("Ctrl", "Shift", "m")
    for i in range(0, 7 + accounts_opened):
        pg.press("tab")
        sleep(0.08)

    pg.press("enter")
    sleep(.6)

def open_specific_account(no_on_list):
    global accounts_opened
    accounts_opened += 1
    pg.hotkey("Ctrl", "Shift", "m")
    for i in range(0, 7 + no_on_list):
        pg.press("tab")
        sleep(0.08)

    pg.press("enter")
    sleep(.6)

def close_account():
    pg.hotkey("alt", "f4")
    sleep(.8)

def main():
    searcher = searching.Search(30, .1, .1, .1, 3, 2)
    # 697 is the optimal no of scroll clicks to make the whole page move so that the same picture is 
    # not shown again when searching for images of points (is that really neccessary)
    mp = major_points.MajorPoints(2.7, .2, 3, 8, .2, .2, .2, .96, .96, -697,  "+10points.png", "+5points.png")

    
    open_browser()

    for i in range(0, 3):
        open_next_account()
        sleep(.4)
        close_account()

if __name__ == "__main__":
    main()