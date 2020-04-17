"""33. Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів."""
import numpy as np

arr = [np.random.randint(-3, 3) for x in range(10)]
print('Array:\n', arr)
NoZero_arr = filter(lambda x: x != 0, arr)
print('Non-zero numbers multiplication:\n', np.prod(list(NoZero_arr)))
