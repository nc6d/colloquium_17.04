"""Знайти добуток елементів масиву цілих чисел, які кратні 7. Розмірність
масиву - 15. Заповнення масиву здійснити випадковими числами від 10 до 50."""
import random
import numpy as np
arr = [random.randint(10, 50) for x in range(15)]
print('Array:\n', arr)
new_arr = list(filter(lambda x: x % 7 == 0, arr))
print('Filtered array:\n', new_arr)

print('Multiplication of filtered array:\n', np.prod(new_arr))
