import numpy as np
import matplotlib.pyplot as plt

# Построение гистограммы для случайных данных, сгенерированных с помощью функции `numpy.random.normal`
mean = 0 # Среднее значение
std_dev = 1 # Стандартное отклонение
num_samples = 1000 # Количество образцов
data = np.random.normal(mean, std_dev, num_samples)

# Основные параметры гистограммы
plt.hist(data, bins=100, edgecolor='black')
# Добавление заголовка и меток осей
plt.title('Гистограмма для случайных чисел')
plt.xlabel('Значение')
plt.ylabel('Частота')
# Вывод гистограммы
plt.show()



