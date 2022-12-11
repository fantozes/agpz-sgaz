from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import datetime
import os

# Страница авторизации АИС НСК
urlLogin = 'https://agpz.sgaz.pro/faces/zeroLevelOOP'

# Страница приложения с инспекциями
urlWork = 'https://agpz.sgaz.pro/faces/page/contracts/48899/build-tracker/tasks'

# Опции запуска Chrome driver
options = Options()
options.add_argument("--disable-extensions")

# Определение полного пути к драйверу хром
path_crome_driver = os.getcwd() + os.sep + 'chromedriver'
driver = webdriver.Chrome(service=path_crome_driver, options=options)


def authorization():
    print(f'Авторизация LOGIN: "ваш_логин", PASS: {"*" * len("ваш_пароль")}')


def main():

    print(f'Переход на сайт: {urlLogin}')

    driver.get(urlLogin)
    driver.maximize_window()    # Развернуть браузер на весь экран
    print(f'Получен заголовок сайта: {driver.title}')

    time.sleep(2)

    authorization()


if __name__ == '__main__':
    main()
