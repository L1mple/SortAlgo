def InsertSort (massive, n):
    number = 1
    for i in range (1, n):
        if massive[i] < massive[i - 1]:
            swap = massive[i]
            massive[i] = massive[i - 1]
            massive[i - 1] = swap
            print("After swap", massive)
        for j in range (number - 1, 0, -1):
            if massive[j] < massive[j - 1]:
                swap = massive[j]
                massive[j] = massive[j - 1]
                massive[j - 1] = swap
                print("After swap", massive)
        number += 1
    return massive
def ChooseSort (massive,n):
    for i in range(n):
        ind = massive.index(min(massive[i:n]))
        if ind != i:
            swap = massive[i]
            massive[i] = massive[ind]
            massive[ind] = swap


    return massive