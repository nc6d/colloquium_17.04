"""28. Знайти кількість парних елементів одновимірного масиву."""
import numpy as np

arr = [np.random.randint(-10, 10) for x in range(10)]
print('Array:\n', arr)
new_arr = filter(lambda x: x % 2 == 0, arr)
print('There are', len(list(new_arr)), 'even elements')
