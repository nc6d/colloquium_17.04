"""26. Напишіть програму аналізу значень температури хворого за добу:
визначте мінімальне і максимальне значення, середнє арифметичне. Заміри
температури виробляються шість раз на добу і результати вводяться з клавіатури у
масив T."""
arr = [float(input(f'Enter {x + 1} element: ')) for x in range(6)]
print('Measures:\n', '°C, '.join(map(str, arr)), end='°C\n')
print('Minimal value: ', min(arr), '\nMaximal value', max(arr), '\nAverage value: ', sum(arr) / len(arr))
