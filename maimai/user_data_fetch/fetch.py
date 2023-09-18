import os
from maimai.user_data_fetch.user import User
from selenium.webdriver.common.by import By
from common.driver_base import DriverBase
import warnings
from dotenv import load_dotenv
from maimai.user_data_fetch.html_parser import Parser

load_dotenv()
warnings.filterwarnings('ignore')

"""
difficulty = 0
uid = '8024177546069'
url = f'https://maimaidx-eng.com/maimai-mobile/friend/friendGenreVs/battleStart/' \
       f'?scoreType=2&genre=99&diff={difficulty}&idx={uid}'
"""


class MaimaiNet(Parser, DriverBase):

    def __init__(self):
        super().__init__()
        self.open_url('https://maimaidx-eng.com/maimai-mobile/home/')
        self.__login()

    def __login(self):
        self.click([By.XPATH, "//section[@id='segaid']//span[@class='c-button--openid--segaId']"])
        self.send_keys([By.NAME, 'sid'], os.getenv("ACCOUNT"))
        self.send_keys([By.NAME, 'password'], os.getenv("PW"))
        self.click([By.ID, 'btnSubmit'])

    def refresh(self):
        self.fetch_user_information()
        self.fetch_song_score()

    def add_friends(self, user_id, friend_code):

        if type(user := self.fetch_user_information(user_id, friend_code)) == str:
            return f'好友碼錯誤，請再次確認'

        if invite := self.finds([By.NAME, 'invite']):
            invite[0].click()
            self.driver.switch_to.alert.accept()
            return f'已發送好友邀請至玩家名稱: {user["name"]} ，請至 maimai net 接受邀請'  # todo: change to user.name
        else:
            status = self.find([By.CSS_SELECTOR, '.t_r.m_t_5.gray.f_13']).text
            if status == 'Friend signed in':
                return f'已成功加入好友，可以開始使用功能'
            else:
                return f'邀請已發送，請至 maimai net 確認邀請'

    def add_favorites(self):
        self.click()

    def remove_favorite(self):
        self.click()

    def fetch_song_score(self):
        self.add_favorites()

    def fetch_user_information(self, user_id, friend_code):

        self.open_url('https://maimaidx-eng.com/maimai-mobile/friend/search/')
        self.send_keys([By.NAME, 'friendCode'], friend_code)
        self.click([By.TAG_NAME, 'button'])

        if self.finds([By.CSS_SELECTOR, '.see_through_block.m_15.p_15.f_14.t_c']):
            return f'好友碼錯誤，請再次確認'

        user_info = {
            "name": self.find([By.CSS_SELECTOR, '.name_block.f_l.f_16']).text,
            "title": self.find([By.CLASS_NAME, 'trophy_inner_block']).text,
            "rating": self.find([By.CLASS_NAME, 'rating_block']).text,
            "rating_board": self.find([By.CSS_SELECTOR, '.h_30.f_r']).get_attribute('src'),
            "kyu": self.find([By.CSS_SELECTOR, '.h_35.f_l']).get_attribute('src'),
            "rank": self.find([By.CSS_SELECTOR, '.p_l_10.h_35.f_l']).get_attribute('src'),
        }

        User(user_id, friend_code).set_attributes(user_info)

        return user_info


def fetch_song_score(user: User):
    # driver = open_browser()
    # todo: add to favorites
    for i in range(0, 5):
        print(i)
