from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import datetime
import os

urlLogin = 'https://agpz.sgaz.pro/faces/zeroLevelOOP'

urlWork = 'https://agpz.sgaz.pro/faces/page/contracts/48899/build-tracker/tasks'

options = Options()

options.add_argument("--disable-extensions")


driver = webdriver.Chrome(executable_path='./chromedriver', options=options)


def authorization():
    print(f'Авторизация LOGIN: "ваш_логин", PASS: {"*" * len("ваш_пароль")}')


def main():

    print(f'Переход на сайт: {urlLogin}')

    driver.get(urlLogin)
    print(f'Получен заголовок сайта: {driver.title}')

    time.sleep(2)

    authorization()


if __name__ == '__main__':
    main()
