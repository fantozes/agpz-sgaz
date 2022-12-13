from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from fake_useragent import UserAgent
from sys import platform

from time import sleep


import os
import datetime



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

# Функция определяющая полного пути к драйверу
if platform in ['linux1', 'linux2']:
    service = Service(os.getcwd() + os.sep + 'chromedriver')
if platform in ['win32']:
    service = Service(os.getcwd() + os.sep + 'chromedriver.exe')

# Запуск драйвера с установленными параметрами
driver = webdriver.Chrome(service=service, options=options)


def authorization():
    # Функция авторизации на сайте
    while True:
        try:
            driver.find_element(By.ID, 'loginInput').send_keys('KarasikDE')
            driver.find_element(By.ID, 'passInput').send_keys('Kar-2003')
            driver.find_element(By.ID, 'enter_btn').click()
            return
        except:
            driver.refresh()
        finally:
            sleep(5)


def get_site(url):
    # Функция перехода на сайт
    driver.get(url)
    sleep(5)
    print(f'Получен заголовок страницы сайта: {driver.title}')


def dec_text_click(func):
    # Декоратор для функции клика и ввода текста
    def wrapper(*args, **kwargs):
        a = 3
        while True:
            sleep(5)
            try:
                return_func = func(*args, **kwargs)
                if (return_func) == 0:
                    return return_func
                else:
                    raise
            except:
                if a == 0:
                    print(f'Ошибка: {kwargs}')
                    raise
                else:
                    print(f'Ожидание загрузки: {kwargs}. Попыток осталось {a}')
                    a -= 1
    return wrapper


@dec_text_click
def get_click(elem_cls, elem_name):
    # Функция клика по элементам сайта
    for elem in driver.find_elements(By.CLASS_NAME, elem_cls):
        if elem.text == elem_name:
            elem.click()
            return 0
    raise

@dec_text_click
def get_text(elem_xpath,  val):
    # Функция ввода текста в поля заполнения
    driver.find_element(By.XPATH, elem_xpath).send_keys(val)
    return 0


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

        print('Нажатие на кнопку <<RFI (строительный контроль)>>')
        get_click(elem_cls='af_commandToolbarButton_text', elem_name='RFI (строительный контроль)')

        out_number = '5-40-HP41001-002'
        print(f'Заполнение формы: Исходящий номер: {out_number}')
        get_text(elem_xpath='//*[@id="C8zap53_2::content"]', val=out_number)
        
        out_date = '13.12.2022 14:48'
        print(f'Заполнение формы: Дата и время инспекции: {out_date}')
        get_text(elem_xpath='//*[@id="C8zl006_2::content"]', val=out_date)

        out_groupwork = 'Технологические трубопров'
        print(f'Заполнение формы: Группа работ: {out_groupwork}')
        get_text(elem_xpath='//*[@id="gihyoe_2-suggest-input"]', val=out_groupwork)
        sleep(1)
        driver.find_element(By.XPATH, '//*[@id="gihyoe_2-suggest-input"]').send_keys(Keys.ENTER)

        print('Нажатие на кнопку выбора структур')
        get_click(elem_cls='af_panelLabelAndMessage_content-cell', elem_name='<не выбраны>')




    except Exception as ex:
        print(ex)
    finally:
        os.system('pause')
        driver.close()
        driver.quit()


if __name__ == '__main__':

    # driver.get('https://www.whatismybrowser.com/detect/what-is-my-user-agent/')
    # os.system('pause')
    # driver.close()
    # driver.quit()

    # Запуск основного макроса исполнения
    main()
