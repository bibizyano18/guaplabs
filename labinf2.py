while True:
    try:
        a = int(input("Enter number: "))
        break
    except ValueError:
        print("Invalid syntax: input an integral number")
b = ''
for i in range(-1000, abs(a)+1):
    for d in range(1, 100):
        if (i)**d == a:
            b = b + str(i) + ' '
# доп задание + 2 балла
while a > 1:
    if a % 3 == 0:
        a = a // 3
    else:
        print(b, False)
        break
# доп -
else:
    if a < 1:
        print(b, False)
    else:
        print(b, True)
