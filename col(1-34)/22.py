"""22. Знайти добуток елементів масиву, кратних 3 і 9. Розмірність масиву - 10.
Заповнення масиву здійснити випадковими числами від 5 до 500."""
import numpy as np

arr = [np.random.randint(5, 500) for x in range(10)]
print('Array:\n', arr)
new_arr = filter(lambda x: x % 3 == 0 and x % 9 == 0, arr)
print('Filtered numbers multiplication:\n', np.prod(list(new_arr)))
