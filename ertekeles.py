def ertekeles(arr,ert,suly,taska_m):
    for e in arr:
        e.calculate_weight(suly)                                            #ha tul nagy a betett targyak osszege, az adott egyed erteket negativva tesszuk
        if(e.weight > taska_m):
            e.calculate_value(ert)
            e.setValue(-1*e.value)
        else:
            e.calculate_value(ert)
    


#sorbarendezzuk a populaciot ertek szerint (value). Ez a szelekciohoz segit
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