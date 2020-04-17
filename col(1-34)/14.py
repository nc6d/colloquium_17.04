"""14. Сформуйте лінійний масив дійсних чисел, елементи якого є відстанями,
пройденими тілом при вільному падінні на землю за 1, 2, ..., 10 с."""
h_arr = []
for t in range(10):
    h = (9.8 * t**2) / 2
    h_arr.append(h)
for i in range(len(h_arr)):
    print(f'Distance passed after {i + 1} seconds:', h_arr[i], 'meters')
