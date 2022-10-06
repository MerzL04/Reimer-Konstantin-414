#Задание №1
x = 'Hello world!'
y = 0
for i in range(len(x)):
    y+=1
print(y)

#Задание №2
print(x[::-1])

#Задание №3
z = 'Hello \'world\'!'
print(z[7:12])

 
#Звдвние №4
a = '23 456'
print(a[3:6], a[0:2])

#Задание №5
b = 'ivan@lenta.ru'
print(b [0:4])

#Задание №6
c = '7(495) 234-56-78'
c = c.replace('-',"")
c = c.replace(')',"")
c = c.replace('(',"")
c = c.replace(' ',"")
print(c)


#Задание №7
h = 'Hello world!'
print(h[0:5])
print(h[6:12])

#Задание №8
l = 'qwerty454ytrewq'
n = l[::-1]
if l == n:
    print('yes')