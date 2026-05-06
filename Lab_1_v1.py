#Вариант 1 (бессмертные кролики)
#Расчёт количества пар бессмертных кроликов


def immortal_rabbits(n, k):
    
    if n == 1 or n == 2:
        return 1
    
    pre_previous = 1  # n-2 месяц
    previous = 1      # n-1 месяц
    current = 0       # текущий месяц
    
    for month in range(3, n + 1):
        current = previous + k * pre_previous
        pre_previous = previous
        previous = current
        
    return current 

if __name__ == "__main__":
    n, k = map(int, input("Введите два натуральных числа (n ≤40 и k ≤5): ").split())
    result = immortal_rabbits(n, k)
    print(f"Количество пар кроликов на {n}-й месяц: {result}")