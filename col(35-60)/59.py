"""59. Дан одновимірний масив з 10 цілих чисел. Підрахуйте кількість різних
чисел в ньому."""
import random
arr = [random.randint(0, 10) for x in range(10)]
print(arr)
print(dict((x, arr.count(x)) for x in set(arr)))
