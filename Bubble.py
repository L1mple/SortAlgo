from tkinter import *
from tkinter.ttk import Radiobutton
import random
def BubbleSort (massive, n):
    for i in range(n):
        for j in range(i + 1, n):
            if massive[i] > massive[j]:
                swap = massive[i]
                massive[i] = massive[j]
                massive[j] = swap

def ShakerSort (massive, n):
    left = 1
    right = n - 1
    while left != right:
        for i in range(left-1, right):
            if massive[i] > massive[i + 1]:
                swap = massive[i]
                massive[i] = massive[i + 1]
                massive[i + 1] = swap
                print("After LEFT", massive)
        right -= 1

        for j in range(right+1,left-1,-1):
            if massive[j] < massive[j - 1]:
                swap = massive[j]
                massive[j] = massive[j - 1]
                massive[j - 1] = swap
                print("After RIGTH", massive)
        left += 1

    return massive
def CombSort (massive, n):
    factor = 1.247
    step = int(n // factor)
    while step >= 2:
        for i in range(n - step +1 ):
            if massive[i] > massive[i + step - 1]:
                swap = massive[i]
                massive[i] = massive[i + step - 1]
                massive[i + step - 1] = swap
            print("After RIGTH", massive)
        step = int(step // factor)
    return massive