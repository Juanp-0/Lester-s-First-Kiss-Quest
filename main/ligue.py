from random import choice
from personaje import Personaje
import output

def novia_escena():
    import main as _main
    _main.primer_beso = True
    output.escena("novia_escena", nombre=_main.ligue.nombre)

class Ligue(Personaje):
    def __init__(self,nombre,nv_carisma,estado_relacion_xp):
        self.nv_carisma = nv_carisma
        self.nombre = nombre
        self.estado_relacion = ["Nulo", "Interesada", "Amigos", "Quedantes", "Novios"]
        self.estado_relacion_xp = estado_relacion_xp
        self.ligue_aprobacion = ["Like", "Dislike", "Excelente"]
        self.ligue_chance = [True, False]
    
    # Métodos de utilidad
    def mostrar_estado_relacion(self):
        if self.estado_relacion_xp == 0:
            return self.estado_relacion[0]
        elif 1 <= self.estado_relacion_xp < 10:
            return self.estado_relacion[1]
        elif 10 <= self.estado_relacion_xp < 15:
            return self.estado_relacion[2]
        elif 15 <= self.estado_relacion_xp < 20:
            return self.estado_relacion[3]
        else:
            return self.estado_relacion[4]
    
    
    def hablar_ligue(self, personaje):
        if choice(self.ligue_chance):
            aprobacion = choice(self.ligue_aprobacion)
            if aprobacion == "Like":
                self.estado_relacion_xp += 1
                if self.estado_relacion_xp >= 20:
                    output.msg_key("ligue_cita_novia_inicio", nombre=self.nombre)
                    novia_escena()
                else:
                    output.msg_key("ligue_hablar_like", nombre=self.nombre)
            
            elif aprobacion == "Excelente":
                self.estado_relacion_xp += 3
                if self.estado_relacion_xp >= 20:
                    output.msg_key("ligue_cita_novia_inicio", nombre=self.nombre)
                    novia_escena()
                else:
                    output.msg_key("ligue_hablar_excelente", nombre=self.nombre)
            
            else:
                self.estado_relacion_xp -= 1
                if self.estado_relacion_xp == 0:
                    self.tener_ligue = False
                    personaje.nv_carisma -= 2
                    output.msg_key("ligue_hablar_trabo")
                else:
                    output.msg_key("ligue_hablar_dislike", nombre=self.nombre)
        
        else:
            output.msg_key("ligue_hablar_no_disp", nombre=self.nombre)
    
    LUGARES_CITA = {
        "1": {"nombre": "Sandwichería Local", "energia": 30, "dinero": 100},
        "2": {"nombre": "Cafetería",           "energia": 40, "dinero": 200},
        "3": {"nombre": "Buffet Italiano",     "energia": 40, "dinero": 350},
        "4": {"nombre": "Estadio de Fútbol",   "energia": 50, "dinero": 1000},
    }

    def cita(self, personaje, lugar_key):
        lugar = self.LUGARES_CITA[lugar_key]
        energia_req  = lugar["energia"]
        dinero_req   = lugar["dinero"]
        nombre_lugar = lugar["nombre"]

        if personaje.energia < energia_req:
            output.msg_key("ligue_cita_sin_energia")
        elif personaje.dinero < dinero_req:
            output.msg_key("ligue_cita_sin_dinero")
        else:
            output.msg_key("ligue_cita_lugar", nombre_lugar=nombre_lugar)
            personaje.energia -= energia_req
            personaje.dinero  -= dinero_req
            aprobacion = choice(self.ligue_aprobacion)
            if aprobacion == "Like":
                self.estado_relacion_xp += 1
                if self.estado_relacion_xp >= 20:
                    output.msg_key("ligue_cita_novia_inicio", nombre=self.nombre)
                    novia_escena()
                else:
                    output.msg_key("ligue_cita_like", nombre=self.nombre)
            elif aprobacion == "Excelente":
                self.estado_relacion_xp += 3
                if self.estado_relacion_xp >= 20:
                    output.msg_key("ligue_cita_novia_inicio", nombre=self.nombre)
                    novia_escena()
                else:
                    output.msg_key("ligue_cita_excelente", nombre=self.nombre)
            else:
                self.estado_relacion_xp -= 1
                if self.estado_relacion_xp == 0:
                    self.tener_ligue = False
                    personaje.nv_carisma -= 2
                    output.msg_key("ligue_hablar_trabo")
                else:
                    output.msg_key("ligue_cita_dislike", nombre=self.nombre)
            output.msg_key("ligue_cita_regreso")