"""25. Знайти добуток елементів лінійного масиву цілих чисел, які кратні 5.
Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами від 10 до
100."""
import numpy as np

arr = [np.random.randint(10, 100) for x in range(10)]
print('Array:\n', arr)
new_arr = filter(lambda x: x % 5 == 0, arr)
print('Filtered numbers multiplication:\n', np.prod(list(new_arr)))
