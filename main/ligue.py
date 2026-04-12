from random import choice
from personaje import Personaje
import output

def novia_escena():
    import main as _main
    _main.primer_beso = True
    output.msg(f"\u00a1Felicidades! {_main.ligue.nombre} es ahora tu novia")
    try:
        import gui as _gui
        _gui.iniciar_escena("novia_escena")
    except Exception:
        pass

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
                    output.msg(f"Citas a {self.nombre} al lugar donde se conocieron")
                    novia_escena()
                else:
                    output.msg(f"Parece ser que {self.nombre} ha disfrutado de la charla")
            
            elif aprobacion == "Excelente":
                self.estado_relacion_xp += 3
                if self.estado_relacion_xp >= 20:
                    output.msg(f"Citas a {self.nombre} al lugar donde se conocieron")
                    novia_escena()
                else:
                    output.msg(f"Parece ser que {self.nombre} ha disfrutado muchisimo de la charla")
            
            else:
                self.estado_relacion_xp -= 1
                if self.estado_relacion_xp == 0:
                    self.tener_ligue = False
                    personaje.nv_carisma -= 2
                    output.msg("Hiciste que tu ligue perdiera todo interes en tí")
                else:
                    output.msg(f"Parece ser que {self.nombre} no ha disfrutado de la charla")
        
        else:
            output.msg(f"Parece ser que {self.nombre} no esta disponible")
    
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
            output.msg("No tienes ganas de salir hoy")
        elif personaje.dinero < dinero_req:
            output.msg("No te alcanza")
        else:
            output.msg(f"Has decidido ir a {nombre_lugar}")
            aprobacion = choice(self.ligue_aprobacion)
            if aprobacion == "Like":
                self.estado_relacion_xp += 1
                if self.estado_relacion_xp >= 20:
                    novia_escena()
                else:
                    output.msg(f"Parece ser que {self.nombre} ha disfrutado la cita")
            elif aprobacion == "Excelente":
                self.estado_relacion_xp += 3
                if self.estado_relacion_xp >= 20:
                    novia_escena()
                else:
                    output.msg(f"Parece ser que {self.nombre} ha disfrutado muchísimo la cita")
            else:
                self.estado_relacion_xp -= 1
                if self.estado_relacion_xp == 0:
                    self.tener_ligue = False
                    personaje.nv_carisma -= 2
                    output.msg("Hiciste que tu ligue perdiera todo interés en ti")
                else:
                    output.msg(f"Parece ser que {self.nombre} no ha disfrutado la cita")
            output.msg("Regresas a casa después de salir con tu ligue")