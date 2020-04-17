"""42. Підрахувати кількість елементів одновимірного масиву, для яких
виконується нерівність i * i < ai < i!"""
import numpy as np
import math

arr = [np.random.uniform(0, 5) for x in range(20)]
print('Default array:', arr)

# I used an math.gamma, not math.factorial because math.factorial cannot calculate float nums

filtered_arr = list(filter(lambda i: i ** 2 < i < math.gamma(i), arr))
print(filtered_arr)
