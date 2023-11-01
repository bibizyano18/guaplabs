# 4.	Реализовать модуль, содержащий функцию нахождения в массиве вещественных чисел числа
# с наименьшей дробной частью (дробная часть всегда положительна
# Сложность программы зависит от кол-ва вводимых элементов O(n)
def minfraction(*arg):
    print(arg)
    fl = []
    min = 10 ** 20
    for i in range(len(arg)):
        if type(arg[i]) == float:
            fl.append(arg[i])
    for j in range(len(fl)):
        fl[j] = [fl[j], fl[j] % 1]
    for x in range(len(fl)):
        if fl[x][1] < min:
            min = fl[x][1]
            otvet = fl[x][0]
    return otvet

print(minfraction(-42.005, 33.8, 29.007))
