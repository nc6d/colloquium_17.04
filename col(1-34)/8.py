"""8. Створіть цілочисельний масив А [1..15] за допомогою генератора
випадкових чисел з елементами від -15 до 30 і виведіть його на екран. Визначте
найбільший елемент масиву і його індекс."""
import random

arr = [random.randint(-15, 30) for x in range(15)]
print('Array:\n', arr)
maximal = 0
c = 0
for i in range(len(arr)):
    if arr[i] > maximal:
        maximal = arr[i]
        c = i
print(f'Largest element - {maximal}[{c}]')
