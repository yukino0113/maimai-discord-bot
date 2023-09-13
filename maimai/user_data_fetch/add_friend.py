from selenium.webdriver.common.by import By
from maimai.user_data_fetch.fetch import open_browser


def add_friend(friend_code) -> str:
    driver = open_browser()
    driver.get('https://maimaidx-eng.com/maimai-mobile/friend/search/')
    driver.find_element(By.NAME, 'friendCode').send_keys(friend_code)
    driver.find_element(By.TAG_NAME, 'button').click()

    if driver.find_elements(By.CSS_SELECTOR, '.see_through_block.m_15.p_15.f_14.t_c'):
        return f'好友碼錯誤，請再次確認'

    name = driver.find_element(By.CSS_SELECTOR, '.name_block.f_l.f_16').text

    if invite_button := driver.find_elements(By.NAME, 'invite'):
        invite_button[0].click()
        driver.switch_to.alert.accept()
        return f'已發送好友邀請至玩家名稱: {name} ，請至 maimai net 接受邀請'
    else:
        if status := driver.find_element(By.CSS_SELECTOR, '.t_r.m_t_5.gray.f_13').text:
            if status == 'Friend signed in':
                return f'已成功加入好友，可以開始使用功能'
            else:
                return f'邀請已發送，請至 maimai net 確認邀請訊息'
    pass