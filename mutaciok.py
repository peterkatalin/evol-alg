import random;

#egyetlen egy bittet cserelunk fel,veletlenszeruen
def mutacio(arr,p_mut):
    n=arr[0].size
    for e in arr:
        if(random.uniform(0,1) <= p_mut):
            flip_bit_index=random.randint(0,n-1)
            A=e.getRep()
            if(A[flip_bit_index]==0):
                A[flip_bit_index]=1
            else:
                A[flip_bit_index]=0
            e.setRep(A)

#sorbamegyunk bittenkent es ha teljesul a p_mut, akkor felcsereljuk. Igy tobb bit is mutalodhat
def mutacio2(arr,p_mut):
    n=arr[0].size
    for e in arr:
        for j in range(0,n):
            if(random.uniform(0,1) <= p_mut):
                A=e.getRep()
                if(A[j]==0):
                    A[j]=1
                else:
                    A[j]=0
                e.setRep(A)