from time import sleep
from random import shuffle

class Personaje:
    def __init__(self, energia, dinero, nv_carisma):
        self.energia = energia
        self.dinero = dinero
        self.nv_carisma = nv_carisma

    #Getters y Setters
    def getEnergia(self):
        return self.energia
        
    def setEnergia(self, energia):
        self.energia = energia
        
    def getDinero(self):
        return self.dinero
        
    def setDinero(self, dinero):
        self.dinero = dinero
        
    def getNvCarisma(self):
        return self.nv_carisma
        
    def setNvCarisma(self, nv_carisma):
        self.nv_carisma = nv_carisma
    
    #Operadores
    def sumEnergia(self, cant):
        self.setEnergia(self.energia + cant)
    
    def resEnergia(self, cant):
        self.setEnergia(self.energia - cant)
    
    def sumDinero(self, cant):
        self.setDinero(self.dinero + cant)
    
    def resDinero(self, cant):
        self.setDinero(self.dinero - cant)
    
    def sumNvCarisma(self, cant):
        self.setNvCarisma(self.nv_carisma + cant)
    
    def resNvCarisma(self, cant):
        self.setNvCarisma(self.nv_carisma - cant)
    
        #Acciones
    def trabajar(self):
        if self.energia >= 50:
            self.resEnergia(50)
            self.sumDinero(50)
            sleep(1)
            print("\nRegresas a Casa, despues de un arduo día de trabajo\n")
            sleep(1)
        else:
            print ("\nNo tienes ganas de ir a Trabajar\n")
    
    def dormir(self):
        global dias, hablar_ligue_uso, hablar_uso
        sleep(1)
        dias += 1
        self.setEnergia(100)
        hablar_uso = False
        hablar_ligue_uso = False
    
    def hablar(self, dax_chance):
        global hablar_uso
        shuffle(dax_chance)
        if dax_chance[0] == True:
            sleep(1)
            self.sumNvCarisma(1)
            print("\nDax te da unos buenos consejos para aumentar tu carisma\n")
            sleep(1)
        else:
            sleep(1)
            print ("\nParece ser que Dax no esta disponible\n")





    
    
        