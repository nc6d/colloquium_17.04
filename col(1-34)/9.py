"""З 8 до 20 години температура повітря вимірювалася щогодини. Відомо,
що протягом цього часу температура знижувалася. Визначте, о котрій годині було
вперше зафіксовано від'ємну температуру."""
import random

arr = [random.randint(-0, 16) for x in range(8, 21)]
print('°C, '.join(map(str, arr)), end='°C\n')
minimal = max(arr)
c = 0
for i in range(len(arr)):
    if arr[i] < minimal:
        minimal = arr[i]
        c = i
print(f'Lowest temperature {minimal}°C was firstly spotted at {c + 8} hours')
