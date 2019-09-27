# Кондрашова Ольга ИУ7-25Б
#
# Калькулятор выполняет следующие действия: перевод из 10 с/с в 5с/с
# обратный перевод; очистка полей; вывод информации о программе.
#
# n - отступ при вводе
# entered_number - введенное число
# win_left - поле ввода
# win_right - поле вывода
# res - результат перевода
# parts, p_one, p_two - целая и дробная часть введенного числа
# text_r - текст в поле вывода

from tkinter import *
from tkinter import messagebox as mb

# Кнопка '1'
def one():
    win_left.insert(END, '1')

# Кнопка '2'
def two():
    win_left.insert(END, '2')

# Кнопка '3'
def three():
    win_left.insert(END, '3')

# Кнопка '4'
def four():
    win_left.insert(END, '4')

# Кнопка '5'
def five():
    win_left.insert(END, '5')

# Кнопка '6'
def six():
    win_left.insert(END, '6')

# Кнопка '7'
def seven():
    win_left.insert(END, '7')

# Кнопка '8'
def eight():
    win_left.insert(END, '8')

# Кнопка '9'
def nine():
    win_left.insert(END, '9')

# Кнопка '0'
def zero():
    win_left.insert(END, '0')

# Кнопка '.'
def point():
    win_left.insert(END, '.')
    
# Кнопка '-'
def minus():
    win_left.insert(END, '-')

# Перевод из 10 с/с в 5 с/с
def ten_to_five():
    entered_number = win_left.get()
    flag = 0
    # Проверка на ввод
    try:
        number = float(entered_number)
    except ValueError:
        mb.showerror("Ошибка", "Неккоректный ввод.")
        clear_both()
    else:
        # Проверка на дробное число
        if entered_number[-1] == '.' or entered_number[0] == '.':
            mb.showerror("Ошибка", "Неккоректный ввод.")
            clear_both()
            flag = 1
        if flag == 0:
            # Проверка на отрицательное число
            if entered_number[0] == '-':
                entered_number = entered_number[1:]
                flag = 2
            if entered_number.count('.') == 1:
                res1 = res2 = ''
                parts = entered_number.split('.')
                p_one = int(parts[0])
                p_two = int(parts[1])
                k = len(parts[1])
                res = ''
                while p_one != 0:
                    res1 += str(p_one % 5)
                    p_one //= 5
                j = 0
                while j < 5:
                    p_two *= 5
                    p_two = str(p_two)
                    res2 += p_two[:-k]
                    if len(p_two) > 1:
                        p_two = p_two[1:]
                    p_two = int(p_two)
                    j += 1
                res1 = res1[::-1]
                res = str(res1) + '.' + str(res2)
            elif entered_number == '0':
                res = 0
            else:
                res = ''
                number = int(entered_number)
                while number != 0:
                    res += str(number % 5)
                    number //= 5
                res = res[::-1]
            if flag == 2:
                res = '-' + res
            win_right.insert(END, res)

# Перевод из 5 с/с в 10 с/с
def five_to_ten():
    entered_number = win_left.get()
    try:
        number = float(entered_number)
    except ValueError:
        mb.showerror("Ошибка", "Неккоректный ввод.")
        clear_both()
    else:
        flag = 0
        res = ''
        st = 0
        if entered_number[-1] == '.' or entered_number[0] == '.':
            mb.showerror("Ошибка", "Неккоректный ввод.")
            clear_both()
            flag = 1
        for i in entered_number:
            if i.isdigit() and int(i) >= 5:
                mb.showerror("Ошибка", "Число не в пятеричной системе.")
                clear_both()
                flag = 1
            break
        if flag == 0:
            if entered_number[0] == '-':
                entered_number = entered_number[1:]
                flag = 2   
            if entered_number.count('.') == 1:
                res1 = res2 = 0
                parts = entered_number.split('.')
                p_one = int(parts[0])
                p_two = int(parts[1])
                k = len(parts[1])
                while p_one != 0:
                    res1 += (p_one % 10) * pow (5, st)
                    p_one //= 10
                    st += 1
                while p_two != 0:
                    res2 += (p_two % 10) * pow (5, -k)
                    p_two //= 10
                    k -= 1
                res = res1 + res2
            elif entered_number == '0':
                res = 0
            else:
                st = 0
                res = 0
                number = int(entered_number)
                while number!= 0:
                    res += (number % 10) * pow(5, st)
                    number //= 10
                    st += 1
            if flag == 2:
                res = '-' + str(res)
        win_right.insert(END, res)

