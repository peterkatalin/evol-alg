



#csak az elso 10 egyed marad meg, a tobbit toroljuk
#valamint ki kell valasszuk a 10 egyed kozul, kik azok akik a kovetkezo generacio szulei lesznek, a Roulette Wheel segitsegevel
def szelekcio(arr,n_pop):
    del arr[n_pop:len(arr)]


    #A Roulette Wheel-hez kellenek a parent valoszinusegek
    #(mekkora a valoszinusege hogy egy chromoszoma szulo legyen, attol fuggoen hogy milyen jo a fitneszje)
    fractions_of_total=[]
    fitness_sum=0
    for e in arr:
        fitness_sum=fitness_sum+ e.getValue()
    
    for e in arr:
        fractions_of_total.append(e.getValue()/fitness_sum)

    return fractions_of_total




#csak az elso 10 egyed marad meg, a tobbit toroljuk
#veletlenszeruen valasszuk ki, hogy melyik egyedek lesznek a kovetkezo szulok
def szelekcio_random(arr,n_pop):
    del arr[n_pop:len(arr)]
    fractions_of_total=[]
    for e in arr:
        fractions_of_total.append(1/n_pop)
    
    return fractions_of_total





    