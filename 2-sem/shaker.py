# Кондрашова Ольга ИУ7-25Б

# Программа измеряет время сортировки трех массивов разной размерности
# Метод сортировки - шейкер

# small_entry, average_entry, big_entry - размеры массивов
# start_time, fin_time - начало и конец измерения времени
# res - время, затраченное на сортировку
# sort_sorted - отсортированный массив
# sort_inverse - отсортированный в обратном порядке массив
# sort_random - неотсортированный массив случайных чисел

from tkinter import *
from tkinter import messagebox as mb
import random
import time

# массив случайных чисел
def random_array(size):
    return [random.randint(-100, 100) for i in range(int(size))]

# отсортированный массив
def sorted_array(size):
    return [i for i in range(int(size))]

# отсортированный в обратном порядке массив
def inverse_array(size):
    A = sorted_array(size)
    A.reverse()
    return A

# сортировка шейкер
def shaker_sort(a):
    start_time = time.time()
    left = 0
    right = len(a) - 1
    while left <= right:
        # прохождение массива слева направо
        for i in range(left, right, +1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        right -= 1
        # прохождение массива справа налево
        for i in range(right, left, -1):
            if a[i - 1] > a[i]:
                a[i], a[i - 1] = a[i - 1], a[i]
        left += 1
        if left > right:
            break
    fin_time = time.time()
    res = fin_time - start_time
    return res

# демонстрация сортировки
def show_sort():
    a = [random.randint(-100, 100) for i in range(int(small_entry.get()))]
    y_coord = 270
    left = 0
    right = len(a) - 1
    while left <= right:
        # прохождение массива слева направо
        for i in range(left, right, +1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        right -= 1
        # прохождение массива справа налево
        for i in range(right, left, -1):
            if a[i - 1] > a[i]:
                a[i], a[i - 1] = a[i - 1], a[i]
        left += 1
        if left > right:
            break
        text_array = Label(text = a)
        text_array.place(x = 25, y = y_coord)
        y_coord += 20
    return a

# расчет времени сортировки маленького массива
def column_one():
    small_size = small_entry.get()
    sort_sorted = sorted_array(small_size)
    sort_inverse = inverse_array(small_size)
    sort_random = random_array(small_size)
    res1 = shaker_sort(sort_sorted)
    text_res1 = Label(text = '{:1.6e}'.format(res1))
    text_res1.place(x = 150, y = 45)
    res2 = shaker_sort(sort_inverse)
    text_res2 = Label(text = '{:1.6e}'.format(res2))
    text_res2.place(x = 150, y = 65)
    res3 = shaker_sort(sort_random)
    text_res3 = Label(text = '{:1.6e}'.format(res3))
    text_res3.place(x = 150, y = 85)

# расчет времени сортировки среднего массива
def column_two():
    average_size = average_entry.get()
    sort_sorted = sorted_array(average_size)
    sort_inverse = inverse_array(average_size)
    sort_random = random_array(average_size)
    res1 = shaker_sort(sort_sorted)
    text_res1 = Label(text = '{:1.6e}'.format(res1))
    text_res1.place(x = 250, y = 45)
    res2 = shaker_sort(sort_inverse)
    text_res2 = Label(text = '{:1.6e}'.format(res2))
    text_res2.place(x = 250, y = 65)
    res3 = shaker_sort(sort_random)
    text_res3 = Label(text = '{:1.6e}'.format(res3))
    text_res3.place(x = 250, y = 85)

# расчет времени сортировки большого массива
def column_three():
    big_size = big_entry.get()
    sort_sorted = sorted_array(big_size)
    sort_inverse = inverse_array(big_size)
    sort_random = random_array(big_size)
    res1 = shaker_sort(sort_sorted)
    text_res1 = Label(text = '{:1.6e}'.format(res1))
    text_res1.place(x = 350, y = 45)
    res2 = shaker_sort(sort_inverse)
    text_res2 = Label(text = '{:1.6e}'.format(res2))
    text_res2.place(x = 350, y = 65)
    res3 = shaker_sort(sort_random)
    text_res3 = Label(text = '{:1.6e}'.format(res3))
    text_res3.place(x = 350, y = 85)

# проверка и вывод
def table():
    # проверка на ввод целых чисел
    try:
        small_entry_int = int(small_entry.get())
        average_entry_int = int(average_entry.get())
        big_entry_int = int(big_entry.get())
    except ValueError:
        mb.showerror("Ошибка", "Неккоректный ввод.")
    else:
        text_one = Label(text = small_entry.get())
        text_one.place(x = 180, y = 25)
        text_two = Label(text = average_entry.get())
        text_two.place(x = 280, y = 25)
        text_three = Label(text = big_entry.get())
        text_three.place(x = 380, y = 25)
        column_one()
        column_two()
        column_three()
        show_sort()

# интерфейс
root = Tk()
root.geometry('500x400')
root.resizable(width = False, height = False)

text_size = Label(text = 'Размер:')
text_size.place(x = 25, y = 25)
text_sort = Label(text = 'Сортированный:')
text_sort.place(x = 25, y = 45)
text_inverse = Label(text = 'Обратный порядок:')
text_inverse.place(x = 25, y = 65)
text_rndm = Label(text = 'Случайный')
text_rndm.place(x = 25, y = 85)

text_small = Label(text = 'Маленький массив:')
text_small.place(x = 25, y = 140)
small_entry = Entry(root, width = 20, bg = 'white')
small_entry.place(x = 150, y = 140)
text_average = Label(text = 'Средний массив:')
text_average.place(x = 25, y = 160)
average_entry = Entry(root, width = 20, bg = 'white')
average_entry.place(x = 150, y = 160)
text_big = Label(text = 'Большой массив:')
text_big.place(x = 25, y = 180)
big_entry = Entry(root, width = 20, bg = 'white')
big_entry.place(x = 150, y = 180)

but_sort = Button(text = 'Отсортировать', command = table)
but_sort.place(x = 200, y = 210)

text_sort = Label(text = 'Сортировка маленького массива:')
text_sort.place(x = 25, y = 250)

root.mainloop()
