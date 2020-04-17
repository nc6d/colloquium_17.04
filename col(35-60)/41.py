"""41. Змінній t привласнити значення істина, якщо максимальний елемент
одновимірного масиву єдиний і не перевищує наперед заданого числа а."""
import numpy as np

arr = [np.random.randint(5) for x in range(10)]
print('Default array:\n', arr)
max_value = max(arr)
print('Max value:', max_value)
t = False
query = int(input('Enter the limit-number: '))
count = 0
for i in range(len(arr)):
    if max_value == arr[i]:
        count += 1
if max_value < query and count == 1:
    t = True
print(t)
