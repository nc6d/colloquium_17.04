"""34. Дано два лінійних масиву однакової розмірності. Скласти третій масив з
добутку елементів перших двох масивів, що стоять на місцях з однаковим індексом."""
import numpy as np

arr1 = [np.random.randint(-5, 5) for i in range(10)]
print('First array:\n', arr1)
arr2 = [np.random.randint(-5, 5) for j in range(10)]
print('Second array:\n', arr2)
print('Arrays multiplication:\n', np.multiply(arr1, arr2))
