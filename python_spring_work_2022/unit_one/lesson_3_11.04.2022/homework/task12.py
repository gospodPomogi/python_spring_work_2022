measure = int(input('Введите еденицу массы тела: '))
weight = int(input('Введите массу тела: '))
if measure == 1:
    print(weight, 'кг')
elif measure == 2:
    print(weight / 1e+6, 'кг')
elif measure == 3:
    print(weight / 1000, 'кг')
elif measure == 4:
    print(weight * 1000, 'кг')
elif measure == 5:
    print(weight * 100, 'кг')