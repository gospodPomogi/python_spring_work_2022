while True:
    coefficient_a, coefficient_b = int(input('input coefficient A: ')), int(input('input coefficient B: '))
    if coefficient_a == 0:
        print('coefficient a cannot be equal to 0')
    else:
        x = coefficient_b / coefficient_a
        decision = coefficient_a * x - coefficient_b
        print(decision)
