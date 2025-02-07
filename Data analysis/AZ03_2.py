# Построение диаграммы рассеяния для двух наборов случайных данных,
# сгенерированных с помощью функции `numpy.random.rand`

import numpy as np
import matplotlib.pyplot as plt

n = 100
random_array_X = np.random.rand(n) # Набор случайных чисел для X
random_array_Y = np.random.rand(n) # Набор случайных чисел для Y
print(f'Массив случайных чисел для X {random_array_X}')
print(f'Массив случайных чисел для Y {random_array_Y}')

# Построение диаграммы рассеяния
plt.scatter(random_array_X, random_array_Y)
# Добавление заголовка и меток осей
plt.xlabel("ось Х")
plt.ylabel("ось Y")
plt.title("Диаграмма рассеяния")
# Показать диаграмму рассеяния
plt.show()
