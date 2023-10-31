# Ввести строку, подсчитать количество слов заданной длины.
# Выбираешь длину (например 3) и считаешь кол-во слов, длина которых совпадает с этим числом
string = str(input("Enter your word: "))
while True:
    try:
        key = int(input("Enter length: "))
        if key > 0:
            break
        else:
            print("Invalid syntax: input an integral number")
    except ValueError:
        print("Invalid syntax: input an integral number")
words = []
string = string.split()
for i in range(len(string)):
    if len(string[i]) == key:
        words.append(string[i])
# dop

def sort(s):
    for i in range(len(s)):
        c = 0
        for j in range(len(s)-1):
            while c <= len(s[j]):
                if ord(s[j][c]) > ord(s[j+1][c]):
                    s[j], s[j+1] = s[j+1], s[j]
                    c = len(s[j]) + 100
                else:
                    if ord(s[j][c]) == ord(s[j+1][c]):
                        c = c + 1
                    else:
                        c = len(s[j]) + 100
                if c == len(s[j]):
                    c = c + 1
            c = 0
    return s


sort(words)



print("Result:", len(words), words)