"""58. Дан одновимірний масив цілих чисел. Знайдіть, скільки разів в ньому
повторюється найчастіше число."""
import random
from collections import Counter
arr = [random.randint(0, 10) for i in range(10)]
print('Array:\n', arr)
counter = list(Counter(arr).most_common(1))
a = list((counter[0]))
print(a)
