# Кондрашова Ольга ИУ7-25Б

# x1, y1 - массивы, в которых хранятся корни функции
# x_ext, y_ext - массивы, в которых хранятся экстремумы функции
# x_coor, y_coor - массивы, в которых хранятся координаты всей функции
# a, b - концы заданного отрезка
# h - шаг
# eps - эпсилент
# n - максимальное количество итераций
# i - количество корней
# a1, b1 - элементраный интервал
# x, y, x_e, y_e, x_ox, y_ox, x0, y0 - координаты для графика
# t - словарь, содержащий интервал, шаг, ошибку и max кол-во итераций
# num - номер итерации

from tkinter import *
import math as m
import random
from time import time
import tkinter.messagebox as mb
import matplotlib.pyplot as plt
import numpy as np

def root_search(a, b, eps, n):
    i = 0
    xprev = b
    while(i < n):
        i += 1
        y = f(xprev)
        fi = fi_f(xprev)
        x = fi
        if abs(x - xprev) < eps:
            return x, i, 0
        xprev = x
        
    return 10 * '-', i, 1

def solution(a, b, eps, h, n):
    c1 = a
    c2 = a
    k = 0
    while(c2 < b):
        found = True
        x_sol = 0
        y_sol = 0
        err_code = 0
        n_iter = 1
        
        c2 += h
        if c2 > b:
            c2 = b
        if abs(f(c1)) <= 1e-20:
            x_sol = c1
            y_sol = f(c1)
        elif abs(f(c2)) <= 1e-20:
            if c2 == b:
                x_sol = c2
                y_sol = f(c2)
            else:
                found = False
        elif f(c1)*f(c2) < 0:
            x_sol, n_iter, err_code = root_search(c1,c2,eps,n)
            if err_code == 0:
                y_sol = f(x_sol)
        else:
            found = False

        if found:
            k += 1
            print("{:3d}".format(k),end = ' ')
            t['n'].append(k)
            print("[{:10.7f};{:10.7f}]".format(c1,c2),end = ' ')
            t['ab'].append([(round(c1, 8)), (round(c2, 8))])
            if err_code == 0:
                print("{:10.7f}".format(x_sol),end = ' ')
                print("{:10.7f}".format(y_sol),end = ' ')
                t['y'].append(y_sol)
                t['x'].append(x_sol)
            else:
                print(10 * '-',end = ' ')
                print(10 * '-',end = ' ')
                t['x'].append(12 * '-')
                t['y'].append(12 * '-')
            print("{:8d}".format(n_iter),end = ' ')
            t['N'].append(n_iter)
            print("{:10d}".format(err_code))
            t['err'].append(err_code)  
        c1 = c2            
        
