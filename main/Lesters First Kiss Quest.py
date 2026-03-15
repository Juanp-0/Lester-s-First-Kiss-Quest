#Lester's First Kiss Quest

import json
from random import shuffle
from time import sleep
from personaje import Personaje
from escenas import intro, bad_ending, norm_ending, novia_escena, good_ending

#Stats
dias = 1

#Stats del Ligue
nom_ligue = "null"
nv_carisma_ligue = 0
estado_relacion = ["Nulo", "Interesada", "Amigos", "Quedantes", "Novios"]
estado_relacion_xp = 0

#Factores RNG
dax_chance = [True, False]
ligue_chance = [True, False]
nom_chicas = ["Romina", "Ariana", "Julieta", "María", "Maya", "Erika", "Sofía", "Carla", "Debanhi", "Deborah", "Katia", "Serena", "Ramona", "Ana", "Alejandra", "Tondelaya", "Victoria", "Nereida", "Violeta", "Fernanda", "Catalina"]
nv_carisma_chicas = [1,2,3,4,5,6,7,8,9,10]
nv_carisma_mayor = ["Si", "No", "No", "No", "Flechazo"]
nv_carisma_igual = ["Si", "Si", "No", "No", "Flechazo"]
nv_carisma_menor = ["Si", "Si", "Si", "No", "Flechazo"]
ligue_aprobacion = ["Like", "Dislike", "Excelente"]

#Verificadores
hablar_uso = False
ligue = False
hablar_ligue_uso = False
primer_beso = False
fin_juego = False

