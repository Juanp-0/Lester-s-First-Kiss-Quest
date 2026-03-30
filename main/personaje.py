from random import choice
import output

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
            output.msg("Regresas a Casa, despues de un arduo día de trabajo")
        else:
            output.msg("No tienes ganas de ir a Trabajar")
    
    def dormir(self, dias):
        global hablar_ligue_uso, hablar_uso
        dias += 1
        self.energia = 100
        hablar_uso = False
        hablar_ligue_uso = False
        return dias
    
    def hablar(self, dax_chance, hablar_uso, dax_disponible):
        if self.nv_carisma >= 10:
            output.msg("Has llegado al maximo nivel de carisma")
        elif hablar_uso == False:
            resultado = choice(dax_chance)
            if resultado:
                self.nv_carisma += 1
                output.msg("Dax te da unos buenos consejos para aumentar tu carisma")
                dax_disponible = True
            else:
                output.msg("Parece ser que Dax no esta disponible")
                dax_disponible = False
            hablar_uso = True
        elif hablar_uso == True:
            if dax_disponible:
                output.msg("Parece ser que ya has hablado con Dax")
            else:
                output.msg("Parece ser que Dax no esta disponible")
        
        return hablar_uso, dax_disponible
    
    def salir(self, primer_beso):
        if self.energia >= 30 and self.dinero >= 20:
            from fiesta import chicas
            self.energia -= 30
            self.dinero -= 20
            output.msg("Te escapas a escondidas de tu casa\nTomas el metro para llegar al centro de la ciudad\nEntras a la primera discoteca que ves")
            output.msg("La estas pasando excelente\nParece que se acercan unas chicas interesadas en ti\nEs hora de usar tus habilidades de carisma")
            chicas(self)
            if primer_beso == True:
                self.dormir()
        elif self.dinero < 20:
            output.msg("No tienes dinero para Salir de fiesta")
        elif self.energia < 30:
            output.msg("No tienes ganas de Salir de fiesta")
        else:
            output.msg("Regresas a Casa de manera silenciosa, despues de una noche de locura")





    
    
        