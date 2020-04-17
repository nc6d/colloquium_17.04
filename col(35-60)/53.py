"""53. В масиві X (1: n) кожен елемент рівний 0, 1 або 5. Переставити елементи
масиву так, щоб спочатку розташовувалися всі нулі, потім все одиниці, а потім всі
п'ятірки. Додаткового масиву не заводити."""
import random
nums = (0, 1, 5)
arr = sorted([random.choice(nums) for i in range(int(input('Enter an array size: ')))])
print(arr)
