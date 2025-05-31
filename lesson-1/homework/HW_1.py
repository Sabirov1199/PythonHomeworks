#Given a side of square. Find its perimeter and area.
a=int(input('a ni kirgizing'))
b=int(input('b ni kirgizing'))

p=a+b*2
s=a*b
print(f'Perimeter {p}\nYuzi {s}')

#Given diameter of circle. Find its length

D=int(input('Diametrni kirgizing'))

Lent=D*3.14
print(f'Uzunligi {Lent}')


#Given two numbers a and b. Find their mean
a=int(input('a ni kirgizing'))
b=int(input('b ni kirgizing'))

AVG=(a+b)/2
print(f'average {AVG}')

#Given two numbers a and b. Find their sum, product and square of each number.
a=int(input('a ni kirgizing'))
b=int(input('b ni kirgizing'))
S=a+b
P=a*b
Sq=a**2
Sqb=b**2
print(f'sum {S}\nProduct{P}\nsquarea{Sq}\nSquareb{Sqb}')
