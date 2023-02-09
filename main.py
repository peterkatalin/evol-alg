import numpy as np;
import random;
from egyed import *;
import matplotlib.pyplot as plt;
from szelekciok import *;
from ertekeles import *;
from mutaciok import *;
from keresztezodes import *;


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


#  Inicializaljuk a parametereket
def get_parameters():
    n_pop=10                                                            #populacio merete
    p_cross = 0.8                                                       #keresztezodesek valoszinusege
    p_mut = 0.10                                                        #mutaciok valoszinusege
    gen = 50                                                            #geineracok szama
    select = int(n_pop / 2)                                             #hany elemet valasztunk szulonek (elso szelekcional)
    return [ n_pop, p_cross, p_mut, gen, select ]                         



# a populacio inicializalasa
# populacio = lista ami egyedekbol all
def init_population(n,n_pop,ertekek,sulyok):
    lista=[]
    for j in range(n_pop):
        kromoszoma=[]
        for i in range (n):         
            kromoszoma.append(random.randint(0,1))
        e=egyed(n,kromoszoma)
        e.calculate_value(ertekek)
        e.calculate_weight(sulyok)
        lista.append(e)
    return lista



def genetikus_algoritmus(chroms ,gen, taska_meret, ertekek, sulyok, n_pop, select, p_cross, p_mut):
    
    ertekeles(chroms,ertekek,sulyok,taska_meret)
    quickSort(chroms,0,n_pop-1)
    legjobb_egyed=egyed(chroms[0].size, chroms[0].rep, chroms[0].value, chroms[0].weight)
    best=[]
    for i in range(gen):
        parent_probability=szelekcio(chroms,n_pop)
        #keresztezodes_uniformalis(chroms,select,p_cross,n_pop,parent_probability,7)
        keresztezodes_n(chroms,select,p_cross,n_pop,parent_probability,50)
        mutacio2(chroms[n_pop:],p_mut)
        ertekeles(chroms,ertekek,sulyok,taska_meret)
        quickSort(chroms,0,len(chroms)-1)
        if(chroms[0].value > legjobb_egyed.value):
            legjobb_egyed.setRep(chroms[0].rep)
            legjobb_egyed.setValue(chroms[0].value)
            legjobb_egyed.setWeight(chroms[0].weight)
        print("Az "+str(i)+". generacioban a legjobb megoldas: "+ str(legjobb_egyed.getRep()))
        print(legjobb_egyed)
        best.append(legjobb_egyed.getValue())
        
    
    parent_probability=szelekcio_random(chroms,n_pop)
    last_generation_values=[]
    for ch in chroms:
        last_generation_values.append(ch.getValue())
    return [best,last_generation_values]


[ taska_meret, ertekek, sulyok, n ] = beolvas_tesztallomany()
[ n_pop, p_cross, p_mut, gen, select ] = get_parameters()

#ha tobbszor lefuttassuk a programot
data=[]
best_results=[]
for i in range(0,10):
    population = init_population(n,n_pop,ertekek,sulyok)
    [best,last_generation_values]=genetikus_algoritmus(population ,gen, taska_meret, ertekek, sulyok, n_pop,select,p_cross,p_mut)
    data.append(last_generation_values)
    best_results.append(best[gen-1])

fig,ax = plt.subplots()
ax.set_title("Last population of all iterations")
ax.set_xlabel("Iteration")
ax.set_ylabel("Value")
bp = ax.boxplot(data)

generations=range(1,51)
fig2,ax2=plt.subplots()
ax2.set_title("Evolution of best value in 50 generation")
ax2.set_xlabel("Generation")
ax2.set_ylabel("Value")
sc=ax2.scatter(generations,best)

iteations=range(1,11)
fig3,ax3=plt.subplots()
ax3.set_title("Best values in all iterations")
ax3.set_ylabel("Value")
pl=ax3.boxplot(best_results)

it=10
with open('best_result.txt', 'w') as f:
    f.writelines("nr of objects: %d\n" %n)
    f.writelines("Knapsack capacity: %d\n" %taska_meret)
    f.writelines("the best results in the %d iteration : \n" %it)
    for b in best_results:
        f.writelines("%d "%b)
f.close()

fig.savefig('GA_KP1.png')
fig2.savefig('GA_KP2.png')
fig3.savefig('GA_KP3.png')

plt.show()