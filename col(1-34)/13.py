"""13. Створіть масив з 15 цілочисельних елементів і визначте серед них
мінімальне значення."""
import random

arr = [random.randint(-10, 10) for x in range(15)]
print('Array:\n', arr, '\nMinimal value:\n', min(arr))
