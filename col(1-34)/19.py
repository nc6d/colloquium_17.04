"""19. Знайти суму всіх елементів масиву цілих чисел що задовольняють умові:
остача від ділення на 2 дорівнює 3. Розмірність масиву - 20. Заповнення масиву
здійснити випадковими числами від 200 до 300."""
import random

arr = [random.randint(200, 300) for x in range(20)]
print('Array:\n', arr)
new_arr = list(filter(lambda x: x % 2 == 3, arr))
print('Filtered numbers sum:\n', sum(new_arr))
