"""35. Дан лінійний масив цілих чисел. Перевірте, чи є він упорядкованим по
спаданню."""

# Creating an array

arr = [int(input(f'Enter {x + 1} element: ')) for x in range(5)]
print(arr)

# Make a bool-list

check = False
bool_arr = []
for i in range(len(arr) - 1):

    # If there is at least one non-ordered number, append an False value

    if arr[i] >= arr[i + 1]:
        check = True
        bool_arr.append(check)
    else:
        check = False
        bool_arr.append(check)

if False in bool_arr:
    print("Non-ordered")
else:
    print('Ordered')
