n, m = map(int, input("Введите два натуральных числа через пробел (n ≤100 и m ≤20): ").split())
def mortal_rabbits(n, m):
    ages = [0] * m 
    ages[0] = 1 
    for month in range(1, n):
        new_borns = sum(ages[1:])  # Все, кто старше 0 месяцев, производят потомство
        
        # Сдвигаем кроликов по возрасту (старение)
        # Кролики возраста m-1 умирают, поэтому  сдвигаем до m-1
        for i in range(m - 1, 0, -1):
            ages[i] = ages[i-1]
            
        ages[0] = new_borns # Записываем родившихся
        
    return sum(ages)

result = mortal_rabbits(n, m)
print(f"Выходные данные: {result}")