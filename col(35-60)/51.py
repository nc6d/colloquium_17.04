"""51. Дан одновимірний масив а. Сформувати новий масив, який складається
тільки з тих елементів масиву а, які перевищують свій номер на 10. Якщо таких
елементів немає, то видати повідомлення."""
import random

arr = [random.randint(0, 15) for x in range(10)]
print('Default array:\n', arr)
filtered_arr = []
for x in range(len(arr)):
    if arr[x] > x + 10:
        filtered_arr.append(arr[x])
if not filtered_arr:
    print('Elements not found')
else:
    print('Filtered array:\n', filtered_arr)
