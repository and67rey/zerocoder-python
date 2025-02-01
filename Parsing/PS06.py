import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver = webdriver.Firefox()

url = 'https://www.divan.ru/rostov-na-donu/category/svet'

driver.get(url)

time.sleep(3)

lights = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')

print(f'Количество светильников на странице {len(lights)}\n')

parsed_data = []

# Используем конструкцию try-except, чтобы "ловить" ошибки, как только они появляются
for light in lights:
   try:
     name = light.find_element(By.CSS_SELECTOR, 'div.lsooF').find_element(By.CSS_SELECTOR, 'span').text
     price = light.find_element(By.CSS_SELECTOR, 'div.q5Uds').find_element(By.CSS_SELECTOR, 'span').text
     link = light.find_element(By.CSS_SELECTOR, 'link').get_attribute('href')
   except:
     print("произошла ошибка при парсинге")
     continue

   parsed_data.append([name, price, link])

driver.quit()

with open("lights.csv", 'w',newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название светильника', 'Цена', 'Ссылка на светильник'])
    writer.writerows(parsed_data)