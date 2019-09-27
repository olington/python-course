# Из заданного множества точек на плоскости выбрать 2 различные точки так,
# чтобы окружности заданного радиуса с центрами в этих точках содержали внутри
# себя одинаковое количество заданных точек.
#
# Кондрашова
# ИУ7-15

from tkinter import *
from tkinter import messagebox as mb

def but_func():
    global n
    if((not point_str.get().count(' ') == 1) or (point_str.get()\
    .split()[0].replace('-','',1).replace('.','',1).isdigit() == False)\
    or (point_str.get().split()[0].find('-') > 0) or (point_str.get()\
    .split()[1].replace('-','',1).replace('.','',1).isdigit() == False)\
    or (point_str.get().split()[1].find('-') > 0)):
        mb.showerror("Ошибка", "Неккоректный ввод.")
    else:
        l.insert(END, point_str.get())
        entry.delete(0, END)
        n += 1
        
def but_func_2():
    global n
    l.delete(0, END)
    n = 0
    
x_max = 940
x_min = 0
y_max = 730
y_min = 0

def but_func_3():
    global x_max, x_min, y_max, y_min
    if((rad_str.get().replace('.','',1).isdigit()== False)):
        mb.showerror("Ошибка", "Неккоректный ввод.")
    elif (not points_str.get().isdigit()):
        mb.showerror("Ошибка", "Неккоректный ввод.")
    elif n == 0:
        mb.showerror("Ошибка", "Не введено ни одной точки")
    else:
        n1 = -1
        n2 = -1
        for i in range(n):
            k = 0
            
            if (float(l.get(i).split()[0]) > x_max):
                x_max = float(l.get(i).split()[0])
            elif (float(l.get(i).split()[0]) < x_min):
                x_min = float(l.get(i).split()[0])
            if (float(l.get(i).split()[1]) > y_max):
                y_max = float(l.get(i).split()[1])
            elif (float(l.get(i).split()[1]) < y_min):
                y_min = float(l.get(i).split()[1])
                
            for j in range(n):
                if j != i:
                    x1=float(l.get(j).split()[0]) - float(l.get(i).split()[0])
                    y1=float(l.get(j).split()[1]) - float(l.get(i).split()[1])
                    if ((x1**2 + y1**2) <= float (rad_str.get())**2):
                        k += 1
                        
            if k == float(points_str.get()):
                if n1 == -1:
                    n1 = i
                else:
                    n2 = i

        if ((n1 == -1) or (n2 == -1)):
            mb.showerror("Ошибка", "При данных условиях задачу решить нельзя.")
        else:
            draw(n1,n2)
            
def draw(n1,n2):
        scale_x = ((x_max - x_min) / 940)
        scale_y = ((y_max - y_min) / 730)
        if scale_x > scale_y:
            scale = scale_x
        else:
            scale = scale_y
        '''print(scale_x, scale_y)'''
        w.delete("all")
        rad = float(rad_str.get())
        print(n1, n2)
        x1, y1 = (float(l.get(n1).split()[0]) - rad + abs(x_min))*scale+5,\
                     (float(l.get(n1).split()[1]) - rad + abs(y_min))*scale+5
        x2, y2 = (float(l.get(n1).split()[0]) + rad + abs(x_min))*scale+5,\
                 (float(l.get(n1).split()[1]) + rad + abs(y_min))*scale+5
        w.create_oval(x1, y1, x2, y2, width=1)
        x1, y1 = (float(l.get(n2).split()[0]) - rad + abs(x_min))*scale+5,\
                     (float(l.get(n2).split()[1]) - rad + abs(y_min))*scale+5
        x2, y2 = (float(l.get(n2).split()[0]) + rad + abs(x_min))*scale+5,\
                 (float(l.get(n2).split()[1]) + rad + abs(y_min))*scale+5
        w.create_oval(x1, y1, x2, y2, width=1)
        
        for i in range(n):
            x1, y1 = (float(l.get(i).split()[0]) - 1 + abs(x_min))*scale+5,\
                     (float(l.get(i).split()[1]) - 1 + abs(y_min))*scale+5
            x2, y2 = (float(l.get(i).split()[0]) + 1 + abs(x_min))*scale+5,\
                     (float(l.get(i).split()[1]) + abs(y_min))*scale+5
            w.create_oval(x1, y1, x2, y2, fill='red')
            
def but_clear():
    w.delete("all")
    
n = 0
root = Tk()
root.geometry('1200x800')
point_str = StringVar()
points_str = StringVar()
rad_str = StringVar()
label1 = Label(text = "Введите координаты точки:")
label1.place(x = 1000, y = 40)
entry = Entry(textvariable = point_str, width=25)
entry.place(x = 1002, y = 70)
but = Button(text = "Добавить точку", command = but_func)
but.place(x = 1032, y = 100)
l = Listbox(height = 20, width = 25)
l.place(x = 1002, y = 150)
but = Button(text = "Удалить все точки", command = but_func_2)
but.place(x = 1023, y = 490)
label2 = Label(text = "Введите радиус окружности:")
label2.place(x = 1000, y = 530)
entry2 = Entry(textvariable = rad_str, width = 25)
entry2.place(x = 1002, y = 560)
label3 = Label(text = "Введите количество точек,\nкоторые входят в окружность:"\
, width=25, height = 2)
label3.place(x = 990, y = 590)
entry3 = Entry(textvariable = points_str, width = 25)
entry3.place(x = 1002, y = 630)
but = Button(text = "Решить", width = 15, command = but_func_3)
but.place(x = 1025, y = 660)
w = Canvas(root, width=950, height=740, bg='white')
w.place(x = 10, y = 10)
but = Button(text = "Очистить поле", command = but_clear)
but.place(x = 450, y = 760)
root.mainloop()
