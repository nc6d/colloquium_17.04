"""49. Задано дві таблиці. Одна містить найменування послуг, а інша - розцінки
за ці послуги. Видаліть з обох таблиць все, що передує послузі, ціна якої G гривень."""

data = {'washing': 15, 'drying': 5, 'cleaning': 8, 'disinfecting': 16, 'polishing': 9, 'full cleaning': 25}
data2 = list(data.items())
data3 = []
g = int(input('Enter G value: '))

print('Default list:')
for i in range(len(data2)):
    data2[i] = list(data2[i])
    print(data2[i])

# Making a slice of created list, deleting all previous values

print('New list: ')
for j in range(len(data2)):
    if data2[j][1] == g:
        slice_obj = slice(j, len(data2))
        for x in range(len(data2[slice_obj])):
            print(data2[slice_obj][x])


