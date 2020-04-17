"""55. У будинку, що складається з 30 квартир, переселити мешканців так, щоб
мешканці першої квартири переїхали в тридцяту, з тридцятого - в першу, з другої - в 29
і т.д., знайдіть кількість квартир, в яких проживає більше 5 осіб."""
import random

dwellers = [random.randint(1, 7) for x in range(10)]
print('Default dwellers array:\n', dwellers)

for i in range(10):
    print(f'Dwellers in flat no.{i + 1}:', dwellers[i])

migrated = list(reversed(dwellers))
print('Removed dwellers array:\n', migrated)

for i in range(10):
    print(f'Replaced dwellers in flat no.{i + 1}:', migrated[i])
count = 0
for j in range(len(migrated)):
    if migrated[j] >= 5:
        count += 1
print('There are flats with more that 5 dwellers:', count)
