"""3. Створіть масив з п'яти прізвищ і виведіть їх на екран стовпчиком,
починаючи з останнього."""

sur_arr = []
for i in range(5):
    sur_arr.append(input(f'Enter {i + 1} surname: '))
rev_sur_arr = reversed(sur_arr)
for x in rev_sur_arr:
    print(x)
