"""44. Підрахуйте кількість елементів одновимірного масиву, які збігаються зі
своїм номером і при цьому кратні 3."""
import numpy as np
arr = [np.random.randint(0, 10) for x in range(10)]
print('Array:\n', arr)
filtered = []
for i in range(len(arr)):
    if i == arr[i] and arr[i] % 3 == 0:
        filtered.append(arr[i])
print('Sum of filtered numbers:', sum(filtered))
