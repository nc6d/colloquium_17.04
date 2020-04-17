"""37. Розсортуйте заданий лінійний масив по зростанню."""

import random
arr = [random.randint(0, 10) for x in range(5)]
print('Default array:\n', arr)
print("Sorted array:\n", list(sorted(arr)))
