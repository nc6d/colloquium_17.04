"""2. Введіть з клавіатури п'ять цілочисельних елементів масиву X. Виведіть на
екран значення коренів і квадратів кожного з елементів масиву."""

x = []
for i in range(5):
    x.append(int(input(f'Enter {i + 1} element: ')))
print('Squares: \n', [i ** 2 for i in x], '\nRoots: \n', [i ** 0.5 for i in x])
