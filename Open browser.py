import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")
time.sleep(5)

# как получить URL страницы
current_url = driver.current_url # используем свойство current_url объекта драйвера
page_url = driver.current_url # сохраняем URL в переменную

print(page_url) # принтим URL

if "sauce" in driver.current_url: # при положительном результате принтим
        print("Страница авторизации успешно загружена")
else: # при отрицательном результате принтим
        print("Ошибка: открыта неверная страница")

# получаем заголовок веб-страницы
page_title = driver.title # используем свойство title объекта драйвера
title_page = driver.title # сохраняем title в переменную

print(title_page) # принтим заголовок страницы

