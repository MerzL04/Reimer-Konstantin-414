#Задание №1
x = 'Hello world!'
y = 0
for i in range(len(x)):
    y+=1
print(y)

print(x[::-1])

z = 'Hello \'world\'!'
print(z[7:12])

 
#Звдвние №2
a = '23 456'
print(a[3:6], a[0:2])

b = 'ivan@lenta.ru'
print(b [0:4])

c = '7(495) 234-56-78'
c = c.replace('-',"")
c = c.replace(')',"")
c = c.replace('(',"")
c = c.replace(' ',"")
print(c)


#Задание №3
h = 'Hello world!'
print(h[0:5])
print(h[6:12])


l = 'qwerty454ytrewq'
n = l[::-1]
if l == n:
    print('yes')