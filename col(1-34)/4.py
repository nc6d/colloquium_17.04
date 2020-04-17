"""4. Створіть масив з п'яти прізвищ і виведіть на екран ті з них, які
починаються з певної букви, яка вводиться з клавіатури."""
sur_arr = []
letter_query = input('Input the 1st letter of surname: ').upper()
for i in range(5):
    sur_arr.append(input(f'Enter {i + 1} surname: ').title())
print(f'Filtered surnames which starting with "{letter_query}" letter:')
for x in sur_arr:
    if x.startswith(letter_query):
        print(x)


