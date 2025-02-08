# Парсинг цен на диваны с сайта divan.ru в csv файл,
# обработка полученных данных, нахождение средней цены,
# построение гистограммы цен на диваны с сайта divan.ru

import pandas as pd
import matplotlib.pyplot as plt
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://www.divan.ru/sankt-peterburg/category/divany-i-kresla'
driver.get(url)
time.sleep(3)

divans = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')

print(f'Количество диванов на странице {len(divans)}\n')

parsed_data = []

# Используем конструкцию try-except, чтобы "ловить" ошибки, как только они появляются
for divan in divans:
   try:
     price = divan.find_element(By.CSS_SELECTOR, 'div.q5Uds').find_element(By.CSS_SELECTOR, 'span').text
     price = price.replace('руб.', '')
     price = price.replace(' ', '')
     price = int(price)
   except:
     print("произошла ошибка при парсинге")
     continue

   parsed_data.append(price)

driver.quit()

print('Список цен на диваны по результатам парсинга с сайта divan.ru')
print(parsed_data)
print()

# Создание DataFrame в pandas
data = {'Цена на диван': parsed_data}
df = pd.DataFrame(data)
print(df.describe())
print()

# Вычисление среднего значения цен на диваны
mean_price = df['Цена на диван'].mean()
print(f'Среднее значение цены на диваны: {round(mean_price, 2)} руб.')
print()

# Сохранение данных в csv файл
df.to_csv('divan_prices.csv', index=False)

# Построение гистограммы цен на диваны
bins = 20
plt.hist(df, bins=bins, edgecolor='black')
# Добавление заголовка и меток осей
plt.title('Гистограмма цен на диваны на сайте divan.ru')
plt.xlabel('Цена на диван, руб.')
plt.ylabel('Частота')
# Вывод гистограммы
plt.show()