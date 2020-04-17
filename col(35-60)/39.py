"""39. Дані про температуру повітря і кількості опадів за декаду квітня
зберігаються в масивах. Визначити кількість опадів, що випали у вигляді дощу і у
вигляді снігу за цю декаду."""

# Main data

data = {'temp': [4, -3, 0, -2, 10, 13, 18, 9, -1, 5],
        'drops': [13, 12, 3, 4, 6, 2, 6, 9, 11, 8]
        }

# Get an dict keys and zip them to general list

temp_data = data.get('temp')
drops_data = data.get('drops')
split_data = list(zip(temp_data, drops_data))

rain_volume = []
snow_volume = []

# Sort data:
# If the temperature will below zero, it will be snowy
# In other cases it will be rainy

for i in range(len(split_data)):
    split_data[i] = list(split_data[i])
    if split_data[i][0] <= 0:
        snow_volume.append(split_data[i][1])
    else:
        rain_volume.append(split_data[i][1])

print('Snow volume:', sum(snow_volume))
print('Raindrops volume:', sum(rain_volume))
