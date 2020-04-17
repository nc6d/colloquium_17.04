"""17. Знайти суму елементів масиву дійсних чисел, що мають непарні номери.
Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами від 100
до 200."""
import random

arr = [random.uniform(100, 200) for x in range(20)]
print('Default array:')
for _ in range(len(arr)):
    print(arr[_])
summa = 0
for i in range(len(arr)):
    if i % 2 != 0:
        arr[i] += summa
        summa = arr[i]
print('Sum of array with odd indices: ', summa)

