import random
import Bubble
import Insert
import Complicated

massive = []
print("Input n =", end=" ")
#n = int(input())
n = 7
for i in range(n):
    massive.append(random.randint(1, 11212))
firstmas = massive
print(massive)
#print("Massive after bubble")
#print(Bubble.BubbleSort(massive, n))
print("Massive after QuickSort")
print(Complicated.QuickSort(massive))