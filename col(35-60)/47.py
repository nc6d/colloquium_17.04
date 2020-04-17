"""47. У лінійному масиві знайти максимальний елемент. Вставте порядковий
номер елемента за ним, пересунувши всі залишилися на одну позицію вправо."""
import numpy as np
arr = [np.random.randint(0, 10) for x in range(10)]
print('Array:\n', arr)
maximal = 0
arr2 = []
c = 0
for i in range(len(arr)):
    if arr[i] > maximal:
        maximal = arr[i]
        c = i
print(f'Largest element - {maximal}[{c}]')
arr.insert(c + 1, c)
print('Updated array:\n', arr)
