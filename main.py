from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from fake_useragent import UserAgent
from sys import platform

import os
import datetime
import time


def path_chrome_driver():
    # Функция определяющая полного пути к драйверу
    if platform in ['linux1', 'linux2']:
        return os.getcwd() + os.sep + 'chromedriver'

    if platform in ['win32']:
        return os.getcwd() + os.sep + 'chromedriver.exe'


def authorization():
    # Функция авторизации на сайте
    driver.find_element(By.ID, 'loginInput').send_keys('KarasikDE')
    driver.find_element(By.ID, 'passInput').send_keys('Kar-2003')
    driver.find_element(By.ID, 'enter_btn').click()

    if find_request('/j_security_check') == 303:
        print('Авторизация OK')
        return
    else:
        print('Неверный логин или пароль')
        raise


def get_site(url):
    # Функция перехода на сайт
    driver.get(url)

    while True:
        time.sleep(5)
        a = find_request(url)
        if a == 200:
            print(f'Получен заголовок сайта: {driver.title}, Код ответа {a}')
            return
        else:
            print(f'Ошибка загрузки сайта: {driver.title}, Код ответа {a}. Перезагрузка...')
            driver.refresh()


def find_request(url):
    # Функция поиска кода страницы по адресу запроса
    for request in driver.requests:
        if request.url.find(url) >= 0:
            return request.response.status_code


def get_click(elem_cls, elem_name):
    # Процедура клика по элементам сайта
    a = 3
    while True:
        try:
            time.sleep(10)
            for elem in driver.find_elements(By.CLASS_NAME, elem_cls):
                if elem.text == elem_name:
                    elem.click()
                    return
            raise

        except:
            if a == 0:
                print(f'Не удалось нажать на кнопку {elem_name} в разделе {elem_cls}')
                raise
            else:
                print(f'Ожидание загрузки кнопки {elem_name} в разделе {elem_cls}. попыток осталось {a}')
                a -= 1


def main():
    # Основная функция выполнения программы
    try:
        print(f'Переход на сайт: {urlLogin}')
        get_site(urlLogin)

        print(f'Авторизация LOGIN: "KarasikDE", PASS: {"*" * len("Kar-2003")}')
        authorization()

        print(f'Переход на сайт: {urlWork}')
        get_site(urlWork)

        print('Нажатие на кнопку <<Добавить инспекцию>>')
        get_click(elem_cls='af_toolbar_item', elem_name='add')

        print('Нажатие на кнопку << RFI (строительный контроль)>>')
        get_click(elem_cls='af_commandToolbarButton_text', elem_name='RFI (строительный контроль)')

    except Exception as ex:
        print(ex)


    finally:
        os.system('pause')
        driver.close()
        driver.quit()


if __name__ == '__main__':
    # Страница завершения сеанса
    urlStop = 'https://agpz.sgaz.pro/http/utils/resourceServlet/adaptive/error/serverShutdown.html'

    # Страница авторизации АИС НСК
    urlLogin = 'https://agpz.sgaz.pro/faces/zeroLevelOOP'

    # Страница приложения с инспекциями
    urlWork = 'https://agpz.sgaz.pro/faces/page/contracts/48899/build-tracker/tasks'

    # Информация об эмуляторе браузера
    useragent = UserAgent()

    # Опции запуска Chrome driver:
    options = webdriver.ChromeOptions()

    options.add_argument(f"user-agent={useragent.chrome}")  # User-Agent Браузера

    options.add_argument("--headless")                      # Загружает заголовки сайта
    options.add_argument("--no-sandbox")                    # 
    options.add_argument("--disable-dev-shm-usage")         #
    options.add_argument("--disable-extensions")            # Опция при которой браузер открывается с отключенными расширениями
    options.add_argument("--start-maximized")               # Опция при которой браузер открывается на весь экран
    options.add_argument("--disable-gpu")                   # Отключение использования GPU
    options.add_argument("--dns-prefetch-disable")          #
    options.add_argument('--ignore-certificate-errors')     # Игнорировать ошибки сертификатов SSL

    # Отключение системы автоматизации контроля браузера
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Отключение системного логирования при исполнении кода
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # Настройка для отображения экрана браузера
    options.headless = False

    service = Service(path_chrome_driver())


    # Запуск драйвера с установленными параметрами
    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    driver.get('https://www.whatismybrowser.com/detect/what-is-my-user-agent/')

    

    os.system('pause')
    driver.close()
    driver.quit()

    # Запуск основного макроса исполнения
    # main()
