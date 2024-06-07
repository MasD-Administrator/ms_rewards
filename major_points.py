import pyautogui as pg
from time import sleep 
from pyscreeze import ImageNotFoundException


class MajorPoints:
    def __init__(self, time_to_redeem_point, wait_time_after_point_collection,
                 ms_rewards_page_loading_time, no_of_scrolls, waiting_time_after_scrolling,
                 waiting_time_before_scrolling, scroll_pause, point10_confidence_rate,
                 point5_confidence_rate, scroll_amount, point10_image_path, point5_image_path):
        self.time_to_redeem_point = time_to_redeem_point
        self.wait_time_after_point_collection = wait_time_after_point_collection
        self.ms_rewards_page_loading_time = ms_rewards_page_loading_time
        self.no_of_scrolls = no_of_scrolls
        self.waiting_time_after_scrolling = waiting_time_after_scrolling
        self.waiting_time_before_scrolling = waiting_time_before_scrolling
        self.scroll_pause = scroll_pause
        self.point10_confidence_rate = point10_confidence_rate
        self.point5_confidence_rate = point5_confidence_rate
        self.scroll_amount = scroll_amount
        self.point5_image_path = point5_image_path
        self.point10_image_path = point10_image_path

    def complete_point_collection(self, point):
        pg.moveTo(point)
        pg.leftClick()
        sleep(self.time_to_redeem_point)
        pg.hotkey("ctrl", "f4")
        sleep(self.wait_time_after_point_collection)

    def collect_points(self):
        res = pg.resolution()

        pg.write("https://rewards.bing.com/")
        pg.press("enter")
        sleep(self.ms_rewards_page_loading_time)

        pg.moveTo(int(res[0]/2), int(res[1]/2))

        for i in range(0, self.no_of_scrolls):
            sleep(self.waiting_time_before_scrolling)
            pg.hscroll(self.scroll_amount)
            sleep(self.waiting_time_after_scrolling)
            try:
                point_10_list = list(pg.locateAllOnScreen(self.point10_image_path, confidence=self.point10_confidence_rate))
                for point_10 in point_10_list:
                    self.complete_point_collection(point_10)
            except ImageNotFoundException:
                pass

            try:    
                point_5_list = list(pg.locateAllOnScreen(self.point5_image_path, confidence=self.point5_confidence_rate))
                for point_5 in point_5_list:
                    self.complete_point_collection(point_5)
            except ImageNotFoundException:
                pass
            sleep(self.scroll_pause)
