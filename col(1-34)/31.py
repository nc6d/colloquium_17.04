"""31. Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які потрапляють в інтервал від -2 до 10."""
import numpy as np

arr = [np.random.randint(-10, 10) for x in range(10)]
print('Default array:\n', arr)
filter_arr = list(filter(lambda x: x in range(-2, 10), arr))
print('Numbers in range:\n', filter_arr, '\nAverage value is', sum(filter_arr) / len(filter_arr))
