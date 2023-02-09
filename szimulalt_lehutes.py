import numpy as np;
import random;
from egyed import *;
import matplotlib.pyplot as plt;
import math;
import matplotlib.pyplot as plt;


# beolvassuk a tesztallomanyokat
def beolvas_tesztallomany(): 
    f=open("knap.txt","r")
    taska_meret =int(f.read())                                           
    f.close()

    f=open("values.txt","r")
    ertekek = f.read().split()
    ertekek = [int(x) for x in ertekek]
    f.close()

    f=open("weights.txt", "r")
    sulyok = f.read().split()
    sulyok = [int(x) for x in sulyok]
    f.close()

    n=len(sulyok)

    return [ taska_meret, ertekek, sulyok, n ]


#inicializaljuk a parametereket
def get_parameters():
    T0=1000
    iter_max=1000
    alpha=0.99
    return [ T0 ,iter_max,alpha ]                         



def szimulalt_lehutes(n,iter_max,ertekek,sulyok,taska_meret,T,alpha):
    chromosome=np.zeros(n,int)
    X = egyed(n,chromosome)
    BestX=egyed(n,X.getRep())
    all_best_values=[]
    all_X_values=[]
    for i in range(1,iter_max):
        j = random.randint(0,n-1)
        
        array=X.getRep()
        if(array[j]==1):
            array[j]=0
        else:
            array[j]=1
        Y = egyed(n,array)
        Y.calculate_value(ertekek)
        Y.calculate_weight(sulyok)
        if(Y.getWeight() <= taska_meret):                                                               #ha ez a megoldas megfelelo
            if(Y.getValue() > X.getValue()):                                                            #ha ez a megoldas jobb mint az eddigi aktualis X akkor ez lesz az uj X
                X.setRep(Y.getRep())
                X.setValue(Y.getValue())
                X.setWeight(Y.getWeight())

                if(X.getValue() > BestX.getValue()):                                                    #Ha legjobb megoldasnal is jobb akkor legjobb megoldaskent is elmentjuk
                    BestX.setRep(X.getRep())
                    BestX.setValue(X.getValue())
                    BestX.setWeight(X.getWeight())
            else:                                                                                       #Ha roszabb mint az X, akkor "lehutjuk " az X-et ha teljesul a P valoszinuseg
                r=random.uniform(0,1)
                if(r < math.exp((Y.getValue()-X.getValue())/T )):
                    X.setRep(Y.getRep())
                    X.setValue(Y.getValue())
                    X.setWeight(Y.getWeight())
        all_X_values.append(X.getValue())
        all_best_values.append(BestX.getValue())
        T=alpha*T
    
    return [BestX.getValue(), BestX.getWeight(), BestX.getRep(),all_best_values, all_X_values]


taska_meret, ertekek, sulyok,n=beolvas_tesztallomany()
best_values=[]
best_weights=[]


for i in range(0,10):
    T,iter_max,alpha =  get_parameters()
    V,W,R,A,AX =szimulalt_lehutes(n,iter_max,ertekek,sulyok,taska_meret,T,alpha)
    best_values.append(float(V))
    best_weights.append(W)


fig,ax = plt.subplots()
iterations=range(0,10)
sc = ax.plot(iterations,best_values)
ax.set_title("The final results in all iterations")

fig2,ax2=plt.subplots()
iterations2=range(1,iter_max)
sc2= ax2.scatter(iterations2,A)
ax2.set_title("The best values in the 10th iteration")

fig3,ax3=plt.subplots()
iterations2=range(1,iter_max)
sc3= ax3.plot(iterations2,AX)
ax3.set_title("All values of the variable in the 10th iteration")


it=10
with open('best_result.txt', 'w') as f:
    f.writelines("nr of objects: %d\n" %n)
    f.writelines("Knapsack capacity: %d\n" %taska_meret)
    f.writelines("the best results in the %d iteration : \n" %it)
    for b in best_values:
        f.writelines("%d "%b)

f.close()


fig.savefig('SA_KP1.png')
fig2.savefig('SA_KP2.png')
fig3.savefig('SA_KP3.png')

plt.show()
