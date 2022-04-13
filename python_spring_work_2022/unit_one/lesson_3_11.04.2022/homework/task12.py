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
# к сожалению задание было сделано без конструкции match, так как такая конструкция
# отсутствует в моем pycharm. весь вечер убил в попытки ее поставить
# но ловил странные ошибки. Задание будет сделанно согласно требованиям
# когда будет побежден pycharm и match