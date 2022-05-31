from tkinter import *
from tkinter.ttk import Radiobutton
import random
import Bubble
import Insert
import Complicated
import time

def DrawRect(firstx, firsty, aside, color):
    canva.create_rectangle(firstx, firsty, firstx + 12, firsty - aside, fill=color)


def DrawNewMas(firstxx):
    firstx = firstxx
    canva.delete(ALL)
    for i in range(scale.get()):
        DrawRect(firstx, firsty, massive[i], "green")
        firstx += 15

global massive, firstx
massive = []
firstxx = 3
firsty = 459



def clicked():
    n = scale.get()
    global massive
    lbl2.configure(text=selected.get())
    if selected.get() == 1:
        lbl2.configure(text="Processing...")
        for i in range(n):
            for j in range(n-1):
                firstx = firstxx
                canva.delete(ALL)
                for c in range(n):
                    if c == j or c == j+1:
                        DrawRect(firstx, firsty, massive[c], "yellow")
                    else:
                        DrawRect(firstx, firsty, massive[c], "green")
                    firstx += 15
                canva.after(500, canva.update())
                if massive[j] > massive[j+1]:
                    firstx = firstxx
                    canva.delete(ALL)
                    for c in range(n):
                        if c == j or c == j + 1:
                            DrawRect(firstx, firsty, massive[c], "red")
                        else:
                            DrawRect(firstx, firsty, massive[c], "green")
                        firstx += 15
                    canva.after(500, canva.update())
                    swap = massive[j]
                    massive[j] = massive[j+1]
                    massive[j+1] = swap
                    firstx = firstxx
                    canva.delete(ALL)
                    for c in range(n):
                        if c == j or c == j + 1:
                            DrawRect(firstx, firsty, massive[c], "blue")
                        else:
                            DrawRect(firstx, firsty, massive[c], "green")
                        firstx += 15
                    canva.after(500, canva.update())
        lbl2.configure(text="Sorted!")
    elif selected.get() == 2:
        lbl2.configure(text="Processing...")
        left = 1
        right = n - 1
        while left != right:
            for i in range(left - 1, right):
                firstx = firstxx
                canva.delete(ALL)
                for c in range(n):
                    if c == i or c == i + 1:
                        DrawRect(firstx, firsty, massive[c], "yellow")
                    else:
                        DrawRect(firstx, firsty, massive[c], "green")
                    firstx += 15
                canva.after(500, canva.update())
                if massive[i] > massive[i + 1]:
                    firstx = firstxx
                    canva.delete(ALL)
                    for c in range(n):
                        if c == i or c == i + 1:
                            DrawRect(firstx, firsty, massive[c], "red")
                        else:
                            DrawRect(firstx, firsty, massive[c], "green")
                        firstx += 15
                    canva.after(500, canva.update())
                    swap = massive[i]
                    massive[i] = massive[i + 1]
                    massive[i + 1] = swap
                    firstx = firstxx
                    canva.delete(ALL)
                    for c in range(n):
                        if c == i or c == i + 1:
                            DrawRect(firstx, firsty, massive[c], "blue")
                        else:
                            DrawRect(firstx, firsty, massive[c], "green")
                        firstx += 15
                    canva.after(500, canva.update())
            right -= 1
            if left == right: break
            for j in range(right + 1, left - 1, -1):
                firstx = firstxx
                canva.delete(ALL)
                for c in range(n):
                    if c == j or c == j - 1:
                        DrawRect(firstx, firsty, massive[c], "yellow")
                    else:
                        DrawRect(firstx, firsty, massive[c], "green")
                    firstx += 15
                canva.after(500, canva.update())
                if massive[j] < massive[j - 1]:
                    firstx = firstxx
                    canva.delete(ALL)
                    for c in range(n):
                        if c == j or c == j - 1:
                            DrawRect(firstx, firsty, massive[c], "red")
                        else:
                            DrawRect(firstx, firsty, massive[c], "green")
                        firstx += 15
                    canva.after(500, canva.update())
                    swap = massive[j]
                    massive[j] = massive[j - 1]
                    massive[j - 1] = swap
                    firstx = firstxx
                    canva.delete(ALL)
                    for c in range(n):
                        if c == j or c == j - 1:
                            DrawRect(firstx, firsty, massive[c], "blue")
                        else:
                            DrawRect(firstx, firsty, massive[c], "green")
                        firstx += 15
                    canva.after(500, canva.update())
            left += 1
        lbl2.configure(text="Sorted!")
    elif selected.get() == 3:
        lbl2.configure(text="Processing...")
        factor = 1.247
        step = int(n // factor)
        while step >= 2:
            for i in range(n - step + 1):
                firstx = firstxx
                canva.delete(ALL)
                for c in range(n):
                    if c == i or c == i + step - 1:
                        DrawRect(firstx, firsty, massive[c], "yellow")
                    else:
                        DrawRect(firstx, firsty, massive[c], "green")
                    firstx += 15
                canva.after(500, canva.update())
                if massive[i] > massive[i + step - 1]:
                    firstx = firstxx
                    canva.delete(ALL)
                    for c in range(n):
                        if c == i or c == i + step - 1:
                            DrawRect(firstx, firsty, massive[c], "red")
                        else:
                            DrawRect(firstx, firsty, massive[c], "green")
                        firstx += 15
                    canva.after(500, canva.update())
                    swap = massive[i]
                    massive[i] = massive[i + step - 1]
                    massive[i + step - 1] = swap
                    firstx = firstxx
                    canva.delete(ALL)
                    for c in range(n):
                        if c == i or c == i + step - 1:
                            DrawRect(firstx, firsty, massive[c], "blue")
                        else:
                            DrawRect(firstx, firsty, massive[c], "green")
                        firstx += 15
                    canva.after(500, canva.update())
            step = int(step // factor)
        lbl2.configure(text="Sorted!")
    elif selected.get() == 4:
        lbl2.configure(text="Processing...")
        number = 1
        for i in range(1, n):
            firstx = firstxx
            canva.delete(ALL)
            for c in range(n):
                if c <= number:
                    DrawRect(firstx, firsty, massive[c], "yellow")
                else:
                    DrawRect(firstx, firsty, massive[c], "green")
                firstx += 15
            canva.after(500, canva.update())
            if massive[i] < massive[i - 1]:
                firstx = firstxx
                canva.delete(ALL)
                for c in range(n):
                    if c <= number-1:
                        DrawRect(firstx, firsty, massive[c], "yellow")
                    elif c == i:
                        DrawRect(firstx, firsty, massive[c], "red")
                    else:
                        DrawRect(firstx, firsty, massive[c], "green")
                    firstx += 15
                canva.after(500, canva.update())
                swap = massive[i]
                massive[i] = massive[i - 1]
                massive[i - 1] = swap
                firstx = firstxx
                canva.delete(ALL)
                for c in range(n):
                    if c < number-1:
                        DrawRect(firstx, firsty, massive[c], "yellow")
                    elif c == number-1 or c == i:
                        DrawRect(firstx, firsty, massive[c], "blue")
                    else:
                        DrawRect(firstx, firsty, massive[c], "green")
                    firstx += 15
                canva.after(500, canva.update())
            for j in range(number - 1, 0, -1):
                if massive[j] > massive[j - 1]: break
                firstx = firstxx
                canva.delete(ALL)
                for c in range(n):
                    if c != j and c <= number:
                        DrawRect(firstx, firsty, massive[c], "yellow")
                    elif c == j:
                        DrawRect(firstx, firsty, massive[c], "red")
                    else:
                        DrawRect(firstx, firsty, massive[c], "green")
                    firstx += 15
                canva.after(500, canva.update())
                if massive[j] < massive[j - 1]:
                    firstx = firstxx
                    canva.delete(ALL)
                    for c in range(n):
                        if c != j and c <= number:
                            DrawRect(firstx, firsty, massive[c], "yellow")
                        elif c == j or c == j - 1:
                            DrawRect(firstx, firsty, massive[c], "red")
                        else:
                            DrawRect(firstx, firsty, massive[c], "green")
                        firstx += 15
                    canva.after(500, canva.update())
                    swap = massive[j]
                    massive[j] = massive[j - 1]
                    massive[j - 1] = swap
                    firstx = firstxx
                    canva.delete(ALL)
                    for c in range(n):
                        if c != j and c!= j -1 and c <= number:
                            DrawRect(firstx, firsty, massive[c], "yellow")
                        elif c == j or c == j - 1:
                            DrawRect(firstx, firsty, massive[c], "blue")
                        else:
                            DrawRect(firstx, firsty, massive[c], "green")
                        firstx += 15
                    canva.after(500, canva.update())
            number += 1
        DrawNewMas(firstxx)
        canva.after(500, canva.update())
        lbl2.configure(text="Sorted!")
    elif selected.get() == 5:
        lbl2.configure(text="Processing...")
        for i in range(n):
            ind = massive.index(min(massive[i:n]))
            firstx = firstxx
            canva.delete(ALL)
            for c in range(n):
                if c < i and c != ind:
                    DrawRect(firstx, firsty, massive[c], "yellow")
                elif c == i or c == ind:
                    DrawRect(firstx, firsty, massive[c], "red")
                else:
                    DrawRect(firstx, firsty, massive[c], "green")
                firstx += 15
            canva.after(500, canva.update())
            if ind != i:
                swap = massive[i]
                massive[i] = massive[ind]
                massive[ind] = swap
                firstx = firstxx
                canva.delete(ALL)
                for c in range(n):
                    if c < i and c != ind:
                        DrawRect(firstx, firsty, massive[c], "yellow")
                    elif c == i or c == ind:
                        DrawRect(firstx, firsty, massive[c], "blue")
                    else:
                        DrawRect(firstx, firsty, massive[c], "green")
                    firstx += 15
                canva.after(500, canva.update())
        DrawNewMas(firstxx)
        canva.after(500, canva.update())
        lbl2.configure(text="Sorted!")



def click():
    global massive, canva
    massive=[]
    n = scale.get()
    canva.destroy()
    canva = Canvas(window, width=15 * scale.get(), height=460, background='white')
    canva.grid(column=4, row=4)

    for i in range(n):
        massive.append(random.randint(1, 450))
    firstx = firstxx
    canva.delete(ALL)
    for i in range(n):
        DrawRect(firstx, firsty, massive[i], "green")
        firstx += 15

    lbl2.configure(text=massive)


window = Tk()
window.title("SortAlgo")
window.geometry('1600x1600')
selected = IntVar()

scale = Scale(window, from_= 1, to=50, orient= HORIZONTAL)
rad1 = Radiobutton(window, text='BubbleSort', value=1, variable=selected)
rad2 = Radiobutton(window, text='ShakerSort', value=2, variable=selected)
rad3 = Radiobutton(window, text='CombSort', value=3, variable=selected)
rad4 = Radiobutton(window, text='InsertSort', value=4, variable=selected)
rad5 = Radiobutton(window, text='ChooseSort', value=5, variable=selected)

btn = Button(window, text="Выбрать", command=clicked)
btn2 = Button(window, text="Создать массив", command=click)

lbl = Label(window)
lbl2 = Label(window)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
rad4.grid(column=0, row=1)
rad5.grid(column=1, row=1)
scale.grid(column=4, row=2)
btn.grid(column=3, row=0)
btn2.grid(column=4, row=0)
lbl.grid(column=0, row=2)
lbl2.grid(column=4, row=1)

canva = Canvas(window, width=15 * scale.get(), height=460, background='white')
canva.grid(column=4, row=4)
window.mainloop()