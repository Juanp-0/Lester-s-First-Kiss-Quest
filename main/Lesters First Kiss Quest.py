#Lester's First Kiss Quest

import json
from random import choice, shuffle
from time import sleep
from personaje import Personaje
from escenas import intro, bad_ending, norm_ending, novia_escena, good_ending
from ligue import Ligue
from item import Item, EnergItem, CarismaItem
from tienda import Tienda

#Stats
dias = 1

#Factores RNG
dax_chance = [True, False]
nom_chicas = ["Romina", "Ariana", "Julieta", "María", "Maya", "Erika", "Sofía", "Carla", "Debanhi", "Deborah", "Katia", "Serena", "Ramona", "Ana", "Alejandra", "Tondelaya", "Victoria", "Nereida", "Violeta", "Fernanda", "Catalina"]
nv_carisma_chicas = [1,2,3,4,5,6,7,8,9,10]
nv_carisma_mayor = ["Si", "No", "No", "No", "Flechazo"]
nv_carisma_igual = ["Si", "Si", "No", "No", "Flechazo"]
nv_carisma_menor = ["Si", "Si", "Si", "No", "Flechazo"]

#Verificadores
hablar_uso = False
tener_ligue = False
hablar_ligue_uso = False
primer_beso = False
fin_juego = False

tienda = Tienda([EnergItem("Bebida Energetíca", 20, 20), EnergItem("Café Enbotellado", 15, 10), CarismaItem("Perfume", 150, 1)])


#Sistema de Guardado
def newgame():
    global dias, hablar_uso, nom_ligue, nv_carisma_ligue, estado_relacion_xp, hablar_ligue_uso, fin_juego, lester, ligue, primer_beso
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
        "nom_ligue": "null",
        "nv_carisma_ligue": 0,
        "estado_relacion_xp": 0,
        "hablar_ligue_uso": False,
        "fin_juego": False
    }
    with open("lester_sav.json", "w") as new_game:
        json.dump(save_data, new_game)

def load():
    global dias, hablar_uso, tener_ligue, primer_beso, nom_ligue, nv_carisma_ligue, estado_relacion_xp, hablar_ligue_uso, fin_juego, lester
    try:
        with open("lester_sav.json", "r") as load_game:
            save_data = json.load(load_game)
            # Restaurar variables globales
            dias = save_data["dias"]
            hablar_uso = save_data["hablar_uso"]
            tener_ligue = save_data["tener_ligue"]
            primer_beso = save_data["primer_beso"]
            nom_ligue = save_data["nom_ligue"]
            nv_carisma_ligue = save_data["nv_carisma_ligue"]
            estado_relacion_xp = save_data["estado_relacion_xp"]
            hablar_ligue_uso = save_data["hablar_ligue_uso"]
            fin_juego = save_data["fin_juego"]

        # Crear personaje con stats guardados
        lester = Personaje(save_data["energia"], save_data["dinero"], save_data["nv_carisma"])
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
        "nom_ligue": nom_ligue,
        "nv_carisma_ligue": nv_carisma_ligue,
        "estado_relacion_xp": estado_relacion_xp,
        "hablar_ligue_uso": hablar_ligue_uso,
        "fin_juego": fin_juego
    }
    with open("lester_sav.json", "w") as save_game:
        json.dump(save_data, save_game)
    print("\nJuego guardado exitosamente.\n")

