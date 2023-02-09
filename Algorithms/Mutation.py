import random


def multiBitMutation(array, p_mut):
    if array:
        n = array[0].size
        for e in array:
            for j in range(0, n):
                if (random.uniform(0, 1) <= p_mut):
                    A = e.getRep()
                    if (A[j] == 0):
                        A[j] = 1
                    else:
                        A[j] = 0
                    e.setRep(A)
