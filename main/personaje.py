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
            output.msg_key("trabajar_ok")
        else:
            output.msg_key("trabajar_sin_energia")
    
    def dormir(self, dias):
        global hablar_ligue_uso, hablar_uso
        dias += 1
        self.energia = 100
        hablar_uso = False
        hablar_ligue_uso = False
        return dias
    
    def hablar(self, dax_chance, hablar_uso, dax_disponible):
        if self.nv_carisma >= 10:
            output.msg_key("carisma_maximo")
        elif hablar_uso == False:
            resultado = choice(dax_chance)
            if resultado:
                self.nv_carisma += 1
                output.msg_key("dax_consejos")
                dax_disponible = True
            else:
                output.msg_key("dax_no_disponible")
                dax_disponible = False
            hablar_uso = True
        elif hablar_uso == True:
            if dax_disponible:
                output.msg_key("dax_ya_hablaste")
            else:
                output.msg_key("dax_no_disponible")
        
        return hablar_uso, dax_disponible
    
    def salir(self, primer_beso):
        """Verifica condiciones para salir de fiesta. Retorna True si puede."""
        if self.energia >= 30 and self.dinero >= 20:
            self.energia -= 30
            self.dinero -= 20
            output.msg_key("salir_inicio")
            output.msg_key("salir_chicas")
            return True
        elif self.dinero < 20:
            output.msg_key("salir_sin_dinero")
            return False
        elif self.energia < 30:
            output.msg_key("salir_sin_energia")
            return False
        else:
            output.msg_key("salir_regreso")
            return False