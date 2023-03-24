import os
import time

import chromedriver_binary
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

load_dotenv()

option = Options()
option.add_argument('--headless')

driver = webdriver.Chrome('chromedriver.exe', options=option)

driver.get('https://diskunion.net/ec/ct/mypage')
time.sleep(3)
mail = driver.find_element(By.NAME, 'email_address')
password = driver.find_element(By.NAME, 'password')
mail.send_keys(os.environ['MAIL'])
password.send_keys(os.environ['PASSWORD'])

password.submit()

time.sleep(1)

driver.get('https://diskunion.net/ec/ct/fav_goods')

time.sleep(1)

tables = driver.find_elements(By.CLASS_NAME, 'tag-normal--blue')
for table in tables:
    elem = table.find_element(By.TAG_NAME, 'a')
    href = elem.get_attribute("href")
    print(href)