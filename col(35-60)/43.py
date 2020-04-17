"""43. Задано два натуральних числа a і b. Змінній w привласнити значення
істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а
і не кратний b."""
import numpy as np
arr = [np.random.randint(0, 10) for x in range(10)]
print('Array:\n', arr)
w = False
a, b = int(input('Enter A: ')), int(input('Enter B: '))
for i in range(len(arr)):
    if (arr[i] % a == 0) and (arr[i] % b != 0):
        w = True
print('w =', w)
