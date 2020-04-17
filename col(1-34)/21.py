"""21. Знайти добуток всіх елементів масиву дійсних чисел, менших заданого
числа. Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами
від 50 до 100."""
import numpy as np

arr = [np.random.randint(50, 100) for x in range(20)]
print('Array:\n', arr)
query = int(input('Enter query number: '))
new_arr = filter(lambda x: x < query, arr)
print('Filtered numbers multiplication:\n', np.prod(list(new_arr)))