#Acciones
def chicas():
    global nom_chicas,nv_carisma_chicas,nv_carisma_mayor,nv_carisma_igual,nv_carisma_menor,ligue,primer_beso,nom_ligue,nv_carisma_ligue,estado_relacion_xp
    while True:
        shuffle(nom_chicas)
        shuffle(nv_carisma_chicas)
        print(f"\nChica 1:\nNombre: {nom_chicas[0]}\nNv. de Carisma: {nv_carisma_chicas[0]}\n")
        sleep(1)
        print(f"Chica 2:\nNombre: {nom_chicas[1]}\nNv. de Carisma: {nv_carisma_chicas[1]}\n")
        sleep(1)
        print(f"Chica 3:\nNombre: {nom_chicas[2]}\nNv. de Carisma: {nv_carisma_chicas[2]}\n")
        sleep(1)

        desicion = input("Ingresa el numero de la chica con la que quieras hablar:\n")

        match desicion:
            case "1":
                if lester.nv_carisma < nv_carisma_chicas[0]:
                    resultado_carisma = choice(nv_carisma_mayor)
                    if resultado_carisma == "Si":
                        sleep(1)
                        ligue = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[0]
                        nv_carisma_ligue = nv_carisma_chicas[0]
                        estado_relacion_xp = 5
                        print("Parece que tus habilidades de carisma, fueron efectivas\n")
                    elif resultado_carisma == "Flechazo":
                        sleep(1)
                        ligue = True
                        primer_beso = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[0]
                        nv_carisma_ligue = nv_carisma_chicas[0]
                        estado_relacion_xp = 21
                        print("Parece que tus habilidades de carisma, fueron superefectivas, tanto que acabas de dar tu primer beso\n")
                    else:
                        sleep(1)
                        print("Parece que tus habilidades de carisma, no fueron efectivas\n")
                
                if lester.nv_carisma == nv_carisma_chicas[0]:
                    resultado_carisma_igual = choice(nv_carisma_igual)
                    if resultado_carisma_igual == "Si":
                        sleep(1)
                        ligue = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[0]
                        nv_carisma_ligue = nv_carisma_chicas[0]
                        estado_relacion_xp = 5
                        print("Parece que tus habilidades de carisma, fueron efectivas\n")
                    elif resultado_carisma_igual == "Flechazo":
                        sleep(1)
                        ligue = True
                        primer_beso = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[0]
                        nv_carisma_ligue = nv_carisma_chicas[0]
                        estado_relacion_xp = 21
                        print("Parece que tus habilidades de carisma, fueron superefectivas, tanto que acabas de dar tu primer beso\n")
                    else:
                        sleep(1)
                        print("Parece que tus habilidades de carisma, no fueron efectivas\n")
                
                if lester.nv_carisma > nv_carisma_chicas[0]:
                    resultado_carisma_menor = choice(nv_carisma_menor)
                    if resultado_carisma_menor == "Si":
                        sleep(1)
                        ligue = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[0]
                        nv_carisma_ligue = nv_carisma_chicas[0]
                        estado_relacion_xp = 5
                        print("Parece que tus habilidades de carisma, fueron efectivas\n")
                    elif resultado_carisma_menor == "Flechazo":
                        sleep(1)
                        ligue = True
                        primer_beso = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[0]
                        nv_carisma_ligue = nv_carisma_chicas[0]
                        estado_relacion_xp = 21
                        print("Parece que tus habilidades de carisma, fueron superefectivas, tanto que acabas de dar tu primer beso\n")
                    else:
                        sleep(1)
                        print("Parece que tus habilidades de carisma, no fueron efectivas\n")
                break
            case "2":
                if lester.nv_carisma < nv_carisma_chicas[1]:
                    resultado_carisma = choice(nv_carisma_mayor)
                    if resultado_carisma == "Si":
                        sleep(1)
                        ligue = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[1]
                        nv_carisma_ligue = nv_carisma_chicas[1]
                        estado_relacion_xp = 5
                        print("Parece que tus habilidades de carisma, fueron efectivas\n")
                    elif resultado_carisma == "Flechazo":
                        sleep(1)
                        ligue = True
                        primer_beso = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[1]
                        nv_carisma_ligue = nv_carisma_chicas[1]
                        estado_relacion_xp = 21
                        print("Parece que tus habilidades de carisma, fueron superefectivas, tanto que acabas de dar tu primer beso\n")
                    else:
                        sleep(1)
                        print("Parece que tus habilidades de carisma, no fueron efectivas\n")
                
                if lester.nv_carisma == nv_carisma_chicas[1]:
                    resultado_carisma_igual = choice(nv_carisma_igual)
                    if resultado_carisma_igual == "Si":
                        sleep(1)
                        ligue = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[1]
                        nv_carisma_ligue = nv_carisma_chicas[1]
                        print("Parece que tus habilidades de carisma, fueron efectivas\n")
                        estado_relacion_xp = 5
                    elif resultado_carisma_igual == "Flechazo":
                        sleep(1)
                        ligue = True
                        primer_beso = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[1]
                        nv_carisma_ligue = nv_carisma_chicas[1]
                        estado_relacion_xp = 21
                        print("Parece que tus habilidades de carisma, fueron superefectivas, tanto que acabas de dar tu primer beso\n")
                    else:
                        sleep(1)
                        print("Parece que tus habilidades de carisma, no fueron efectivas\n")
                
                if lester.nv_carisma > nv_carisma_chicas[1]:
                    resultado_carisma_menor = choice(nv_carisma_menor)
                    if resultado_carisma_menor == "Si":
                        sleep(1)
                        ligue = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[1]
                        nv_carisma_ligue = nv_carisma_chicas[1]
                        estado_relacion_xp = 5
                        print("Parece que tus habilidades de carisma, fueron efectivas\n")
                    elif resultado_carisma_menor == "Flechazo":
                        sleep(1)
                        ligue = True
                        primer_beso = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[1]
                        nv_carisma_ligue = nv_carisma_chicas[1]
                        estado_relacion_xp = 21
                        print("Parece que tus habilidades de carisma, fueron superefectivas, tanto que acabas de dar tu primer beso\n")
                    else:
                        sleep(1)
                        print("Parece que tus habilidades de carisma, no fueron efectivas\n")
                break
            case "3": 
                if lester.nv_carisma < nv_carisma_chicas[2]:
                    resultado_carisma = choice(nv_carisma_mayor)
                    if resultado_carisma == "Si":
                        sleep(1)
                        ligue = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[2]
                        nv_carisma_ligue = nv_carisma_chicas[2]
                        estado_relacion_xp = 5
                        print("Parece que tus habilidades de carisma, fueron efectivas\n")
                    elif resultado_carisma == "Flechazo":
                        sleep(1)
                        ligue = True
                        primer_beso = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[2]
                        nv_carisma_ligue = nv_carisma_chicas[2]
                        estado_relacion_xp = 21
                        print("Parece que tus habilidades de carisma, fueron superefectivas, tanto que acabas de dar tu primer beso\n")
                    else:
                        sleep(1)
                        print("Parece que tus habilidades de carisma, no fueron efectivas\n")
                
                if lester.nv_carisma == nv_carisma_chicas[2]:
                    resultado_carisma_igual = choice(nv_carisma_igual)
                    if resultado_carisma_igual == "Si":
                        sleep(1)
                        ligue = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[2]
                        nv_carisma_ligue = nv_carisma_chicas[2]
                        estado_relacion_xp = 5
                        print("Parece que tus habilidades de carisма, fueron efectivas\n")
                    elif resultado_carisma_igual == "Flechazo":
                        sleep(1)
                        ligue = True
                        primer_beso = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[2]
                        nv_carisma_ligue = nv_carisma_chicas[2]
                        estado_relacion_xp = 21
                        print("Parece que tus habilidades de carisma, fueron superefectivas, tanto que acabas de dar tu primer beso\n")
                    else:
                        sleep(1)
                        print("Parece que tus habilidades de carisma, no fueron efectivas\n")
                
                if lester.nv_carisma > nv_carisma_chicas[2]:
                    resultado_carisma_menor = choice(nv_carisma_menor)
                    if resultado_carisma_menor == "Si":
                        sleep(1)
                        ligue = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[2]
                        nv_carisma_ligue = nv_carisma_chicas[2]
                        estado_relacion_xp = 5
                        print("Parece que tus habilidades de carisma, fueron efectivas\n")
                    elif resultado_carisma_menor == "Flechazo":
                        sleep(1)
                        ligue = True
                        primer_beso = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[2]
                        nv_carisma_ligue = nv_carisma_chicas[2]
                        estado_relacion_xp = 21
                        print("Parece que tus habilidades de carisma, fueron superefectivas, tanto que acabas de dar tu primer beso\n")
                    else:
                        sleep(1)
                        print("Parece que tus habilidades de carisma, no fueron efectivas\n")
                break
            case _:
                print("Selecciona una opción valida\n")

#Hub
def game():
    global dias,hablar_uso,dax_chance,ligue,nom_ligue,nv_carisma_ligue,estado_relacion,estado_relacion_xp,ligue_chance,hablar_ligue_uso,fin_juego, lester
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
                    lester.salir()
                else:
                    print(f"\nMejor trata de salir con {nom_ligue}\n")
            case "4":
                sleep(1)
                print("\nCajero: Bienvenido ¿En que te puedo servir?")
                tienda.tienda_menu(lester)
            case "5":
                ligue.ligueMenu(lester)
            case "6": 
                lester.dormir()
                if dias == 50 and lester.dinero < 2000:
                    bad_ending()
                    print("\nNo tienes el dinero suficiente para ejecutar el Plan De Lester, Perdiste el Juego\n")
                    save()
                    break
                elif dias == 50 and lester.dinero >= 2000:
                    print("\nNo diste tu primer beso, tendras que ejecutar el Plan De Lester")
                    sleep(1)
                    norm_ending()
                    save()
                    break 
                elif primer_beso == True:
                    good_ending()
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