import pyautogui as pg
from time import sleep
import random
from wonderwords import RandomWord



class Search:
    def __init__(self, no_of_searches, type_speed, wait_time_after_opening_tab,
                 wait_time_after_closing_tab, sentence_max_words, time_to_detect_reward_collection):
        self.type_speed = type_speed
        self.wait_time_after_opening_tab = wait_time_after_opening_tab
        self.wait_time_after_closing_tab = wait_time_after_closing_tab
        self.sentence_max_words = sentence_max_words
        self.no_of_searches = no_of_searches
        self.time_to_detect_reward_collection = time_to_detect_reward_collection
        
        for _ in range(0, self.no_of_searches):
            self.new_tab()
            self.actual_search(self.custom_random_sentence())
            sleep(self.time_to_detect_reward_collection)
            self.close_tab()
            
    def actual_search(self, text):
        sleep(.2)
        pg.write(text)
        pg.press("enter")

    def new_tab(self):
        pg.hotkey("ctrl", "t")
        sleep(self.wait_time_after_opening_tab)

    def close_tab(self):
        pg.hotkey("ctrl", "f4")
        sleep(self.wait_time_after_closing_tab)

    def custom_random_sentence(self):
        a = RandomWord()
        string = "how to "
        for i in range(0, self.sentence_max_words):
            string += a.word() + " "

        return string
   

