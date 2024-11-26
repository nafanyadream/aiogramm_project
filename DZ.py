# Задание 1
def bill():
    a, b = "Don't compare yourself with anyone in this world…", "if you do so, you are insulting yourself.”"
    print('“' + a, "\n" + b + "\n                                         Bill Gates")
bill()
# Задание 2
def chet():
    a = int(input("Введите начало диапозона: "))
    b = int(input("Введите конец диапозона: "))
    c = list()
    for i in range(a, b + 1):
        if i % 2 == 0:
            c.append(i)
    print(c)
chet()
# Задание 3
def kvadrat():
    a = input("Пустой или Заполненный? ( True or False ) ")
    b = int(input("Длинна стороны квадрата: "))
    c = input("Символ квадрата: ")
    if a == "True":
        for i in range(b//2 - 1):
            print("       " + c * b)
    elif a == "False":
        print("       " + c * b)
        for i in range(b//2 - 1):
            print("       " + c + (" " * (b - 2) + c))
        print("       " + c * b)
kvadrat()
# Задание 4
def mina():
    j = list()
    for i in range(5):
        a = int(input("Введите число любое "))
        j.append(a)
    print(min(j))
mina()
# Задание 5
def proz():
    a = 1
    b = int(input("Введите начало диапозона "))
    c = int(input("Введите конец диапозона "))
    for i in range(min(b, c), max(b, c)):
        a = a * i
    print(a)
proz()
# Задание 6
def shish():
    a = input("Введите цифры ")
    print(len(a))
shish()
# Задание 7
def polindrom():
    a = input("Введите набор из 6 цифр ")
    if a[0] == a[5] and a[1] == a[4] and a[2] == a[3]:
        print("True")
    else:
        print("False")
polindrom()