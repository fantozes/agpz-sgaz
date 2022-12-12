from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from fake_useragent import UserAgent
from sys import platform

import os
import datetime
import time


# Страница завершения сеанса
urlStop = 'https://agpz.sgaz.pro/http/utils/resourceServlet/adaptive/error/serverShutdown.html'

# Страница авторизации АИС НСК
urlLogin = 'https://agpz.sgaz.pro/faces/zeroLevelOOP'

# Страница приложения с инспекциями
urlWork = 'https://agpz.sgaz.pro/faces/page/contracts/48899/build-tracker/tasks'

# Информация об эмуляторе браузера
useragent = UserAgent()

# Опции запуска Chrome driver:
options = Options()
options.add_argument("--disable-extensions")        # Опция при которой браузер открывается с отключенными расширениями
options.add_argument("--start-maximized")           # Опция при которой браузер открывается на весь экран
options.add_argument("--no-sandbox")                # 
options.add_argument("--disable-dev-shm-usage")     # 

# Отключение системного логирования при исполнении кода
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# Настройка для отображения экрана браузера
options.headless = False


def path_crome_driver():
    # Функция определяющая полного пути к драйверу
    if platform in ['linux1', 'linux2']:
        return os.getcwd() + os.sep + 'chromedriver'

    if platform in ['win32']:
        return os.getcwd() + os.sep + 'chromedriver.exe'


path_crome_driver = os.getcwd() + os.sep + 'chromedriver'
driver = webdriver.Chrome(executable_path=path_crome_driver, options=options)


def authorization():
    # Функция авторизации на сайте
    driver.find_element(By.ID, 'loginInput').send_keys('KarasikDE')
    driver.find_element(By.ID, 'passInput').send_keys('Kar-2003')
    driver.find_element(By.ID, 'enter_btn').click()

    for request in driver.requests:
        if request.response:
            if request.url.find('/j_security_check') > 0:
                if request.response.status_code == 303:
                    print('Авторизация OK')
                    return
                else:
                    print('Неверный логин или пароль')
                    raise


def get_site(url):
    # Функция перехода на сайт
    driver.get(url)

    while True:
        for request in driver.requests:
            if (request.url == url):
                print(f'Получен заголовок сайта: {driver.title}')
                a = request.response.status_code
                if (a == 200):
                    return
                else:
                    print(f'Ошибка загрузки сайта: {a} Перезагрузка...')
                    driver.refresh()
        time.sleep(2)


def get_click(elem_cls, elem_name):
    # Процедура клика по элементам сайта
    while True:
        try:
            driver.find_elements(By.CLASS_NAME, 'elem_cls').find_element(By.XPATH,'elem_name').click()
        except:
            time.sleep(2)


def main():
    # Основная функция выполнения программы
    try:
        print(f'Переход на сайт: {urlLogin}')
        get_site(urlLogin)

        print(f'Авторизация LOGIN: "KarasikDE", PASS: {"*" * len("Kar-2003")}')
        authorization()

        print(f'Переход на сайт: {urlWork}')
        get_site(urlWork)


    except Exception as ex:
        print(ex)


    finally:
        os.system('pause')
        driver.quit
        driver.close


if __name__ == '__main__':
    main()
