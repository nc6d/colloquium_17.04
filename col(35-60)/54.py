"""54. Введіть масив з 20 елементів і визначте, чи є в ньому елементи з
однаковими значеннями."""

arr = [int(input(f'Enter {x + 1} element: ')) for x in range(20)]
print('Default array:', arr)

if len(arr) == len(set(arr)):
    print('Every element is unique')
else:
    print('There are identical elements')
