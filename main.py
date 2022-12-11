import os
import datetime
import time
import configparser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from fake_useragent import UserAgent

config = configparser.ConfigParser()
config.read('user.ini')
lng = config.get('User Data', 'login')
psw = config.get('User Data', 'Pass')

# Страница завершения сеанса
urlStop = 'https://agpz.sgaz.pro/http/utils/resourceServlet/adaptive/error/serverShutdown.html'

# Страница авторизации АИС НСК
urlLogin = 'https://agpz.sgaz.pro/faces/zeroLevelOOP'

# Страница приложения с инспекциями
urlWork = 'https://agpz.sgaz.pro/faces/page/contracts/48899/build-tracker/tasks'

# Информация об эмуляторе браузера
useragent = UserAgent()

# Опции запуска Chrome driver
options = Options()
options.add_argument("--disable-extensions")
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')


# Определение полного пути к драйверу хром
path_crome_driver = os.getcwd() + os.sep + 'chromedriver'
driver = webdriver.Chrome(service=path_crome_driver, options=options)


def authorization():
    print(f'Авторизация LOGIN: {lng}, PASS: {"*" * len(psw)}')


def main():
    try:
        print(f'Переход на сайт: {urlLogin}')

        driver.get(urlLogin)
        driver.maximize_window()    # Развернуть браузер на весь экран
        print(f'Получен заголовок сайта: {driver.title}')

        time.sleep(2)

        authorization()

    except Exception as ex:
        print(ex)

    finally:
        driver.quit
        driver.close


if __name__ == '__main__':
    main()
