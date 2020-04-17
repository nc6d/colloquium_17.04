"""
1. Введіть з клавіатури в масив п'ять цілочисельних значень. Виведіть їх в
один рядок через кому. Отримайте для масиву середнє арифметичне.
"""
a = []
for i in range(5):
    a.append(int(input(f'Enter {i + 1} element: ')))
print(', '.join(map(str, a)))
print('Average value is', sum(a)/len(a))
