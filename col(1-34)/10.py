"""10. Дані про температуру повітря за декаду листопада зберігаються в масиві.
Визначити, скільки разів температура опускалася нижче -10 градусів."""
import random

arr = [random.randint(-20, 5) for x in range(10)]
print('°C, '.join(map(str, arr)), end='°C\n')
count = 0
for i in range(len(arr)):
    if arr[i] < -10:
        count += 1
print(f'{count} times November decade temperature values were below -10°C ')
