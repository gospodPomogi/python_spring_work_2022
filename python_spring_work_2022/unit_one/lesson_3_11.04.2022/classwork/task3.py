arbitary_string = str(input('Введите строку: '))
number = (len(arbitary_string))
if number % 2 == 0:
    print(arbitary_string[0:number // 2])
    print(arbitary_string[number // 2:number])
else:
    number += 1
    print(arbitary_string[0:number//2])
    print(arbitary_string[number//2:number])
