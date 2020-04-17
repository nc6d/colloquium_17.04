"""29. Знайти кількість парних елементів одновимірного масиву до першого
зустрінутого числа рівного наперед заданому числу а."""
import numpy as np

arr = [np.random.randint(-10, 10) for x in range(10)]
print('Default array:\n', arr)
filter_arr = list(filter(lambda x: x % 2 == 0, arr))
print('Filtered array:\n', filter_arr)
a = int(input('Enter the stop-number: '))
stop_arr = []
for i in range(len(filter_arr)):    
    if filter_arr[i] != a:
        stop_arr.append(filter_arr[i])
    else:
        break
print('Array with stop-number:\n', stop_arr, f'\nIt has {len(stop_arr)} even numbers')
