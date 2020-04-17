"""Дані про температуру води на Чорноморському узбережжі за декаду
вересня зберігаються в масиві. Визначити, скільки за цей час було днів, придатних для
купання."""
import random

arr = [random.randint(14, 24) for x in range(10)]
print('°C, '.join(map(str, arr)), end='°C\n')
count = 0
for i in range(len(arr)):
    if arr[i] >= 17:
        count += 1
print(f"{count} times water temperature was above 17°C and it was suitable for swimming")
