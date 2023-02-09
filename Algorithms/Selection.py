def selection(arr, popN):
    del arr[popN:len(arr)]
    fractionsOfTotal = []
    for e in arr:
        fractionsOfTotal.append(1/popN)

    return fractionsOfTotal