# Очистить левое поле
def clear_left():
    win_left.delete(0, END)

# Очистить правое поле
def clear_right():
    win_right.delete(0, END)

# Очистить оба поля
def clear_both():
    win_left.delete(0, END)
    win_right.delete(0, END)

# О программе   
def about():
    text_about = 'Автор: Кондрашова Ольга ИУ7-25Б\nПрограмма "Калькулятор"'+\
                 'выполняет следующие действия:\nперевод из 10 с/с в 5с/с;\n'+\
                 'обратный перевод;\nочистка полей; \nвывод информации о '+\
                 'программе;'
    text_about_red = '{:<30}'.format(text_about)
    win = Toplevel(root)
    authtor = Label(win, text=text_about_red)
    authtor.pack()

# Интерфейс    
root = Tk()
root.geometry('500x200')

# Размещение полей ввода и вывода
lab_one = Label(text = 'Поле ввода:')
lab_one.place(x = 25, y = 25)
lab_one = Label(text = 'Поле вывода:')
lab_one.place(x = 250, y = 25)
win_left = Entry(root, width = 200, bg = 'white')
win_left.place(x = 25, y = 45)
win_right = Entry(root, width = 200, bg = 'white')
win_right.place(x = 250, y = 45)

# Размещеие кнопок
but_ttf = Button(text = 'Перевести из 10 с/с в 5 с/с', command = ten_to_five)
but_ttf.place(x = 250, y = 80)
but_ftt = Button(text = 'Перевести из 5 с/с в 10 с/с', command = five_to_ten)
but_ftt.place(x = 250, y = 110)
but_one = Button(text = '1', command = one)
but_one.place(x = 25, y = 80, width = 30)
but_two = Button(text = '2', command = two)
but_two.place(x = 55, y = 80, width = 30)
but_three = Button(text = '3', command = three)
but_three.place(x = 85, y = 80, width = 30)
but_four = Button(text = '4', command = four)
but_four.place(x = 25, y = 106, width = 30)
but_five = Button(text = '5', command = five)
but_five.place(x = 55, y = 106, width = 30)
but_six = Button(text = '6', command = six)
but_six.place(x = 85, y = 106, width = 30)
but_seven = Button(text = '7', command = seven)
but_seven.place(x = 25, y = 132, width = 30)
but_eight = Button(text = '8', command = eight)
but_eight.place(x = 55, y = 132, width = 30)
but_nine = Button(text = '9', command = nine)
but_nine.place(x = 85, y = 132, width = 30)
but_zero = Button(text = '0', command = zero)
but_zero.place(x = 25, y = 158, width = 30)
but_t = Button(text = '.', command = point)
but_t.place(x = 55, y = 158, width = 30)
but_minus = Button(text = '-', command = minus)
but_minus.place(x = 85, y = 158, width = 30)

# Меню
m = Menu(root)
root.config(menu = m)

clearm = Menu(m) 
m.add_cascade(label='Очистить', menu = clearm) 
clearm.add_command(label='Очистить левое поле', command = clear_left) 
clearm.add_command(label='Очистить правое поле', command = clear_right)
clearm.add_command(label='Очистить оба поля', command = clear_both)
 
informationm = Menu(m) 
m.add_cascade(label = 'Информация', menu = informationm) 
informationm.add_command(label = 'О программе', command = about)

root.mainloop()
