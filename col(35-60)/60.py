"""60. Дан одновимірний масив з 10 цілих чисел. Підрахуйте найбільше число
однакових чисел, що йдуть підряд в ньому."""

n = int(input("Enter array length: "))
a2 = int(input("Enter number: "))

check1 = 0
check2 = 0
for i in range(2, n + 1):
    a = int(input("Enter number: "))
    if a == a2:
        check1 += 1
    elif a != a2:
        amount = 0
        check1 = 0
    if check1 > check2:
        check2 = check1
    a2 = a

if check2 > 0:
    print(f'There are {check2 + 1} identical numbers')
else:
    print('Every number is unique')
