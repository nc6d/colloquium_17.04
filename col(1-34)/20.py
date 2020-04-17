"""20. Знайти суму всіх елементів масиву дійсних чисел, більших за задане
число. Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами
від 50 до 100."""
import random

arr = [random.randint(50, 100) for x in range(20)]
print('Array:\n', arr)
query = int(input('Enter query number: '))
new_arr = list(filter(lambda x: x > query, arr))
print('Filtered numbers sum:\n', sum(new_arr))
