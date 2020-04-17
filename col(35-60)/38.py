"""38. Дані про направлення вітру (північний, південний, східний, західний) і
силі вітру за декаду листопада зберігаються в масиві. Визначити, скільки днів дув
південний вітер з силою, що перевищує 8 м/с."""
data = {'North': [4, 3, 0, 6, 10, 13, 18, 9, 7, 12],
        'South': [13, 12, 3, 4, 6, 2, 6, 9, 11, 8],
        'East': [2, 3, 2, 4, 1, 5, 6, 2, 9],
        'West': [5, 2, 3, 9, 6, 5, 4, 2, 10, 14]
        }
south_data = data.get('South')
print("South wind speed data:\n", 'm/s, '.join(map(str, south_data)), end='m/s\n')
filtered_south_data = list(filter(lambda x: x > 8, south_data))
print(f"Rapid south wind was spotted {len(filtered_south_data)} times")
