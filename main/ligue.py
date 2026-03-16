from random import choice
from escenas import novia_escena
from personaje import Personaje

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
    
    def getDatos(self):
        print(f"\nDatos de tu ligue:\nNombre: {self.nombre}\nNv. de Carisma: {self.nv_carisma}")
        self.mostrar_estado_relacion()
    
    def hablar_ligue(self, tener_ligue, personaje):
        if choice(self.ligue_chance):
            aprobacion = choice(self.ligue_aprobacion)
            if aprobacion == "Like":
                self.estado_relacion_xp += 1
                if self.estado_relacion_xp >= 20:
                    print(f"\nCitas a {self.nombre} al lugar donde se conocieron\n")
                    novia_escena()
                else:
                    print(f"\nParece ser que {self.nombre} ha disfrutado de la charla\n")
            
            elif aprobacion == "Excelente":
                self.estado_relacion_xp += 3
                if self.estado_relacion_xp >= 20:
                    print(f"\nCitas a {self.nombre} al lugar donde se conocieron\n")
                    novia_escena()
                else:
                    print(f"\nParece ser que {self.nombre} ha disfrutado muchisimo de la charla\n")
            
            else:
                self.estado_relacion_xp -= 1
                if self.estado_relacion_xp == 0:
                    self.tener_ligue = False
                    personaje.nv_carisma -= 2
                    print("\nHiciste que tu ligue perdiera todo interes en tí\n")
                else:
                    print(f"\nParece ser que {self.nombre} no ha disfrutado de la charla\n")
        
        else:
            print(f"\nParece ser que {self.nombre} no esta disponible\n")
    
    def cita(self, personaje):
        print(f"\nHas decidido salir con {self.nombre}\n")
        print("Lugares para tener una cita:")
        print("1.- Sandwichería Local (-30 de Energía, -100 de Dinero)")
        print("2.- Cafetería (-40 de Energía, -200 de Dinero)")
        print("3.- Buffet Italiano (-40 de Energía, -350 de Dinero)")
        print("4.- Estadio de Fútbol (-50 de Energía, -1000 de Dinero)\n")
        
        lugares = {
            "1": {"nombre": "Sandwichería Local", "energia": 30, "dinero": 100},
            "2": {"nombre": "Cafetería", "energia": 40, "dinero": 200},
            "3": {"nombre": "Buffet Italiano", "energia": 40, "dinero": 350},
            "4": {"nombre": "Estadio de Fútbol", "energia": 50, "dinero": 1000},
        }
        
        while True:
            cita_desicion = input("Selecciona un lugar para tener una cita o Escribe S para salir\n")

            match cita_desicion:
                case "1" | "2" | "3" | "4":
                    lugar = lugares[cita_desicion]
                    energia_req = lugar["energia"]
                    dinero_req = lugar["dinero"]
                    nombre_lugar = lugar["nombre"]
                    
                    if personaje.energia < energia_req: 
                        print("\nNo tienes ganas de salir hoy\n")
                    elif personaje.dinero < dinero_req: 
                        print("\nNo te alcanza\n")
                    else:
                        print(f"\nHas decidido ir a {nombre_lugar}\n")
                        
                        aprobacion = choice(self.ligue_aprobacion)
                        if aprobacion == "Like":
                            self.estado_relacion_xp += 1
                            if self.estado_relacion_xp >= 20:
                                novia_escena(self)
                            else:
                                print(f"\nParece ser que {self.nombre} ha disfrutado la cita\n")
                        
                        elif aprobacion == "Excelente":
                            self.estado_relacion_xp += 3
                            if self.estado_relacion_xp >= 20:
                                novia_escena(self)
                            else:
                                print(f"\nParece ser que {self.nombre} ha disfrutado muchísimo la cita\n")
                        
                        else:
                            self.estado_relacion_xp -= 1
                            if self.estado_relacion_xp == 0:
                                self.tener_ligue = False
                                personaje.nv_carisma -= 2
                                print("\nHiciste que tu ligue perdiera todo interés en ti\n")
                                
                            else:
                                print(f"\nParece ser que {self.nombre} no ha disfrutado la cita\n")
                        
                        print(f"\nRegresas a casa después de salir con tu ligue\n")
                        break
                
                case "S" | "s":
                    break
                
                case _:
                    print("Selecciona una opción válida\n")

    
    def ligueMenu(self, personaje):
        hablar_ligue_usado = False
        while True:
            ligue_menu = input(f"\nSelecciona lo que quieres hacer con {self.nombre}:\n1.- Hablar con {self.nombre} (Solo una vez por Día)\n2.- Tener una cita con {self.nombre}\n3.- Volver al Hub\n")
            
            match ligue_menu:
                case "1":
                    if not hablar_ligue_usado:
                        self.hablar_ligue(True, personaje)
                        hablar_ligue_usado = True
                    elif self.estado_relacion_xp >= 20:
                        print(f"\nYa eres novio de {self.nombre}, ya la conoces bien\n")
                    else:
                        print(f"\nParece ser que ya has hablado con {self.nombre}\n")
                
                case "2":
                    if self.estado_relacion_xp >= 20:
                        print(f"\nYa eres novio de {self.nombre}, ya la conoces bien\n")
                    else:
                        self.cita(personaje)
            
                case "3":
                    break
                
                case _:
                    print("Selecciona una opción valida\n")