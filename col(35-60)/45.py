"""45. Перетин даху має форму півкола з радіусом R м. Сформувати таблицю,
яка містить довжини опор, які встановлюються через кожні R / 5 м."""
from math import sqrt

radius = int(input('radius: '))
delta = radius / 5
x = 0
i = 0

while x < 2 * radius - delta:
    x = x + delta
    i += 1
    h = sqrt(x * (2 * radius - x))
    print(f'Height of {i} prop:', h)

