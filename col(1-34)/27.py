"""27. Лінійний масив містить відомості про кількість опадів, що випали за
кожен з 12 місяців одного року. Складіть програму, що визначає загальну кількість
опадів протягом цього року, середньомісячну кількість опадів, кількість посушливих
місяців (коли кількість опадів було менше 30 мм), найпосушливіший місяць року."""

arr = [int(input(f'Enter {x + 1} month value: '))for x in range(12)]
print('Values:\n', ' mm Hg, '.join(map(str, arr)), end='mm Hg\n')
dry_month = filter(lambda x: x < 30, arr)
print('Precipitation by year: ', sum(arr), '\nAverage month value: ', sum(arr) / len(arr), '\nDry months:', len(list(dry_month)))