#Sistema de Guardado
def newgame():
    global dias, hablar_uso, nom_ligue, nv_carisma_ligue, estado_relacion_xp, hablar_ligue_uso, fin_juego, lester, ligue, primer_beso
    # Inicializar variables globales
    dias = 1
    hablar_uso = False
    nom_ligue = "null"
    nv_carisma_ligue = 0
    estado_relacion_xp = 0
    hablar_ligue_uso = False
    fin_juego = False
    ligue = False
    primer_beso = False
    
    # Crear nuevo personaje con stats iniciales
    lester = Personaje(100, 0, 0)

    # Guardar estado inicial
    save_data = {
        "dias": 1,
        "energia": lester.energia,
        "dinero": lester.dinero,
        "nv_carisma": lester.nv_carisma,
        "hablar_uso": False,
        "ligue": False,
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
    global dias, hablar_uso, ligue, primer_beso, nom_ligue, nv_carisma_ligue, estado_relacion_xp, hablar_ligue_uso, fin_juego, lester
    try:
        with open("lester_sav.json", "r") as load_game:
            save_data = json.load(load_game)
            # Restaurar variables globales
            dias = save_data["dias"]
            hablar_uso = save_data["hablar_uso"]
            ligue = save_data["ligue"]
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
        "ligue": ligue,
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
                    shuffle(nv_carisma_mayor)
                    if nv_carisma_mayor[0] == "Si":
                        sleep(1)
                        ligue = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[0]
                        nv_carisma_ligue = nv_carisma_chicas[0]
                        estado_relacion_xp = 5
                        print("Parece que tus habilidades de carisma, fueron efectivas\n")
                    elif nv_carisma_mayor[0] == "Flechazo":
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
                    shuffle(nv_carisma_igual)
                    if nv_carisma_mayor[0] == "Si":
                        sleep(1)
                        ligue = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[0]
                        nv_carisma_ligue = nv_carisma_chicas[0]
                        estado_relacion_xp = 5
                        print("Parece que tus habilidades de carisma, fueron efectivas\n")
                    elif nv_carisma_igual[0] == "Flechazo":
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
                    shuffle(nv_carisma_menor)
                    if nv_carisma_menor[0] == "Si":
                        sleep(1)
                        ligue = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[0]
                        nv_carisma_ligue = nv_carisma_chicas[0]
                        estado_relacion_xp = 5
                        print("Parece que tus habilidades de carisma, fueron efectivas\n")
                    elif nv_carisma_menor[0] == "Flechazo":
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
                    shuffle(nv_carisma_mayor)
                    if nv_carisma_mayor[0] == "Si":
                        sleep(1)
                        ligue = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[1]
                        nv_carisma_ligue = nv_carisma_chicas[1]
                        estado_relacion_xp = 5
                        print("Parece que tus habilidades de carisma, fueron efectivas\n")
                    elif nv_carisma_mayor[0] == "Flechazo":
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
                    shuffle(nv_carisma_igual)
                    if nv_carisma_mayor[0] == "Si":
                        sleep(1)
                        ligue = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[1]
                        nv_carisma_ligue = nv_carisma_chicas[1]
                        print("Parece que tus habilidades de carisma, fueron efectivas\n")
                        estado_relacion_xp = 5
                    elif nv_carisma_igual[0] == "Flechazo":
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
                    shuffle(nv_carisma_menor)
                    if nv_carisma_menor[0] == "Si":
                        sleep(1)
                        ligue = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[1]
                        nv_carisma_ligue = nv_carisma_chicas[1]
                        estado_relacion_xp = 5
                        print("Parece que tus habilidades de carisma, fueron efectivas\n")
                    elif nv_carisma_menor[0] == "Flechazo":
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
                    shuffle(nv_carisma_mayor)
                    if nv_carisma_mayor[0] == "Si":
                        sleep(1)
                        ligue = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[2]
                        nv_carisma_ligue = nv_carisma_chicas[2]
                        estado_relacion_xp = 5
                        print("Parece que tus habilidades de carisma, fueron efectivas\n")
                    elif nv_carisma_mayor[0] == "Flechazo":
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
                    shuffle(nv_carisma_igual)
                    if nv_carisma_mayor[0] == "Si":
                        sleep(1)
                        ligue = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[2]
                        nv_carisma_ligue = nv_carisma_chicas[2]
                        estado_relacion_xp = 5
                        print("Parece que tus habilidades de carisma, fueron efectivas\n")
                    elif nv_carisma_igual[0] == "Flechazo":
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
                    shuffle(nv_carisma_menor)
                    if nv_carisma_menor[0] == "Si":
                        sleep(1)
                        ligue = True
                        #Datos del ligue
                        nom_ligue = nom_chicas[2]
                        nv_carisma_ligue = nv_carisma_chicas[2]
                        estado_relacion_xp = 5
                        print("Parece que tus habilidades de carisma, fueron efectivas\n")
                    elif nv_carisma_menor[0] == "Flechazo":
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

def salir():
    global primer_beso
    if lester.energia >= 30 and lester.dinero >= 20:
        lester.resEnergia(30)
        lester.resDinero(20)
        print("\nTe escapas a escondidas de tu casa\nTomas el metro para llegar al centro de la ciudad\nEntras a la primera discoteca que ves\n")
        sleep(1)
        print("La estas pasando excelente\nParece que se acercan unas chicas interesadas en ti\nEs hora de usar tus habilidades de carisma\n")
        chicas()
        if primer_beso == True:
            sleep(1)
            lester.dormir()
        else:
            sleep(1)
            print("Regresas a Casa de manera silenciosa, despues de una noche de locura\n")
            sleep(1)
    elif lester.dinero < 20:
        print("\nNo tienes dinero para Salir de fiesta\n")
    elif lester.energia < 30:
        print("\nNo tienes ganas de Salir de fiesta\n")

def tienda():
    while True:
        print("\nProductos disponibles:\n1.- Bebida Energetíca (+20 de Energia, -20 de Dinero)\n2.- Café Enbotellado (+10 de Energia, -15 de Dinero)\n3.- Perfume (+1 Nv. de Carisma, -150 de Dinero)")
        comprar = input("Selecciona el Producto que vayas a comprar o escribe S para salir de la tienda:\n")
        match comprar:
                case "1":
                    if lester.energia == 100:
                        print("\nTienes toda la energía recargada\n")
                    elif lester.dinero < 20:
                        print("\nNo te alcanza\n")
                    else:
                        lester.sumEnergia(20)
                        lester.resDinero(20)
                case "2":
                    if lester.energia == 100:
                        print("\nTienes toda la energía recargada\n")
                    elif lester.dinero < 15:
                        print("\nNo te alcanza\n")
                    else:
                        lester.sumEnergia(10)
                        lester.resDinero(15)
                case "3":
                    if lester.nv_carisma == 10:
                        print("\nHas llegado al maximo nivel de carisma\n")
                    elif lester.dinero < 150:
                        print("\nNo te alcanza\n")
                    else:
                        lester.sumNvCarisma(1)
                        lester.resDinero(150)
                case "S" | "s" :
                    print("\nCajero: Gracias por Comprar ¡Vuelva Pronto!\n")
                    sleep(1)
                    break
                case _:
                    print("Selecciona una opción valida\n")

def cita():
    global nom_ligue,estado_relacion_xp,ligue_aprobacion,ligue
    print(f"\nHas decido salir con {nom_ligue}")
    print("Lugares para tener una cita:\n1.- Sandwichería Local (-30 de Energía, -100 de Dinero)\n2.- Cafetería (-40 de Energía, -200 de Dinero)\n3.- Buffet Italiano (-40 de Energía, -350 de Dinero)\n4.- Estadio de Fútbol (-50 de Energía, -1000 de Dinero)\n")
    
    while True:
        cita_desicion = input("\nSelecciona un lugar para tener una cita o Escribe S para salir\n")

        match cita_desicion:
                case "1":
                    if lester.energia < 30:
                        print("\nNo tienes ganas de salir hoy\n")
                    elif lester.dinero < 100:
                        print("\nNo te alcanza\n")
                    else:
                        lester.resEnergia(30)
                        lester.resDinero(100)
                        print("\nHas decidido ir a Sandwichería Local\n")
                        shuffle(ligue_aprobacion)
                        if ligue_aprobacion[0] == "Like":
                            sleep(1)
                            estado_relacion_xp += 1
                            if estado_relacion_xp >= 20:
                                novia_escena()
                            else:
                                print(f"\nParece ser que {nom_ligue} ha disfrutado la cita\n")
                        elif ligue_aprobacion[0] == "Excelente":
                            sleep(1)
                            estado_relacion_xp += 3
                            if estado_relacion_xp >= 20:
                                novia_escena()
                            else:
                                print(f"\nParece ser que {nom_ligue} ha disfrutado muchisimo la cita\n")
                        else:
                            sleep(1)
                            estado_relacion_xp -= 1
                            if estado_relacion_xp == 0:
                                ligue = False
                                lester.resNvCarisma(2)
                                print("\nHiciste que tu ligue perdiera todo interes en tí\n")
                            else:
                                print(f"\nParece ser que {nom_ligue} no ha disfrutado la cita\n")
                        sleep(1)
                        print(f"\nRegresas a Casa, despues de salir con tu ligue\n")
                        sleep(1)
                        break
                case "2":
                    if lester.energia < 40:
                        print("\nNo tienes ganas de salir hoy\n")
                    elif lester.dinero < 200:
                        print("\nNo te alcanza\n")
                    else:
                        lester.resEnergia(40)
                        lester.resDinero(200)
                        print("\nHas decidido ir a Cafetería")
                        shuffle(ligue_aprobacion)
                        if ligue_aprobacion[0] == "Like":
                            sleep(1)
                            estado_relacion_xp += 1
                            if estado_relacion_xp >= 20:
                                novia_escena()
                            else:
                                print(f"\nParece ser que {nom_ligue} ha disfrutado la cita\n")
                        elif ligue_aprobacion [0] == "Excelente":
                            sleep(1)
                            estado_relacion_xp += 3
                            if estado_relacion_xp >= 20:
                                novia_escena()
                            else:
                                print(f"\nParece ser que {nom_ligue} ha disfrutado muchisimo la cita\n")
                        else:
                            estado_relacion_xp -= 1
                            if estado_relacion_xp == 0:
                                ligue = False
                                lester.resNvCarisma(2)
                                print("\nHiciste que tu ligue perdiera todo interes en tí\n")
                            else:
                                print(f"\nParece ser que {nom_ligue} no ha disfrutado la cita\n")
                        sleep(1)
                        print(f"\nRegresas a Casa, despues de salir con tu ligue\n")
                        sleep(1)
                        break
                case "3":
                    if lester.energia < 40:
                        print("\nNo tienes ganas de salir hoy\n")
                    elif lester.dinero < 350:
                        print("\nNo te alcanza\n")
                    else:
                        lester.resEnergia(40)
                        lester.resDinero(350)
                        print("\nHas decidido ir a Buffet Italiano\n")
                        shuffle(ligue_aprobacion)
                        if ligue_aprobacion[0] == "Like":
                            estado_relacion_xp += 1
                            if estado_relacion_xp >= 20:
                                novia_escena()
                            else:
                                print(f"\nParece ser que {nom_ligue} ha disfrutado la cita\n")
                        elif ligue_aprobacion[0] == "Excelente":
                            estado_relacion_xp += 3
                            if estado_relacion_xp >= 20:
                                novia_escena()
                            else:
                                print(f"\nParece ser que {nom_ligue} ha disfrutado muchisimo la cita\n")
                        else:
                            sleep(1)
                            estado_relacion_xp -= 1
                            if estado_relacion_xp == 0:
                                lester.resNvCarisma(2)
                                ligue = False
                                print("\nHiciste que tu ligue perdiera todo interes en tí\n")
                            else:
                                print(f"\nParece ser que {nom_ligue} no ha disfrutado la cita\n")
                        sleep(1)
                        print(f"\nRegresas a Casa, despues de salir con tu ligue\n")
                        sleep(1)
                        break
                case "4":
                    if lester.energia < 50:
                        print("\nNo tienes ganas de salir hoy\n")
                    elif lester.dinero < 1000:
                        print("\nNo te alcanza\n")
                    else:
                        lester.resEnergia(50)
                        lester.resDinero(1000)
                        print("\nHas decidido ir a Estadio de Fútbol\n")
                        shuffle(ligue_aprobacion)
                        if ligue_aprobacion[0] == "Like":
                            sleep(1)
                            estado_relacion_xp += 1
                            if estado_relacion_xp >= 20:
                                novia_escena()
                            else:
                                print(f"\nParece ser que {nom_ligue} ha disfrutado la cita\n")
                        elif ligue_aprobacion[0] == "Excelente":
                            sleep(1)
                            estado_relacion_xp += 3
                            if estado_relacion_xp >= 20:
                                novia_escena()
                            else:
                                print(f"\nParece ser que {nom_ligue} ha disfrutado muchisimo la cita\n")
                        else:
                            sleep(1)
                            estado_relacion_xp -= 1
                            if estado_relacion_xp == 0:
                                lester.resNvCarisma(2)
                                ligue = False
                                print("\nHiciste que tu ligue perdiera todo interes en tí\n")
                            else:
                                print(f"\nParece ser que {nom_ligue} no ha disfrutado la cita\n")
                        sleep(1)
                        print(f"\nRegresas a Casa, despues de salir con tu ligue\n")
                        sleep(1)
                        break
                case "S" | "s" :
                    break
                case _:
                    print("Selecciona una opción valida\n")

def hablar_ligue():
    global nom_ligue,estado_relacion_xp,ligue_aprobacion,ligue
    shuffle(ligue_chance)
    if ligue_chance[0] == True:
         if ligue_aprobacion[0] == "Like":
            estado_relacion_xp += 1
            if estado_relacion_xp >= 20:
                print(f"\nCitas a {nom_ligue} al lugar donde se conocieron\n")
                novia_escena()
            else:
                print(f"\nParece ser que {nom_ligue} ha disfrutado de la charla\n")
         elif ligue_aprobacion[0] == "Excelente":
            estado_relacion_xp += 3
            if estado_relacion_xp >= 20:
                print(f"\nCitas a {nom_ligue} al lugar donde se conocieron\n")
                novia_escena()
            else:
                print(f"\nParece ser que {nom_ligue} ha disfrutado muchisimo de la charla\n")
         else:
            estado_relacion_xp -= 1
            if estado_relacion_xp == 0:
                ligue = False
                lester.resNvCarisma(2)
                print("\nHiciste que tu ligue perdiera todo interes en tí\n")
            else:
                print(f"\nParece ser que {nom_ligue} no ha disfrutado de la charla\n")
    else:
        print (f"\nParece ser que {nom_ligue} no esta disponible\n")

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
                    lester.hablar()
                    hablar_uso = True
                elif hablar_uso == True and dax_chance[0] == True:
                    print("\nParece ser que ya has hablado con Dax\n")
                elif hablar_uso == True and dax_chance[0] == False:
                    print("\nParece ser que Dax no esta disponible\n")
                elif hablar_uso == True or hablar_uso == False and lester.nv_carisma == 10:
                    print("\nHas llegado al maximo nivel de carisma\n")
            case "3":
                if ligue == False:
                    salir()
                else:
                    print(f"\nMejor trata de salir con {nom_ligue}\n")
            case "4":
                sleep(1)
                print("\nCajero: Bienvenido ¿En que te puedo servir?")
                tienda()
            case "5":
                if ligue == True:
                    while True:
                        print(f"\nDatos de tu ligue:\nNombre: {nom_ligue}\nNv. de Carisma: {nv_carisma_ligue}")
                        if estado_relacion_xp >= 1 and estado_relacion_xp < 10:
                            print(f"Estado de la Relación: {estado_relacion[1]}\n")
                        elif estado_relacion_xp >= 10  and estado_relacion_xp < 15:
                            print(f"Estado de la Relación: {estado_relacion[2]}\n")
                        elif estado_relacion_xp >= 15  and estado_relacion_xp < 20:
                            print(f"Estado de la Relación: {estado_relacion[3]}\n")
                        elif estado_relacion_xp >= 20:
                            print(f"Estado de la Relación: {estado_relacion[4]}\n")
                        else:
                            print(f"Estado de la Relación: {estado_relacion[0]}\n")
                        ligue_menu = input(f"\nSelecciona lo que quieres hacer con {nom_ligue}:\n1.- Hablar con {nom_ligue} (Solo una vez por Día)\n2.- Tener una cita con {nom_ligue}\n3.- Volver al Hub\n")
                        match ligue_menu:
                            case "1":
                                if hablar_ligue_uso == False:
                                    hablar_ligue()
                                    hablar_ligue_uso = True
                                elif hablar_ligue_uso == True and ligue_chance[0] == True:
                                    print(f"\nParece ser que ya has hablado con {nom_ligue}\n")
                                elif hablar_ligue_uso == True and ligue_chance[0] == False:
                                    print(f"\nParece ser que {nom_ligue} no esta disponible\n")
                                elif  hablar_ligue_uso == True or hablar_ligue_uso == False and estado_relacion_xp >= 20:
                                    print(f"\nYa eres novio de {nom_ligue}, ya la conoces bien\n")
                            case "2":
                                if estado_relacion_xp >= 20:
                                    print(f"\nYa eres novio de {nom_ligue}, ya la conoces bien\n")
                                else:
                                    cita()
                            case "3": 
                                break
                            case _:
                                print("Selecciona una opción valida\n")
                else:
                    print("\nAún no tienes un ligue\n")
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
           intro()
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