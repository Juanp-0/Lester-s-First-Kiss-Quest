#Lester's First Kiss Quest

import json
from time import sleep
from personaje import Personaje
import escenas
from ligue import Ligue
from item import Item, EnergItem, CarismaItem
from tienda import Tienda

#Stats
dias = 1

#Factores RNG
dax_chance = [True, False]


#Verificadores
hablar_uso = False
tener_ligue = False
hablar_ligue_uso = False
primer_beso = False
fin_juego = False

tienda = Tienda([EnergItem("Bebida Energetíca", 20, 20), EnergItem("Café Enbotellado", 15, 10), CarismaItem("Perfume", 150, 1)])


#Sistema de Guardado
def newgame():
    global dias, hablar_uso, hablar_ligue_uso, fin_juego, lester, ligue, tener_ligue, primer_beso
    # Inicializar variables globales
    dias = 1
    hablar_uso = False
    hablar_ligue_uso = False
    fin_juego = False
    tener_ligue = False
    primer_beso = False
    
    # Crear nuevo personaje con stats iniciales
    lester = Personaje(100, 0, 0)
    ligue = Ligue(None, 0, 0)

    # Guardar estado inicial
    save_data = {
        "dias": 1,
        "energia": lester.energia,
        "dinero": lester.dinero,
        "nv_carisma": lester.nv_carisma,
        "hablar_uso": False,
        "tener_ligue": False,
        "primer_beso": False,
        "nom_ligue": ligue.nombre,
        "nv_carisma_ligue": ligue.nv_carisma,
        "estado_relacion_xp": ligue.estado_relacion_xp,
        "hablar_ligue_uso": False,
        "fin_juego": False
    }
    with open("lester_sav.json", "w") as new_game:
        json.dump(save_data, new_game)

def load():
    global dias, hablar_uso, tener_ligue, primer_beso, hablar_ligue_uso, fin_juego, lester, ligue
    try:
        with open("lester_sav.json", "r") as load_game:
            save_data = json.load(load_game)
            # Restaurar variables globales
            dias = save_data["dias"]
            hablar_uso = save_data["hablar_uso"]
            tener_ligue = save_data["tener_ligue"]
            primer_beso = save_data["primer_beso"]
            hablar_ligue_uso = save_data["hablar_ligue_uso"]
            fin_juego = save_data["fin_juego"]

        # Crear personaje con stats guardados
        lester = Personaje(save_data["energia"], save_data["dinero"], save_data["nv_carisma"])
        ligue = Ligue(save_data["nom_ligue"], save_data["nv_carisma_ligue"], save_data["estado_relacion_xp"])
        
        print("\nJuego cargado exitosamente.\n")
        return True
    except FileNotFoundError:
        print("\nNo hay un archivo de guardado existente. Inicia un nuevo juego.\n")
        return False

def save():
    save_data = {
        "dias": dias,
        "energia": lester.energia,
        "dinero": lester.dinero,
        "nv_carisma": lester.nv_carisma,
        "hablar_uso": hablar_uso,
        "tener_ligue": tener_ligue,
        "primer_beso": primer_beso,
        "nom_ligue": ligue.nombre,
        "nv_carisma_ligue": ligue.nv_carisma,   
        "estado_relacion_xp": ligue.estado_relacion_xp,
        "hablar_ligue_uso": hablar_ligue_uso,
        "fin_juego": fin_juego
    }
    with open("lester_sav.json", "w") as save_game:
        json.dump(save_data, save_game)
    print("\nJuego guardado exitosamente.\n")


#Hub
def game():
    global dias,hablar_uso,dax_chance,ligue,hablar_ligue_uso,fin_juego, lester, ligue
    while True:
        print(f"Día {dias}")
        print(f"Stats:\nEnergia: {lester.energia}\nDinero: ${lester.dinero}\nNv. de Carisma: {lester.nv_carisma}")
        hub = input("\nSelecciona lo que quieres realizar:\n1.- Trabajar (-50 de Energia, +50 de Dinero)\n2.- Hablar con Dax (+1 Nv. de Carsima (Solo una vez por día))\n3.- Salir de Fiesta (-30 de Energia, -20 de Dinero)\n4.- Ir a la Tienda\n5.- Ligue\n6.- Dormir (Pasa al Sig. Día y Restablece Toda la Energia)\n7.- Guardar Partida\n8.- Volver al Menú\n")

        match hub:
            case "1":
                lester.trabajar()
            case "2":
                if hablar_uso == False:
                    lester.hablar(dax_chance)
                    hablar_uso = True
                elif hablar_uso == True and dax_chance[0] == True:
                    print("\nParece ser que ya has hablado con Dax\n")
                elif hablar_uso == True and dax_chance[0] == False:
                    print("\nParece ser que Dax no esta disponible\n")
                elif hablar_uso == True or hablar_uso == False and lester.nv_carisma == 10:
                    print("\nHas llegado al maximo nivel de carisma\n")
            case "3":
                if not tener_ligue:
                    lester.salir(primer_beso)
                else:
                    print(f"\nMejor trata de salir con {nom_ligue}\n")
            case "4":
                sleep(1)
                print("\nCajero: Bienvenido ¿En que te puedo servir?")
                tienda.tienda_menu(lester)
            case "5":
                if not tener_ligue:
                    print("\nNo tienes un ligue actualmente\n")
                else:
                    ligue.ligueMenu(lester)
            case "6": 
                dias = lester.dormir(dias)
                if dias == 50 and lester.dinero < 2000:
                    escenas.bad_ending()
                    print("\nNo tienes el dinero suficiente para ejecutar el Plan De Lester, Perdiste el Juego\n")
                    save()
                    break
                elif dias == 50 and lester.dinero >= 2000:
                    print("\nNo diste tu primer beso, tendras que ejecutar el Plan De Lester")
                    sleep(1)
                    escenas.norm_ending()
                    save()
                    break 
                elif primer_beso == True:
                    escenas.good_ending()
                    save()
                    break 
            case "7":
                sleep(1)
                save()
            case "8":
                break
            case _:
                print("Selecciona una opción valida\n")

#Menu
while True:
    print("Lester's First Kiss Quest")
    menu = input("\nSelecciona una opción:\n1.- Juego Nuevo\n2.- Continuar\n3.- Salir del Juego\n")

    match menu:
        case "1":
           sleep(1)
           newgame()
           escenas.intro()
           sleep(1)
           game()
        case "2":
            if load():
                if fin_juego == True and dias == 50 and lester.dinero > 2000 and primer_beso == False:
                    print("\nNo tienes el dinero suficiente para ejecutar el Plan De Lester, Perdiste el Juego\n")
                    break
                elif primer_beso == True:
                    print("\nAl parecer ya diste tu primer beso ¡Felicidades! Ganaste el Juego\n")
                else:
                    sleep(1)
                    game()
        case "3": 
            break
        case _:
            print("Selecciona una opción valida\n")