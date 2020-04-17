"""23. Знайти суму всіх елементів масиву цілих чисел, які менше середнього
арифметичного елементів масиву. Розмірність масиву - 20. Заповнення масиву
здійснити випадковими числами від 150 до 300."""
import numpy as np

arr = [np.random.randint(150, 300) for x in range(20)]
print('Array:\n', arr)
middle_value = sum(arr) / len(arr)
print("Middle value is", middle_value)
new_arr = filter(lambda x: x < middle_value, arr)
print('Filtered numbers multiplication:\n', sum(list(new_arr)))
