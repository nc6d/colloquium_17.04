"""30. Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які розташовані за першим по порядку мінімальним елементом."""
import numpy as np

arr = [np.random.randint(-10, 10) for x in range(10)]
print('Default array:\n', arr)

new_arr = []
for i in range(len(arr)):
    if i != 0:
        new_arr.append(arr[i])
print("First index element:", arr[0], '\nArray without 1st element:\n', new_arr, "\nNew array's average value is", sum(new_arr)/len(arr))
