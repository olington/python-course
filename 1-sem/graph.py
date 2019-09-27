# Вычислить таблицу значений функции, результаты вычислений оформить в виде
# таблицы с заголовком. Построить график одной из функций, у которой есть
# положительные и отрицательные значения. Рисовать нулевую линию,
# которая идет вниз, эта линия может быть или не быть в зависимости
# Кондрашова
# от значения функций.
# y -значение функции
# x - аргумент функции
# num - порядковый номер
# start - начальное значение
# end - конечное значение
# step - шаг
# m - звездочка
# mo - ось
# l - длина

start = float(input("Введите начальное значение: "))         
end = float(input("Введите конечное значение: "))
step = float(input("Введите шаг: "))

print("№  \u2502     X     \u2502     Y \n",
      3 * "\u2500", "\u253c", 11 * "\u2500", "\u253c", 11 * "\u2500", sep = "")
eps = 0.000000005
num = 1
x = start
xl = []
yl = []
while x < (end + eps):
    y = (x ** 9) + (34 * x ** 8) - (2 * x ** 7) + (24 *x ** 6) - (76 * x ** 5)\
            + (33 * x ** 4) - (x ** 3) + (3 * x ** 2) + (7 * x) - 33
    print("{:2} \u2502 {:9.4f} \u2502 {:9.4f}".format(num, x, y))
    xl.append(x)
    yl.append(y)
    ymin = ymax = yl[0]
    xmin = xmax = xl[0]
    for i in range (len(yl)):
        if yl[i] < ymin:
            ymin = yl[i]
            xmin = xl[i]
            i += 1
        elif yl[i] > ymax:
            ymax = yl[i]
            xmax = xl[i]
            i += 1
    x += step
    num += 1
print("Минимальное значение Y: {:.4f} \n"
      "Значение переменной X: {:.4f}".format(ymin, xmin))
print()

l = 50

if ymin > 0 or ymax < 0:
    mo = False
else:
    mo = True
    
mo = int((- ymin) * l / ((ymax - ymin)))

if mo < l:
    print("X", 10 * " ", "{:.1f}".format(ymin), (mo // 4) * " ",\
          "{:.1f}".format(ymin / 2), (mo // 4) * " ", "0", (l // 4) * " ",\
          "{:.1f}".format(ymax / 2), (l // 4) * " ", "{:.1f}".format(ymax))
    print(15 * " ", "\u2514", (mo // 2) * "\u2500", "\u2534",\
          (mo - 1 - (mo // 2)) * "\u2500", "\u253C", ((l - mo) // 2) * "\u2500", "\u2534",\
          (l - mo - 1 - ((l - mo) // 2)) * "\u2500", "\u2518", "Y", sep = "")

    for i in range (len(xl)):   
        m = int((yl[i] - min(yl)) * l / (max(yl) - min(yl)))
        if m == mo:
            print("{:9.4f}".format(xl[i]), 7 * " ", m * " ", "*", \
                    (l - m - 1) * " ", sep = "")
        elif m < mo:
            print("{:9.4f}".format(xl[i]), 7 * " ", m * " ", "*", \
                    (mo - m - 1) * " ", "\u2502", sep = "")
        else:
            print("{:9.4f}".format(xl[i]), 7 * " ", mo * " ", "\u2502", \
                    (m - mo - 1) * " ", "*", sep = "")
        
else:
    print("X", 10 * " ", "{:.1f}".format(ymin), (l // 2) * " ",\
          "{:.1f}".format(ymin / 2), (l // 2) * " ", "0",
          "{:.1f}".format(ymax / 2), "{:.1f}".format(ymax))
    print(15 * " ", "\u2514", (l // 2) * "\u2500", "\u2534",\
          (l - 1 - (l // 2)) * "\u2500",  "\u253C", "\u2534",\
          "\u2518", "Y", sep = "")
    
    mo, l = l, mo
    for i in range (len(xl)):   
        m = int((yl[i] - min(yl)) * l / (max(yl) - min(yl)))
        if m == mo:
            print("{:9.4f}".format(xl[i]), 7 * " ", m * " ", "*", \
                    (l - m - 1) * " ", sep = "")
        elif m < mo:
            print("{:9.4f}".format(xl[i]), 7 * " ", m * " ", "*", \
                    (mo - m - 1) * " ", "\u2502", sep = "")
        else:
            print("{:9.4f}".format(xl[i]), 7 * " ", mo * " ", "\u2502", \
                    (m - mo - 1) * " ", "*", sep = "")
            
print((mo + 14) * " ", "X")
        
