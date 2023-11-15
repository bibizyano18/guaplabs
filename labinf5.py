# Дана прямоугольная матрица.
# Найти строку с наибольшей и строку с наименьшей суммой элементов.
# Вывести на печать найденные строки и суммы их элементов.

while True:
    try:
        kw = int(input("Enter width: "))
        if kw > 0:
            break
        else:
            print("Invalid syntax: input an integer number")
    except ValueError:
        print("Invalid syntax: input an integer number")
while True:
    try:
        kh = int(input("Enter height: "))
        if kh > 0:
            break
        else:
            print("Invalid syntax: input an integer number")
    except ValueError:
        print("Invalid syntax: input an integer number")
s = [0]*kh
for i in range(len(s)):
    s[i] = [0]*kw
for j in s:
    for i in range(len(j)):
        while True:
            try:
                print('Input a number', i + 1, ':')
                inp = input()
                if inp == '0':
                    break
                if type(inp) != str or int(inp):
                    j[i] = int(inp)
                    break
                else:
                    print("Invalid syntax: input a number")
            except ValueError:
                print("Invalid syntax: input a number")
        for i in range(len(s)):
            print(s[i])
print('Result:')
for i in range(len(s)):
    print(s[i])
# 1
maxi = -10 ** 21
mini = 10 ** 20
for j in s:
    if sum(j) < mini:
        mini = sum(j)
        resmin = j
    if sum(j) > maxi:
        maxi = sum(j)
        resmax = j
print('Answer for task №1:')
print('Minimal:', resmin, 'sum:', mini)
print('Maximum:', resmax, 'sum:', maxi)
# 2
while True:
    try:
        ordd = int(input("Enter order of matrix: "))
        if ordd > 0:
            break
        else:
            print("Invalid syntax: input an integer number")
    except ValueError:
        print("Invalid syntax: input an integer number")
s2 = [0]*ordd
for i in range(len(s2)):
    s2[i] = [0]*ordd
if len(s2) > 1:
    for j in s2:
        for i in range(len(j)):
            while True:
                try:
                    print('Input a number', i + 1, ':')
                    inp = input()
                    if inp == '0':
                        break
                    if type(inp) != str or int(inp):
                        j[i] = int(inp)
                        break
                    else:
                        print("Invalid syntax: input a number")
                except ValueError:
                    print("Invalid syntax: input a number")
            for i in range(len(s2)):
                print(s2[i])
else:
    while True:
        try:
            print('Input a number', i + 1, ':')
            inp = input()
            if inp == '0':
                break
            if type(inp) != str or int(inp):
                s2[0] = [int(inp)]
                break
            else:
                print("Invalid syntax: input a number")
        except ValueError:
            print("Invalid syntax: input a number")
print('Result:')
for i in range(len(s2)):
    print(s2[i])
for j in s2:
    for i in range(len(j)):
        if j[i] <= 0:
            j[i] = 0
        else:
            j[i] = 1

bt = []
for i in range(kw):
    x = []
    for j in range(kw):
        if i == j:
            x.append(s2[i][j])
        elif i < j:
            x.append(s2[i][j])
        else:
            x.append(0)
    bt.append(x)
print('Answer for task №2:')
print('Matrix:')
for i in range(len(s2)):
    print(s2[i])
print('Bottom matrix:')
for i in range(len(bt)):
    print(bt[i])
