'''
#   На вход подается строка, состоящая из одного числа. Напишите программу, которая удваивает его.
number = int(input())
print(number * 2)


#   Вводится число. Вывести его квадрат.
square = int(input())
print(square ** 2)


#   Вводятся часы, минуты и секунды. Вывести, сколько секунд прошло с полуночи.
#   Вывести, какая часть суток прошла (число от 0 до 1).
hour = int(input('Hour:'))
minutes = int(input('Minutes:'))
second = int(input('Seconds:'))
allsecond = (hour * 3600) + (minutes * 60) + second
daytime = allsecond/86400
print('Seconds:', allsecond)
print('Day time:', round(daytime, 4))


#   Вводится число. Вывести, оканчивается ли оно на цифру 7, не используя приведение к строке и операции над строками
konec = int(input())
if konec % 10 == 7:
    print('TRUE')
else:
    print('FALSe')


#   Вводятся коэффициенты уравнения ax2+bx+c=0. Вывести его корни(не забыть проверить, что a не равно 0)
a = int(input())
b = int(input())
c = int(input())
disk = b ** 2 - 4 * a * c
if a!=0:
    if disk == 0:
        x0 = (-b) // (2*a)
        print(x0)
    elif disk > 0:
        x1 = (-b + (disk ** (0.5))) / (a * 2)
        x2 = (-b - (disk ** (0.5))) / (a * 2)
        print(round(x1, 4))
        print(round(x2, 4))
    else:
        print('ErrOOOrrrr')
else:
    print((-c)/b)


#   Вводятся три числа. Вывести максимум из них
first = int(input())
second = int(input())
third = int(input())
print(max(first, second, third))

'''
#	Вводится число. Вывести среднее арифметическое (с точностью до двух знаков после запятой)
#   тех чисел в диапазоне от единицы до введённого числа, которые делятся 5 или являются четными
need = int(input())
summ = 0
arifm = 0
kol = 0
for i in range(1, need):
    if i%2==0 or i%5==0:
        summ+=i
        kol+=1
    else:
        continue
arifm = summ / kol
print(round(arifm, 2))
