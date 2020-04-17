"""18. Знайти добуток всіх елементів масиву цілих чисел, менших 0. Розмірність
масиву - 10. Заповнення масиву здійснити за допомогою клавіатури."""
import numpy as np
arr = [int(input(f'Enter {x + 1} element: '))for x in range(10)]
print('Array:\n', arr)
filtered_arr = []
for i in range(len(arr)):
    if arr[i] < 0:
        filtered_arr.append(arr[i])
print('Filtered array:\n ', filtered_arr)
print('Multiplication of filtered array:', np.prod(filtered_arr))
