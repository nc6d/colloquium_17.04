"""5. Створіть масив А [1..7] за допомогою генератора випадкових чисел і
виведіть його на екран. Збільште всі його елементи в 2 рази."""
import random
arr = [random.randint(-10, 10) for x in range(1, 8)]
print('Default array:\n', arr)
print('Doubled array:\n', [i*2 for i in arr])
