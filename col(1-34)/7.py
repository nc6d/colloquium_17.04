"""7. Створіть масив А [1..12] за допомогою генератора випадкових чисел з
елементами від -20 до 10 і виведіть його на екран. Замініть всі від’ємні елементи
масиву числом 0."""
import random
arr = [random.randint(-20, 10) for x in range(12)]
print('Default array:\n', arr)
for i in range(len(arr)):
    if arr[i] < 0:
        arr[i] = 0
print('Zeroed array:\n', arr)

