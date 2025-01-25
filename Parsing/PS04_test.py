from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

driver = webdriver.Chrome()

url = 'https://ru.wikipedia.org/w/index.php?go=%D0%9F%D0%B5%D1%80%D0%B5%D0%B9%D1%82%D0%B8&search=%D0%92%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F&title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F%3A%D0%9F%D0%BE%D0%B8%D1%81%D0%BA&ns0=1'
# Зайти на веб-страницу по заданному URL
driver.get(url)
time.sleep(3)

# Найти все ссылки на странице
elements = driver.find_elements(By.TAG_NAME, 'a')

# Сохранить ссылки в словарь
links_dict = {}
for element in elements:
    link_text = element.text
    link_href = element.get_attribute('href')

    # Проверка на пустые значения
    if link_text and link_href:
        links_dict[link_text] = link_href

print(f'Всего ссылок на странице:{len(links_dict)}')

for key, value in links_dict.items():
       print(f"Название ссылки: {key},\n ссылка: {value}\n")
       choice = input('Нажмите Enter, чтобы дальше листать ссылки, 1 - для перехода по текущей ссылке, 0 - для завершения: ')
       if choice == '0':
           break
       elif choice == '1':
           driver.get(value)
           break

time.sleep(10)

driver.quit()