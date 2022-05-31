def QuickSort(massive):
    n = len(massive)
    if n <= 1:
        return massive
    first = n // 2
    element = massive[first]
    left = []
    right = []
    center = [element]
    for i in range(n):
        if massive[i] <= element and i != first:
            left.append(massive[i])
        elif massive[i] >= element and i != first:
            right.append(massive[i])
    return QuickSort(left) + center + QuickSort(right)