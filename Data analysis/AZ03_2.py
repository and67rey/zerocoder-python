# Построение диаграммы рассеяния для двух наборов случайных данных,
# сгенерированных с помощью функции `numpy.random.rand`

import numpy as np
import matplotlib.pyplot as plt
import random

n = 500
random_array_X = np.random.rand(n) # Набор случайных чисел для X
random_array_Y = np.random.rand(n) # Набор случайных чисел для Y
print(f'Массив случайных чисел для X {random_array_X}')
print(f'Массив случайных чисел для Y {random_array_Y}')

# Цвета для каждой точки выбираются случайным образом
colors = [random.randint(1, 100) for n in range(len(random_array_X))]

# Основные параметры диаграммы рассеяния
plt.scatter(random_array_X, random_array_Y, c = colors, alpha = 0.7, cmap='plasma')
# Добавление заголовка и меток осей
plt.xlabel("ось Х")
plt.ylabel("ось Y")
plt.title("Диаграмма рассеяния")
# plt.legend()
plt.grid(True)
# Вывод диаграммы рассеяния
plt.show()
