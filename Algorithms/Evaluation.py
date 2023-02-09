def evaluation(array, value, weight, knapsackSize):
    for e in array:
        e.calculate_weight(weight)
        if (e.weight > knapsackSize):
            e.calculateQuadraticValue(value)
            e.setValue(-1*e.value)
        else:
            e.calculateQuadraticValue(value)


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


def partition(array, low, high):
    pivot = array[high].value
    i = low - 1
    for j in range(low, high):
        if array[j].value >= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1
