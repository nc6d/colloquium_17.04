"""30. Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які розташовані за першим по порядку мінімальним елементом."""
import numpy as np

arr = [np.random.randint(-10, 10) for x in range(10)]
print('Default array:\n', arr)
index = 0
new_arr = []
minimal = max(arr)
for i in range(len(arr)):
    if arr[i] < minimal:
        minimal = arr[i]
        index = i
for j in range(len(arr)):
    if j > index:
        new_arr.append(arr[j])

print("New array:\n", new_arr,
      f"\nFirst minimal element: {minimal}[{index}]",
      "\nAverage value of new array:", sum(new_arr) / len(new_arr))
