# todo:  Даны три переменные: X, Y, Z. Их значения числа.
# Из данных произвольных чисел выбрать наибольшее.

# Пример:
# X = 5
# Y = 10
# Z = 3
# Ответ: Наибольшее число 10.
#
# X = 10
# Y = 12
# Z = -7
# Ответ: Наибольшее число 12.

first_variable = int(input('X = '))
second_variable = int(input('Y = '))
third_varidable = int(input('Z = '))
if first_variable > second_variable and first_variable > third_varidable:
    print('Наибольшее число: ', first_variable)
elif second_variable > first_variable and second_variable > third_varidable:
    print('Наибольшее число: ', second_variable)
else:
    print('Наибольшее число: ', third_varidable)