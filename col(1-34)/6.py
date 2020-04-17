"""6. Створіть масив А [1..8] за допомогою генератора випадкових чисел з
елементами від -10 до 10 і виведіть його на екран. Підрахуйте кількість від’ємних
елементів масиву."""
import random
arr = [random.randint(-10, 10) for x in range(1, 9)]
print('Default array:\n', arr)
count = 0
for i in arr:
    if i < 0:
        count += 1
print(f'There are {count} negative elements')
