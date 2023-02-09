import random;
from egyed import *;
import math;



def keresztezodes_n(arr,select,p_cross,n_pop,parent_probability,vagasok_szama):
    n=arr[0].getSize()
    for i in range(select):
        if (random.uniform(0,1) <= p_cross):
            
            # kivalasztjuk hogy melyik egyedek keresztezodnek 
            i1=0
            nr=random.uniform(0,1)
            proportion=0.0
            while(i1 < n_pop):
                proportion=proportion+parent_probability[i1]
                if( nr <= proportion):
                    break
                i1=i1+1
            
            i2=i1
            while(i2==i1):
                i2=0
                nr=random.uniform(0,1)
                proportion=0
                
                while(i2 < n_pop):
                    proportion=proportion+parent_probability[i2]
                    if(nr <= proportion):
                        break
                    i2=i2+1
                
                if(i1 == i2):
                    # print("i1 = {}\ni2 = {}".format(i1,i2))
                    if(i1 == n_pop-1):
                        i2=i2-1
                    else:
                        i2=i2+1
                    
                    
    

            

            #n vagasu ekresztezodes
            crossovers=set()
            times = vagasok_szama

            #generaljuk a vagaspontokat
            for i in range(times):
                crossover_index=random.randint(1,n-2)
                while(crossover_index in crossovers):
                    crossover_index=random.randint(1,n-2)
                crossovers.add(crossover_index)

            #rendezzuk a vagaspontokat
            crossovers=list(sorted(crossovers))
            
            A=arr[i1].getRep()
            B=arr[i2].getRep()
            C=[]
            D=[]
            parity=0
            crossover_index=crossovers[parity]
            for j in range(n):
                if((parity % 2) == 0):
                    if(j< crossover_index):
                        C.append(A[j])
                        D.append(B[j])
                    else:
                        if (j == crossover_index):
                            C.append(A[j])
                            D.append(B[j])
                            parity=parity+1
                            if(parity < times):
                                crossover_index=crossovers[parity]
                        else:
                            C.append(A[j])
                            D.append(B[j])
                else:
                    if(j< crossover_index):
                        C.append(B[j])
                        D.append(A[j])
                    else:
                        if (j == crossover_index):
                            C.append(B[j])
                            D.append(A[j])
                            parity=parity+1
                            if(parity < times):
                                crossover_index=crossovers[parity]
                        else:
                            C.append(B[j])
                            D.append(A[j])

            #uj gyerekek letrehozasa 
            gyerek1=egyed(n,C)
            gyerek2=egyed(n,D)
            arr.append(gyerek1)
            arr.append(gyerek2)







def keresztezodes_uniformalis(arr,select,p_cross,n_pop,parent_probability,vagasok_szama):
    n=arr[0].getSize()
    for i in range(select):
        if (random.uniform(0,1) <= p_cross):
            # kivalasztjuk hogy melyik egyedek keresztezodnek 
            i1=0
            nr=random.uniform(0,1)
            proportion=0
            while(i1 < n_pop):
                proportion=proportion+parent_probability[i1]
                if(nr <= proportion):
                    break
                i1=i1+1
            
            i2=i1
            while(i2==i1):
                i2=0
                nr=random.uniform(0,1)
                proportion=0
                
                while(i2 < n_pop):
                    proportion=proportion+parent_probability[i2]
                    if(nr <= proportion):
                        break
                    i2=i2+1
                
                if(i1 == i2):
                    # print("i1 = {}\ni2 = {}".format(i1,i2))
                    if(i1 == n_pop-1):
                        i2=i2-1
                    else:
                        i2=i2+1
            
            #generalunk egy szamot 0 es 1 kozott
            #ha kisebb mint 0.5, akkor nem valtoztatunk az allelen,
            #ha nagyobb akkor felcserejuk
            A=arr[i1].getRep()
            B=arr[i2].getRep()
            C=[]
            D=[]

            for j in range(n):
                posibility = random.uniform(0,1)
                if (posibility <= 0.5):
                    C.append(A[j])
                    D.append(B[j])
                else:
                    C.append(B[j])
                    D.append(A[j])
            
            #uj gyerekek letrehozasa 
            gyerek1=egyed(n,C)
            gyerek2=egyed(n,D)
            arr.append(gyerek1)
            arr.append(gyerek2)



                