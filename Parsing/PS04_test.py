from selenium import webdriver
from selenium.webdriver import Keys
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
while True:
    choice = input('Нажмите Enter для вывода случайно ссылки или 0 для завершения: ')
    if choice == '0':
        break
    else:
        random_item = random.choice(list(links_dict.items()))
        print(f"Случайная пара: ключ: {random_item[0]}, значение: {random_item[1]}")

driver.quit()

# for link_text, link_href in links_dict.items():
#     print(f"Название: {link_text}, Ссылка: {link_href}")