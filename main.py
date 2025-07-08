import pyautogui as pg
from time import sleep
import json

import searching
import major_points

data_file = open("data.json", "r")
data = json.load(data_file)

no_of_seraches = data["no_of_seraches"]
type_speed = data["type_speed"]
wait_time_after_opening_tab = data["wait_time_after_opening_tab"]
wait_time_after_closing_tab = data["wait_time_after_closing_tab"]
sentence_max_words = data["sentence_max_words"]
time_to_detect_reward_collection = data["time_to_detect_reward_collection"]
no_of_seractime_to_redeem_pointhes = data["time_to_redeem_point"]
wait_time_after_point_collection = data["wait_time_after_point_collection"]
ms_reward_page_loading_time = data["ms_reward_page_loading_time"]
no_of_scrools = data["no_of_scrools"]
no_of_serwaiting_time_after_scrollingches = data["waiting_time_after_scrolling"]
waiting_time_before_scrolling = data["waiting_time_before_scrolling"]
waiting_time_after_scrolling= data["waiting_time_after_scrolling"]
scroll_pause = data["scroll_pause"]
point_10_confidence_rate = data["point_10_confidence_rate"]
point_5_confidence_rate = data["point_5_confidence_rate"]
scroll_amount = data["scroll_amount"]
time_to_redeem_point = data["time_to_redeem_point"]

print(data)
data_file.close()

def open_browser():
    pg.hotkey("win", "r")
    pg.write("microsoft-edge: --start-maximized")
    pg.press("enter")
    sleep(.9)
    pg.hotkey("ctrl", "t")
    sleep(.9)
    

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
    open_browser()
    
    searching.Search(no_of_seraches, type_speed, wait_time_after_opening_tab ,wait_time_after_closing_tab, sentence_max_words, time_to_detect_reward_collection)
    major_points.MajorPoints(time_to_redeem_point, wait_time_after_point_collection, ms_reward_page_loading_time, no_of_scrools, waiting_time_after_scrolling, waiting_time_before_scrolling, scroll_pause, point_10_confidence_rate, point_5_confidence_rate, scroll_amount)

    

if __name__ == "__main__":
    main()