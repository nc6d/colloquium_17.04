"""46. Задана таблиця назв товарів, що випускаються заводом. Визначте, чи
повторюється в цій таблиці назва першого товару, і, якщо повторюється, видаліть
назву першого товару з таблиці."""

goods_names = ['knife', 'fork', 'plate', 'table', 'chair', 'knife']
print('Goods list:')
for name in goods_names:
    print('‣', name)
if goods_names.count(goods_names[0]) > 1:
    duplicate = goods_names[0]
    while duplicate in goods_names:
        goods_names.remove(duplicate)
print('Filtered list:')
for name in goods_names:
    print('‣', name)