def main():
    Lb1.delete(0, END)
    Lb2.delete(0, END)
    Lb3.delete(0, END)
    Lb4.delete(0, END)
    Lb5.delete(0, END)
    Lb6.delete(0, END)
    e = 0.0000000000001
    flag = 0
    x1 = []
    y1 = []
    x_ext = []
    y_ext = []
    x_coor = []
    y_coor = []
    try:
        a = float(E1.get())
        b = float(E2.get())
        step = float(E3.get())
        eps = float(E4.get())
        n = float(E5.get())
        flag = 1
    except:
        mb.showerror("Неверный ввод","Введите действительные числа в поля ввода")
    if flag == 1:
        num = 1
        t['n'], t['ab'], t['x'], t['y'],\
                    t['N'], t['err']= [], [], [], [], [], []
        # данные для таблицы
        a1, b1 = a, b
        num = 0
        while a < b:
            if f(a) == 0 and num != 0:
                num -= 1
            else:
                if (a + step) > b:
                    solution(a, b, eps, n, num)
                else:
                    solution(a, a + step, eps, n, num)
            a += step
            num += 1

        n = len(t['n'])
        i = 0
        
        while i < (n - 1):
            if (str(t['x'][i]) != 12 * '-' and str(t['x'][i+1]) != 12 * '-'):
                if abs(t['x'][i] - t['x'][i + 1]) <= eps:
                    t['ab'].pop(i)
                    t['err'].pop(i)
                    t['n'].pop(i)
                    t['x'].pop(i)
                    t['y'].pop(i)
                    t['N'].pop(i)
                    n -= 1
                    i -= 1
            i += 1

        print(t)
        if t['n'] == []:
            mb.showerror("Ошибка!", 'Нет корней на [' +\
                                 str(a1) + '; ' + str(b1) + ']')

        # таблица
        num = 1
        for i in range(len(t['n'])):
            Lb1.insert(END, ''.join(str(num) + '.').center(3))
            num += 1
            Lb2.insert(END, ''.join(str(t['ab'][i]).center(12)))
            try:
                print(str(t['x'][i]))
                if (12 * '-') == str(t['x'][i]):
                    print('!!!')
                    Lb3.insert(END, ''.join())\
                        ('{:g}'.format(t['x'][i]).center(12)))
                else:
                    Lb3.insert(END, ''.join('{:g}'.format\
                                               (t['x'][i]).center(13)))
                print(str(t['y'][i]))
                if (12 * '-') == str(t['y'][i]):
                    print('???')
                    Lb4.insert(END, ''.join \
                        ('{:1.0e}'.format(t['y'][i]).center(12)))
                else:
                    Lb4.insert(END, ''.join('{:1.0e}'.format \
                                              (t['y'][i]).center(13)))
            except:
                Lb3.insert(END, ''.join(t['x'][i]).center(14))
                Lb4.insert(END, ''.join(t['y'][i]).center(14))

            Lb5.insert(END, ''.join(str(t['N'][i]).center(18)))
            Lb6.insert(END, ''.join(str(t['err'][i]).center(18)))

        # график
        x = []
        y = []
        x_e = []
        y_e = []
        x_ox = [a1, b1]
        x_oy = [0, 0]
        x0 = []
        y0 = []
        a2 = a1
        while a1 < b1:
            # экстремумы
            if f(a1 - 0.001) < f(a1) and f(a1 + 0.001) < f(a1) \
               or f(a1 - 0.001) > f(a1) \
                    and f(a1 + 0.001) > f(a1):
                x_e.append(a1)
                y_e.append(f(a1))
            # корни 
            if f(a1 - 0.001) < 0 and f(a1 + 0.001) > 0 or f(a1 - 0.001) > 0 \
                    and f(a1 + 0.001) < 0:
                x0.append(a1)
                y0.append(f(a1))
                a += 0.01
            elif abs(round(float('{:g}'.format(f(a1))), 6)) == 0:
                x0.append(a1)
                y0.append(f(a1))
                a += 0.01

            x.append(a1)
            y.append(f(a1))
            a1 += 0.001
        y_oy = [0, 0]
        if min(y) < 0:
            y_oy[0] = min(y)
        else:
            y_oy[0] = -0.5
        if max(y) > 0:
            y_oy[1] = max(y)
        else:
            y_oy[1] = 0.5
        x_oy = [0, 0]

        plt.clf()
        plt.plot(x, y)
        plt.scatter(x_e, y_e, color='blue')
        plt.scatter(x0, y0, color='red')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.grid(True)
        plt.show()

def scroll(*args):
    Lb1.yview(*args)
    Lb2.yview(*args)
    Lb3.yview(*args)
    Lb4.yview(*args)
    Lb5.yview(*args)
    Lb6.yview(*args)

def f(x):
    return x*x - 4
    #return m.cos(x)
    #return x**4 - 3*x**3 + 8 * x**2 - 6

def fi_f(x):
    return x - f(x)

t = {'n': [], 'ab': [], 'x': [], 'y': [], 'N': [], 'err': []}

# Создание окна
root = Tk()
root.title('Подсчет корней методом простых итераций')
root["bg"] = "white"

# Создание виджетов tkinter
Fm = Frame(root)
Sb = Scrollbar(root,command = scroll)

Lab0 = Label(root,font=('times',12),text = 'Ввод констант',width = 15,bg = "white")
Lab1 = Label(root,font=('times',12),text = 'Начало отрезка',width = 15,bg = "white")
Lab2 = Label(root,font=('times',12),text = 'Конец отрезка',width = 15,bg = "white")
Lab3 = Label(root,font=('times',12),text = 'Шаг',width = 15,bg = "white")
Lab4 = Label(root,font=('times',12),text = 'Точность',width = 15,bg = "white")
Lab5 = Label(root,font=('times',12),text = 'Чило итераций',width = 15,bg = "white")

