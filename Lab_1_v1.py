#Вариант 1 (бессмертные кролики)
n, k = map(int, input("Введите два натуральных числа (n ≤40 и k ≤5): ").split())


if n == 1 or n == 2:
    print(f"Количество пар кроликов на {n}-й месяц: 1")
else:
    pre_previous = 1  # Все кролики два месяца назад
    previous = 1  # Все кролики месяц назад
    current = 0  # текущее количество кроликов



for month in range(3,  n + 1 ):
    current = previous + k * pre_previous
    pre_previous = previous
    previous = current

print(f"Количество пар кроликов на {n}-й месяц: {current}")