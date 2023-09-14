import os
from maimai.user_data_fetch.user import User
from selenium.webdriver.common.by import By
from selenium import webdriver
import warnings
from dotenv import load_dotenv

load_dotenv()
warnings.filterwarnings('ignore')

"""
difficulty = 0
uid = '8024177546069'
url = f'https://maimaidx-eng.com/maimai-mobile/friend/friendGenreVs/battleStart/' \
       f'?scoreType=2&genre=99&diff={difficulty}&idx={uid}'
"""


class MaimaiNet:

    def __init__(self):
        option = webdriver.EdgeOptions()
        # option.headless = True
        self.driver = webdriver.Edge(option)
        self.driver.get('https://maimaidx-eng.com/maimai-mobile/home/')
        self.login()

    def __login(self):
        self.driver.find_element(By.XPATH,
                                 "//section[@id='segaid']//span[@class='c-button--openid--segaId']").click()
        self.driver.find_element(By.NAME, 'sid').send_keys(os.getenv("ACCOUNT"))
        self.driver.find_element(By.NAME, 'password').send_keys(os.getenv("PW"))
        self.driver.find_element(By.ID, 'btnSubmit').click()

    def add_friends(self):
        pass

    def fetch_song_score(self):
        pass

    def fetch_user_information(self):
        pass



def open_browser():
    option = webdriver.EdgeOptions()
    # option.headless = True
    driver = webdriver.Edge(option)
    driver.get('https://maimaidx-eng.com/maimai-mobile/home/')

    if sega_id_button := driver.find_element(By.XPATH,
                                             "//section[@id='segaid']//span[@class='c-button--openid--segaId']"):
        sega_id_button.click()
        driver.find_element(By.NAME, 'sid').send_keys(os.getenv("ACCOUNT"))
        driver.find_element(By.NAME, 'password').send_keys(os.getenv("PW"))
        driver.find_element(By.ID, 'btnSubmit').click()

    return driver


def fetch_song_score(user: User):
    # driver = open_browser()
    # todo: add to favorites
    for i in range(0, 5):
        print(i)


def fetch_user_information(friend_code):
    driver = open_browser()
    driver.get(f'https://maimaidx-eng.com/maimai-mobile/friend/friendDetail/?idx={friend_code}')
