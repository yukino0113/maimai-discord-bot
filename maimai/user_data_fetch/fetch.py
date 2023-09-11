import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from auth import Auth
import requests
import warnings
warnings.filterwarnings('ignore')

"""
difficulty = 0
uid = '8024177546069'
url = f'https://maimaidx-eng.com/maimai-mobile/friend/friendGenreVs/battleStart/' \
       f'?scoreType=2&genre=99&diff={difficulty}&idx={uid}'

driver = webdriver.Edge()
#option.add_argument('headless')
driver.get(url)
time.sleep(10)
"""
option = webdriver.EdgeOptions()
#option.headless = True
driver = webdriver.Edge(option)
driver.get('https://maimaidx-eng.com/maimai-mobile/home/')


if sega_id_button := driver.find_element(By.XPATH, "//section[@id='segaid']//span[@class='c-button--openid--segaId']"):
    sega_id_button.click()
    driver.find_element(By.NAME, 'sid').send_keys(Auth.account)
    driver.find_element(By.NAME, 'password').send_keys(Auth.password)
    driver.find_element(By.ID, 'btnSubmit').click()

driver.get('https://maimaidx-eng.com/maimai-mobile/friend/friendDetail/?idx=8024177546069')
time.sleep(1000)