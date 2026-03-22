from random import choice

class Personaje:
    def __init__(self, energia, dinero, nv_carisma):
        self.energia = energia
        self.dinero = dinero
        self.nv_carisma = nv_carisma

    
    #Acciones
    def sumEnergia(self, cantidad):
        if self.energia + cantidad > 100:
            self.energia = 100
        self.energia += cantidad

    def trabajar(self):
        if self.energia >= 50:
            self.energia -= 50
            self.dinero += 50
            print("\nRegresas a Casa, despues de un arduo día de trabajo\n")
        else:
            print ("\nNo tienes ganas de ir a Trabajar\n")
    
    def dormir(self, dias):
        global hablar_ligue_uso, hablar_uso
        dias += 1
        self.energia = 100
        hablar_uso = False
        hablar_ligue_uso = False
        return dias
    
    def hablar(self, dax_chance, hablar_uso, dax_disponible):
        if self.nv_carisma >= 10:
            print("\nHas llegado al maximo nivel de carisma\n")
        elif hablar_uso == False:
            resultado = choice(dax_chance)
            if resultado:
                sleep(1)
                self.nv_carisma += 1
                print("\nDax te da unos buenos consejos para aumentar tu carisma\n")
                sleep(1)
                dax_disponible = True
            else:
                sleep(1)
                print("\nParece ser que Dax no esta disponible\n")
                sleep(1)
                dax_disponible = False
            hablar_uso = True
        elif hablar_uso == True:
            if dax_disponible:
                print("\nParece ser que ya has hablado con Dax\n")
            else:
                print("\nParece ser que Dax no esta disponible\n")
        
        return hablar_uso, dax_disponible
    
    def salir(self, primer_beso):
        if self.energia >= 30 and self.dinero >= 20:
            from fiesta import chicas
            self.energia -= 30
            self.dinero -= 20
            print("\nTe escapas a escondidas de tu casa\nTomas el metro para llegar al centro de la ciudad\nEntras a la primera discoteca que ves\n")
            print("La estas pasando excelente\nParece que se acercan unas chicas interesadas en ti\nEs hora de usar tus habilidades de carisma\n")
            chicas(self)
            if primer_beso == True:
                self.dormir()
        elif self.dinero < 20:
            print("\nNo tienes dinero para Salir de fiesta\n")
        elif self.energia < 30:
            print("\nNo tienes ganas de Salir de fiesta\n")
        else:
            print("Regresas a Casa de manera silenciosa, despues de una noche de locura\n")





    
    
        