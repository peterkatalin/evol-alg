import numpy as py;

class egyed:
    
    def __init__(self,size=0,rep=[],value=0,weight=0):
        self.size=size
        self.rep=rep
        self.value=value
        self.weight=weight
    
    def setSize(self,s):
        self.size=s
    
    def setRep(self,r):
        if(len(r)== self.size):
            self.rep=r
    
    def setValue(self,v):
        self.value=v
    
    def setWeight(self,w):
        self.weight=w
    
    def calculate_value(self,arr):
        if(self.size == len(arr)):
            aux=0
            for i in range(len(arr)):
                aux=aux + (self.rep[i] * arr[i])
            
            self.value=aux
    
    def calculate_weight(self,arr):
        if(self.size == len(arr)):
            aux=0
            for i in range(len(arr)):
                aux=aux + (self.rep[i] * arr[i])
            
            self.weight=aux
    
    def getSize(self):
        return self.size
    
    def getRep(self):
        return self.rep

    def getValue(self):
        return self.value
    
    def getWeight(self):
        return self.weight

    def __str__(self):
        return "value: "+str(self.value) + " , weight:"+str(self.weight)