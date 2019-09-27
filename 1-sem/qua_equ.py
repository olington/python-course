# Решение квадратных уравнений
# Кондрашова
# D - дискриминант
# discr - вывод дискриминанта
# sq - квадратный корень дискриминанта
# x, x1, x2 - корни уравнения
# a - первый коэффициент
# b - второй коэффициент
# c - третий коэффициент
# zn - рабочая переменная

import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
print ()

if a == 0:
    if b == 0:
        if c == 0:
            print ("x - любое число")
        else:
            print("Корней нет")
    else:
        x = -c / b
        print ("x = {:5.2f}".format(x))
else:
    D = b ** 2 - 4 * a * c
    discr = "D = {:5.2f}".format(D)
    if D > 0:
        sq = math.sqrt(D)
        zn = 2 * a
        x1 = (-b + sq) / zn
        x2 = (-b - sq) / zn
        print(discr,
              "x1 = {:5.2f}"
              "x2 = {:5.2f}".format(x1, x2), sep = "\n")
    elif D == 0:
        x = -b / (2 * a)
        print(discr,
              "x = {:5.2f}".format(x), sep = "\n")
    else:
        print(discr,
              "Мнимые корни", sep = "\n")
