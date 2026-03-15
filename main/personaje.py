from time import sleep
from random import choice

class Personaje:
    def __init__(self, energia, dinero, nv_carisma):
        self.energia = energia
        self.dinero = dinero
        self.nv_carisma = nv_carisma
    
    #Acciones
    def trabajar(self):
        if self.energia >= 50:
            self.energia -= 50
            self.dinero += 50
            sleep(1)
            print("\nRegresas a Casa, despues de un arduo día de trabajo\n")
            sleep(1)
        else:
            print ("\nNo tienes ganas de ir a Trabajar\n")
    
    def dormir(self):
        global dias, hablar_ligue_uso, hablar_uso
        sleep(1)
        dias += 1
        self.energia = 100
        hablar_uso = False
        hablar_ligue_uso = False
    
    def hablar(self, dax_chance):
        global hablar_uso
        if choice(dax_chance):
            sleep(1)
            self.nv_carisma += 1
            print("\nDax te da unos buenos consejos para aumentar tu carisma\n")
            sleep(1)
        else:
            sleep(1)
            print ("\nParece ser que Dax no esta disponible\n")
    
    def salir(self):
        global primer_beso
        if self.energia >= 30 and self.dinero >= 20:
            self.resEnergia(30)
            self.resDinero(20)
            print("\nTe escapas a escondidas de tu casa\nTomas el metro para llegar al centro de la ciudad\nEntras a la primera discoteca que ves\n")
            sleep(1)
            print("La estas pasando excelente\nParece que se acercan unas chicas interesadas en ti\nEs hora de usar tus habilidades de carisma\n")
            #chicas()
            if primer_beso == True:
                sleep(1)
                self.dormir()
        elif self.dinero < 20:
            print("\nNo tienes dinero para Salir de fiesta\n")
        elif self.energia < 30:
            print("\nNo tienes ganas de Salir de fiesta\n")
        else:
            sleep(1)
            print("Regresas a Casa de manera silenciosa, despues de una noche de locura\n")
            sleep(1)





    
    
        