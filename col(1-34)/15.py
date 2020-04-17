"""15. Знайти суму парних елементів масиву цілих чисел. Розмірність масиву -
20. Заповнення масиву здійснити випадковими числами від 100 до 200."""
import random

arr = [random.randint(100, 200) for x in range(20)]
print('Array:\n', arr)
even_arr = filter(lambda x: x % 2 == 0, arr)
print('Even numbers sum:\n', sum(even_arr))


