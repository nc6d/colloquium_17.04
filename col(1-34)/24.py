"""24. Знайти суму елементів масиву цілих чисел, які діляться на 5 і на 8
одночасно. Розмірність масиву - 30. Заповнення масиву здійснити випадковими
числами від 500 до 1000."""
import numpy as np

arr = [np.random.randint(500, 1000) for x in range(30)]
print('Array:\n', arr)
new_arr = filter(lambda x: x % 5 == 0 and x % 8 == 0, arr)
print('Filtered numbers sum:\n', sum(list(new_arr)))
