"""57. Відомість на зарплату представлена як дві таблиці. Одна містить
прізвища працівників цеху, а друга - їх зарплату за поточний місяць. Знайдіть прізвище
працівника, зарплата якого найменш відхиляється від середньої зарплати всіх
працівників за поточний місяць. Знайдіть прізвища двох працівників з найбільшою
заробітною платою. Видаліть з відомості на зарплату відомості про працівника,
зарплата якого мінімальна."""

# Enter data and appending lists with entered data

N = int(input('Enter number of workers: '))
salaries_arr = []
surnames_arr = []
for i in range(N):
    print('Worker', i + 1)
    surnames = input(f'Enter surname of worker {i + 1}: ', )
    salary = int(input(f'Salary of worker {i + 1}: '))
    salaries_arr.append(salary)
    surnames_arr.append(surnames)

# Zip salaries with surnames and printing an info list

info_arr = list(zip(surnames_arr, salaries_arr))
print('Default list of workers:')
for x in range(N):
    print(info_arr[x])

# Average salary

average_salary = sum(salaries_arr) / N
print('Average salary:', average_salary)

# Determine the closest salary value to average.

difference_salary = []
for i in range(N):
    difference_salary.append(abs(salaries_arr[i] - average_salary))
minimal = max(difference_salary)
pos = 0
for j in range(N):
    if difference_salary[j] < minimal:
        minimal = difference_salary[j]
        pos = j
print("Minimal salary deviation has worker: ", surnames_arr[pos])

# Determine two workers with largest salaries

sorted_salary = sorted(info_arr, key=lambda a: a[1], reverse=True)
largest_salary_worker1 = sorted_salary[0]
largest_salary_worker2 = sorted_salary[1]
print(f'The largest salaries have {largest_salary_worker1} and {largest_salary_worker2}')

# Determine worker with least salary

least_salary_worker_index = 0
least_salary = salaries_arr[0]
for i in range(1, len(salaries_arr)):
    current_worker_salary = salaries_arr[i]
    if current_worker_salary < least_salary:
        least_salary = current_worker_salary
        least_salary_worker_index = i
print('Worker with the least salary:', surnames_arr[least_salary_worker_index])

# Remove information of employee with least salary

salaries_arr.pop(least_salary_worker_index)
surnames_arr.pop(least_salary_worker_index)
info_arr2 = list(zip(surnames_arr, salaries_arr))
print('New list without worst worker:')
for i in range(len(surnames_arr)):
    print(info_arr2[i])
