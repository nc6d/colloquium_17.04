"""36. Знайти суму додатніх елементів лінійного масиву цілих чисел.
Розмірність масиву - 10. Заповнення масиву здійснити з клавіатури."""

arr = [int(input(f'Enter {x + 1} element: ')) for x in range(5)]
print('Default array:\n', arr)
filtered_arr = list(filter(lambda x: x > 0, arr))
print("Sum of positive numbers:", sum(filtered_arr))
