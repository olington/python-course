from math import sin

def f(x):
    return x

def middleRect(a, b, n): # срединные прямоугольники
    s = 0
    h = (b - a) / n
    for i in range(n):
        s += f(a + i * h + h / 2)
    s *= h
    return s

def Newton(a, b, n): # метод 3/8
    s = 0
    h = (b - a) / n
    for i in range(n):
        s += f(a+i*h)+3*f(a+i*h+h/3)+3*f(a+i*h+2*h/3)+f(a+i*h+h)
    s *= h / 8
    return s

def Calc_middleRect(a, b, eps):
    n = 1
    while (abs(middleRect(a, b, 2 * n) - middleRect(a, b, n)) > eps):
        n *= 2
    return n

def Calc_Newton(a, b, eps):
    n = 1
    while (abs(Newton(a, b, 2 * n) - Newton(a, b, n)) > eps):
        n *= 2
    return n

a = float(input('Введите левую границу: '))
b = float(input('Введите правую границу: '))
n1 = int(input('Введите N1: '))
n2 = int(input('Введите N2: '))
eps = float(input('Введите eps: '))

I1 = float(middleRect(a, b, n1))
I3 = float(middleRect(a, b, n2))
i1 = '{:19.4f}'.format(I1)
i3 = '{:19.4f}'.format(I3)

if n1 % 3 == 0:
    I2 = float(Newton(a, b, n1))
    if len(str(I2)) <= 19:
        i2 = '{:19.4f}'.format(I2)
    else:
        i2 = '{:19.4e}'.format(I2)
else:
    I2 = i2 = '         -         '
if n2 % 3 == 0:
    I4 = float(Newton(a, b, n2))
    if len(str(I4)) <= 19:
        i4 = '{:19.4f}'.format(I4)
    else:
        i4 = '{:19.4e}'.format(I4)
else:
    I4 = i4 = '         -         '

print(' '*34, '\u250c', '\u2500' * 21,'\u252c','\u2500'*21,'\u2510', sep = '')
print(' '*34,'\u2502',' '*8,'{:4}'.format(n1),' '*9,'\u2502',' '*8,\
      '{:4}'.format(n2),' '*9,'\u2502',sep = '')
print('\u250c','\u2500'*33,'\u253c','\u2500'*21,'\u253c','\u2500'*21,'\u2524',\
      sep='')
print('\u2502',' ','Метод срединных прямоугольников',' ','\u2502',' ',\
      i1,' ','\u2502',' ',i3,' ','\u2502',sep = '')
print('\u251c','\u2500'*33,'\u253c','\u2500'*21,'\u253c','\u2500'*21,'\u2524',\
      sep='')
print('\u2502',' '*12,'Метод 3/8',' '*12,'\u2502',' ',i2,' ','\u2502',\
      ' ',i4,' ','\u2502',sep = '')
print('\u2514','\u2500'*33,'\u2534','\u2500'*21,'\u2534','\u2500'*21,'\u2518',\
      sep='')

if (Calc_middleRect(a, b, eps) < Calc_Newton(a, b, eps)):
    print ('Более точный метод - срединных прямоугольников.\n',
           'Точность достигается при n = ', Calc_middleRect(a, b, eps), sep = '')
else:
    print ('Более точный метод - метод 3/8\n',
           'Точность достигается при n = ', Calc_Newton(a, b, eps), sep = '')
