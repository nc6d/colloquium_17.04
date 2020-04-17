"""12. Дані про температуру повітря за декаду грудня зберігаються в масиві.
Визначити, скільки раз температура була вище середньої за цю декаду."""
import random

arr = [random.randint(-10, 5) for x in range(10)]
print('°C, '.join(map(str, arr)), end='°C\n')
count = 0
middle_temp = sum(arr) / len(arr)
for i in range(len(arr)):
    if arr[i] >= middle_temp:
        count += 1
print(f"{count} times December decade temperature values were above middle value ({middle_temp}°C)")

