"""52. Знайти найбільший елемент з елементів одновимірного масиву, що мають
парний номер. Визначити, чи є він єдиним."""
import numpy as np

arr = [np.random.randint(5) for x in range(10)]
print('Default array:\n', arr)
max_value = max(arr)
print('Max value:', max_value)
t = False
count = 0
arr2 = []
for x in range(0, len(arr), 2):
    arr2.append(arr[x])
print('Array with even index numbers:\n', arr2)
for i in range(len(arr2)):
    if max_value == arr2[i]:
        count += 1
if count == 1:
    print('Max value is a sole number')
else:
    print('Max value is not a sole number')



