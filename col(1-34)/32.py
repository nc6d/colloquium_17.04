"""32. Змінній t привласнити значення істина, якщо в одновимірному масиві є
хоча б одне від’ємне і парне число."""
import numpy as np
arr = [np.random.randint(-10, 10) for x in range(5)]
print('Default array:\n', arr)
t = False
for i in range(len(arr)):
    if arr[i] < 0 and arr[i] % 2 == 0:
        t = True
print('t =', t)
