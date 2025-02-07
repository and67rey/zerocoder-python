# Парсинг цен на диваны с сайта divan.ru в csv файл,
# обработка полученных данных, нахождение средней цены,
# построение гистограммы цен на диваны с сайта divan.ru

import pandas as pd
import csv
import matplotlib.pyplot as plt
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver = webdriver.Firefox()

# url = 'https://www.divan.ru/rostov-na-donu/category/svet'
url = 'https://www.divan.ru/rostov-na-donu/category/divany-i-kresla'

driver.get(url)

time.sleep(3)

lights = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')

print(f'Количество светильников на странице {len(lights)}\n')

parsed_data = []

# Используем конструкцию try-except, чтобы "ловить" ошибки, как только они появляются
for light in lights:
   try:
     # name = light.find_element(By.CSS_SELECTOR, 'div.lsooF').find_element(By.CSS_SELECTOR, 'span').text
     price = light.find_element(By.CSS_SELECTOR, 'div.q5Uds').find_element(By.CSS_SELECTOR, 'span').text
     price = price.replace('руб.', '')
     price = price.replace(' ', '')
     price = int(price)
     # link = light.find_element(By.CSS_SELECTOR, 'link').get_attribute('href')
   except:
     print("произошла ошибка при парсинге")
     continue

   parsed_data.append(price)

driver.quit()

print(parsed_data)

df = pd.DataFrame(parsed_data)
print(df.describe())
print()
mean_price = df.mean()
print(f'Среднее значение цены на диваны {mean_price}')
print()

df.to_csv('divan_prices.csv', index=False)

# Построение гистограммы
bins = 10
plt.hist(parsed_data, bins=bins, edgecolor='black')
# Добавление заголовка и меток осей
plt.title('Гистограмма цен на диваны на сайте divan.ru')
plt.xlabel('Цена на диван, руб.')
plt.ylabel('Частота')
# Показать гистограмму
plt.show()