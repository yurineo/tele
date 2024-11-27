# задачаа1
a = 8
b = 10
c = 12
d = 18

dividend = ((-3 + a ** 2) * b - 2 ** 3)
divider = (c - 2 * d)
res = dividend / divider
print(res)



# Задача 2. Часы
minutes = int(input('Введите количество минут: '))

hours = minutes // 60

rest_minutes = minutes % 60

print('Часов:', hours)
print('Осталось минут:', rest_minutes)


Задача 3. Счастливый билет

n = int(input('Введите номер билета: '))

n1 = n // 100000 # первая цифра
n2 = (n % 100000) // 10000 # вторая цифра
n3 = (n % 10000) // 1000 # третья цифра
n4 = (n % 1000) // 100 # четвертая цифра
n5 = (n % 100) // 10 # пятая цифра
n6 = n % 10 # шестая цифра

if n1 + n2 + n3 == n4 + n5 + n6:
print('yes')
else:
print('no')


#задача 4


leg_1 = int(input('Введите длину первого катета: '))
leg_2 = int(input('Введите длину второго катета: '))

square = leg_1 * leg_2 / 2

print('Площадь прямоугольного треугольника:', square)