LabTb0 = Label(root,font=('times',12),text = 'Номер',width = 15,bg = "white")
LabTb1 = Label(root,font=('times',12),text = 'Интервал',width = 15,bg = "white")
LabTb2 = Label(root,font=('times',12),text = 'Значение корня',width = 15,bg = "white")
LabTb3 = Label(root,font=('times',12),text = 'Значение функции',width = 15,bg = "white")
LabTb4 = Label(root,font=('times',12),text = '№ итерации',width = 15,bg = "white")

E1 = Entry(root,width = 15,bg = "white")
E2 = Entry(root,width = 15,bg = "white")
E3 = Entry(root,width = 15,bg = "white")
E4 = Entry(root,width = 15,bg = "white")
E5 = Entry(root,width = 15,bg = "white")

B = Button(root,text = 'Вычислить',font=('times',12),command = main)

Lb1 = Listbox(root,font=('times',12),width = 20,height = 10,yscrollcommand=Sb.set,bg = "white")
Lb2 = Listbox(root,font=('times',12),width = 20,height = 10,yscrollcommand=Sb.set,bg = "white")
Lb3 = Listbox(root,font=('times',12),width = 20,height = 10,yscrollcommand=Sb.set,bg = "white")
Lb4 = Listbox(root,font=('times',12),width = 20,height = 10,yscrollcommand=Sb.set,bg = "white")
Lb5 = Listbox(root,font=('times',12),width = 20,height = 10,yscrollcommand=Sb.set,bg = "white")
Lb6 = Listbox(root,font=('times',12),width = 20,height = 10,yscrollcommand=Sb.set,bg = "white")

Lb7 = Listbox(root,font=('times',12),width = 40,height = 4,bg = "white")
Lb7.insert(END, "0 - корень нашелся\n")
Lb7.insert(END, "1 - превышение количества итераций\n")
Lb7.insert(END, "2 - выход за пределы интервала\n")

Lab11 = Label(root,text = "№",font=('times',12),bg = "white")
Lab12 = Label(root,text = "Интервал",font=('times',12),bg = "white")
Lab13 = Label(root,text = "Значение корня",font=('times',12),bg = "white")
Lab14 = Label(root,text = "Значение функции",font=('times',12),bg = "white")
Lab15 = Label(root,text = "№ итерации",font=('times',12),bg = "white")
Lab16 = Label(root,text = "Код ошибки",font=('times',12),bg = "white")
Labtit = Label(root,font=('times',14),text = 'Таблица значений',bg = "white")
Lab20 = Label(root,text = "Коды ошибок",font=('times',13),bg = "white")

# Размещение виджетов
Lab1.grid(row = 0,column = 1)
Lab2.grid(row = 0,column = 2)
Lab3.grid(row = 0,column = 3)
Lab4.grid(row = 0,column = 4)
Lab5.grid(row = 0,column = 5)

Lab0.grid(row = 1,column = 0)
E1.grid(row = 1,column = 1)
E2.grid(row = 1,column = 2)
E3.grid(row = 1,column = 3)
E4.grid(row = 1,column = 4)
E5.grid(row = 1,column = 5)
B.grid(row = 2,column = 3)

Labtit.grid(row = 3,column = 0,columnspan = 6)

Lab11.grid(row = 4,column = 0)
Lab12.grid(row = 4,column = 1)
Lab13.grid(row = 4,column = 2)
Lab14.grid(row = 4,column = 3)
Lab15.grid(row = 4,column = 4)
Lab16.grid(row = 4,column = 5)

Lb1.grid(row = 5,column = 0)
Lb2.grid(row = 5,column = 1)
Lb3.grid(row = 5,column = 2)
Lb4.grid(row = 5,column = 3)
Lb5.grid(row = 5,column = 4)
Lb6.grid(row = 5,column = 5)
Sb.grid(row = 5,column = 6,sticky=S+N)

Lab20.grid(row = 6,column = 0,columnspan = 2)
Lb7.grid(row = 7,column = 0,columnspan = 2)

root.mainloop()
