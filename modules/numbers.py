def numbersFunction():
    testArray = list(map(int, input('Введите несколько натуральных чисел через пробел:').split()))
    newArray = []

    for i in testArray:
        if i %3 == 0:
            newArray.append(i)

    if len(newArray) == 0:
        print('** Нет чисел, кратных трем **')
    else:
        print('** Числа, кратные трем: ', newArray)