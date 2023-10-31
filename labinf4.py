# 4.	Реализовать модуль, содержащий функцию нахождения в массиве вещественных чисел числа
# с наименьшей дробной частью (дробная часть всегда положительна
def minfraction(*arg):
    fl = []
    print(arg)
    min = 10 ** 20
    key = 0
    for i in range(len(arg)):
        if type(arg[i]) == float:
            fl.append(arg[i])
    for j in range(len(fl)):
        fl[j] = format(fl[j], '.10f')
        fraction = str(fl[j]).split('.')
        for c in range(len(fraction[1])):
            if fraction[1][c] == '0':
                key = key + 1
            else:
                break
        if int(fraction[1]) < min:
            min = int(fraction[1])
            while int(fraction[1]) % 10 == 0:
                fraction[1] = int(fraction[1]) // 10
            otvet = fraction[0] + '.' + '0' * key + str(fraction[1])
            key = 0
    return otvet


print(minfraction(42.00005, 33.0008, -29.007))
