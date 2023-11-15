# 4.	Реализовать модуль, содержащий функцию нахождения в массиве вещественных чисел числа
# с наименьшей дробной частью (дробная часть всегда положительна
# Сложность программы зависит от кол-ва вводимых элементов O(n)
def minfraction(arg):
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
def maxfraction(arg):
    fl = []
    max = 0
    for i in range(len(arg)):
        if type(arg[i]) == float:
            fl.append(arg[i])
    for j in range(len(fl)):
        fl[j] = [fl[j], fl[j] % 1]
    for x in range(len(fl)):
        if fl[x][1] > max:
            max = fl[x][1]
            otvet = fl[x][0]
    return otvet
while True:
    try:
        inpuu = str(input('Choose the operation min/max: '))
        if inpuu == 'max' or inpuu == 'min':
            break
        else:
            print("Invalid syntax: type 'min' or 'max'")
    except ValueError:
        print("Invalid syntax: type 'min' or 'max'")
a = []
if inpuu == 'max':
    while True:
        try:
            inp = input('Enter your number (type "end" to stop): ')
            if type(inp) != str or float(inp):
                a.append(float(inp))
            elif inp == '0' or inp == '0.0':
                a.append(0.0)
            else:
                print("Invalid syntax: input a number")
        except ValueError:
            if inp == "end":
                break
            print("Invalid syntax: input a number")
    if len(a) > 1 and maxfraction(a):
        print('From', a)
        print('Find', inpuu)
        print('Result:', maxfraction(a))
    else:
        print('Result: None')
else:
    while True:
        try:
            inp = input('Enter your number (type "end" to stop): ')
            if type(inp) != str or float(inp):
                a.append(float(inp))
            elif inp == '0' or inp == '0.0':
                a.append(0.0)
            else:
                print("Invalid syntax: input a number")
        except ValueError:
            if inp == "end":
                break
            print("Invalid syntax: input a number")
    if len(a) > 1 and minfraction(a):
        print('From', a)
        print('Find', inpuu)
        print('Result:', minfraction(a))
    else:
        print('Result: None')