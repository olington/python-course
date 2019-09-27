# Задан радиус шара. Найти объем и площадь полной поверхности.
# Кондрашова
# R - радиус шара
# V - объем шара
# S - площаль полной поверхности шара

from math import pi

R = float(input("Введите радиус шара: "))
print()

x = pi * R ** 2 
V = 4 / 3 * x * R
S = 4 * x

print ("Объем шара: {:.2f} \n"
       "Площадь полной поверхности: {:.2f}".format(V, S))
