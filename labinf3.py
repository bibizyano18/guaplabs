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
print("Result:", len(words))