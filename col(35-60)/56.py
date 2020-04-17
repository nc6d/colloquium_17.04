"""56. Якщо в одновимірному масиві є три поспіль однакових елемента, то
змінній r привласнити значення істина."""
import random

arr = [random.randint(0, 5) for x in range(20)]
print("Array:\n", arr)

r = False
for i in range(len(arr) - 2):
    if (arr[i] == arr[i + 1]) and (arr[i + 1] == arr[i + 2]):
        r = True
        break

print('r value:', r)
