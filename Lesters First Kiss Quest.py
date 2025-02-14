#Lester's First Kiss Quest

import json
from random import shuffle
from time import sleep

#Stats
dias = 1
energia = 100
dinero = 0
nv_carisma = 0

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
    global dias, energia, dinero, nv_carisma, hablar_uso,nom_ligue,nv_carisma_ligue,estado_relacion_xp,hablar_ligue_uso,fin_juego
    dias, energia, dinero, nv_carisma,nv_carisma_ligue,estado_relacion_xp = 1, 100, 0, 0, 0, 0
    hablar_uso = False
    nom_ligue = "null"
    hablar_ligue_uso = False
    fin_juego = False

    save_data = {
        "dias": 1,
        "energia": 100,
        "dinero": 0,
        "nv_carisma": 0,
        "hablar_uso": False,
        "ligue": False,
        "primer_beso": False,
        "nom_ligue": "null",
        "nv_carisma_ligue": 0,
        "estado_relacion_xp": 0,
        "hablar_ligue_uso": False,
        "fin_juego": False
    }
    with open("lester_sav.txt", "w") as new_game:
        json.dump(save_data, new_game)

def load():
    global dias, energia, dinero, nv_carisma, hablar_uso, ligue, primer_beso,nom_ligue,nv_carisma_ligue,estado_relacion_xp,hablar_ligue_uso,fin_juego
    try:
        with open("lester_sav.txt", "r") as load_game:
            save_data = json.load(load_game)
            dias = save_data["dias"]
            energia = save_data["energia"]
            dinero = save_data["dinero"]
            nv_carisma = save_data["nv_carisma"]
            hablar_uso = save_data["hablar_uso"]
            ligue = save_data["ligue"]
            primer_beso = save_data["primer_beso"]
            nom_ligue = save_data["nom_ligue"]
            nv_carisma_ligue = save_data["nv_carisma_ligue"]
            estado_relacion_xp = save_data["estado_relacion_xp"]
            hablar_ligue_uso = save_data["hablar_ligue_uso"]
            fin_juego = save_data["fin_juego"]

        print("\nJuego cargado exitosamente.\n")
        return True
    except FileNotFoundError:
        print("\nNo hay un archivo de guardado existente. Inicia un nuevo juego.\n")
        return False

def save():
    save_data = {
        "dias": dias,
        "energia": energia,
        "dinero": dinero,
        "nv_carisma": nv_carisma,
        "hablar_uso": hablar_uso,
        "ligue": ligue,
        "primer_beso": primer_beso,
        "nom_ligue": nom_ligue,
        "nv_carisma_ligue": nv_carisma_ligue,
        "estado_relacion_xp": estado_relacion_xp,
        "hablar_ligue_uso": hablar_ligue_uso,
        "fin_juego": fin_juego
    }
    with open("lester_sav.txt", "w") as save_game:
        json.dump(save_data, save_game)
    print("\nJuego guardado exitosamente.\n")

#Cinematicas
def intro():
    print("\nEsta es una historia de cuatro amigos, Lester, Dax, Hugh y Zohan\n")
    sleep(1)
    print("Son cuatro chicos de 19 años, quienes se conocen desde la secundaria\n")
    sleep(1)
    print("En la noche de año nuevo, Zohan se acordo de algo que le dijo Lester\n")
    sleep(1)
    print("Una promesa, que tiene que cumplir en el presente año\n")
    sleep(1)
    print("Por lo que rapidamente, Zohan toma su celular y decide hablar en el chat grupal de los amigos\n")
    sleep(1)
    print("\n                  1 de Enero de 2015 - 12:30 am - Chat Grupal                     \n")
    sleep(1)
    print("Zohan: @todos")
    sleep(1)
    print("Zohan: Tengo un anuncio importante que dar")
    sleep(1)
    print("Dax: ¿Que Paso?")
    sleep(1)
    print("Dax: Me estaba durmiendo")
    sleep(1)
    print("Zohan: Me acordé de algo de suma importancia")
    sleep(1)
    print("Zohan: Es que no se si hacerlo más al rato")
    sleep(1)
    print("Zohan: Porque necesito especialmente a Lester disponible")
    sleep(1)
    print("Lester: Aqui estoy")
    sleep(1)
    print("Lester: Dilo de una vez")
    sleep(1)
    print("Zohan: Okey")
    sleep(1)
    print("Zohan: @todos")
    sleep(1)
    print("Zohan: Primero que nada")
    sleep(1)
    print("Zohan: Feliz 2015")
    sleep(1)
    print("Zohan: Ya es 2015")
    sleep(1)
    print("Zohan: Y quiero hacerle un amable recordatorio a mi amigo Lester")
    sleep(1)
    print("Zohan: Ya que dijo que haría algo especial este año")
    sleep(1)
    print("Hugh: Al fin sacaras a Lester del Grupo?")
    sleep(1)
    print("Zohan: Nop")
    sleep(1)
    print("Zohan: Mi buen amigo Lester comento algo el 16 de agosto de 2013 a las 7:43 pm")
    sleep(1)
    print("Zohan: y cito")
    sleep(1)
    print("\n                 16 de Agosto de 2013 - 19:43 pm - Chat Grupal                   \n")
    sleep(1)
    print("Lester: Aunque claro aún tengo presente el plan por si no doy mi primer beso antes de los 20")
    sleep(1)
    print("Lester: Ir a una convención")
    sleep(1)
    print("Lester: Ver a una cosplayer de chica anime")
    sleep(1)
    print("Lester: y ofrecerle unos $2000 para que me de un beso")
    sleep(1)
    print("Lester: con todo respeto")
    sleep(1)
    print("\n                  1 de Enero de 2015 - 01:00 am - Chat Grupal                    \n")
    sleep(1)
    print("Dax: XD")
    sleep(1)
    print("Dax: Ya se por donde va esto")
    sleep(1)
    print("Zohan: Tic Tac Lester Tic Tac")
    sleep(1)
    print("Lester: Se cancela ")
    sleep(1)
    print("Lester: Ni siquiera recordaba haber dicho eso")
    sleep(1)
    print("Hugh: XD")
    sleep(1)
    print("Hugh: Eres un reverendo pendejo Lester")
    sleep(1)
    print("Zohan: No Lester")
    sleep(1)
    print("Zohan: Ya no hay vuelta atrás")
    sleep(1)
    print("Zohan: Te quedan 50 días Lester")
    sleep(1)
    print("Zohan: Lo que quedaba de 2013 no hiciste nada")
    sleep(1)
    print("Zohan: y en 2014 tampoco")
    sleep(1)
    print("Zohan: Y ya solo te quedan menos de 2 meses Lester")
    sleep(1)
    print("Zohan: El tiempo corre")
    sleep(1)
    print("\nLester cumple 20 años dentro de 50 dias\n")
    sleep(1)
    print("Asi que como dijo Zohan\n")
    sleep(1)
    print("EL TIEMPO CORRE\n")

def bad_ending():
    global fin_juego
    sleep(1)
    print("\n                        Unos Meses Despues                   \n")
    sleep(1)
    print("\n             14 de Marzo de 2015 - 16:00 pm - Super Geek Fest                     \n")
    sleep(1)
    print("Zohan: Muy bien")
    sleep(1)
    print("Zohan: Ya llegamos al Super Geek Fest")
    sleep(1)
    print("Zohan: ¿Estas Listo Lester?")
    sleep(1)
    print("Lester: MmMmMmMmM")
    sleep(1)
    print("\nVes nerviosamente a Hugh a quien le importas un comino pero ahi esta\n")
    sleep(1)
    print("Luego ves nerviosamente a Dax quien trato de ayudarte pero fallo estrepitosamente\n")
    sleep(1)
    print("Ves que ambos te estan mirando de una manera bastante peculiar, como si estuviaran aguantando la respiración\n")
    sleep(1)
    print("Lester: Chicos ¿Le Decimos?")
    sleep(1)
    print("Zohan: Decirme que")
    sleep(1)
    print("Lester: Te sere sincero Zohan")
    sleep(1)
    print("Lester: No alcanze a ahorrar $2000 para pagarle a la cosplayer")
    sleep(1)
    print("\nVes que Hugh y Dax se empiezan a reír fuertemente\n")
    sleep(1)
    print("Zohan: ¡PUTA MADRE LESTER!\n")
    fin_juego = True

def norm_ending():
    global dinero, primer_beso, fin_juego
    sleep(1)
    print("\n                        Unos Meses Despues                   \n")
    sleep(1)
    print("\n             14 de Marzo de 2015 - 16:00 pm - Super Geek Fest                     \n")
    sleep(1)
    print("Zohan: Muy bien")
    sleep(1)
    print("Zohan: Ya llegamos al Super Geek Fest")
    sleep(1)
    print("Zohan: ¿Estas Listo Lester?")
    sleep(1)
    print("Lester: Eso Creo")
    sleep(1)
    print("Zohan: Okey, En base a este mapa, estamos en el centro y")
    sleep(1)
    print("Zohan: ¡AY CARAJO!")
    sleep(1)
    print("Zohan: ¡SON UN MONTON DE COSPLAYERS!")
    sleep(1)
    print("Dax: Es una convención, genio")
    sleep(1)
    print("Zohan: Lo sé pero va a estar dificíl econtrar a una cosplayer de chica anime")
    sleep(1)
    print("Hugh: Lo que tenemos que hacer por el estupido de Lester")
    sleep(1)
    print("\n                        Unas Horas Despues                  \n")
    sleep(1)
    print("Zohan: Okey, esta es la Cosplayer No. 500 de chica anime")
    sleep(1)
    print("Zohan: Muy Bien Lester ya sabes que decir campeón")
    sleep(1)
    print("Lester: MmMmMmMmM")
    sleep(1)
    print("Lester: No lo se Zohan")
    sleep(1)
    print("Lester: Empiezo a creer que esto es una perdida de tiempo")
    sleep(1)
    print("\nVes lentamente como Zohan te da una cachetada\n")
    sleep(1)
    print("Lester: Auch")
    sleep(1)
    print("Zohan: Alivianate Bastardo")
    sleep(1)
    print("Zohan: Ya llegamos aquí y no tienes nada que perder¿si o no?")
    sleep(1)
    print("Dax: Si")
    sleep(1)
    print("Hugh: Va a perder o $2000 o su dignidad")
    sleep(1)
    print("Zohan: Callate Hugh")
    sleep(1)
    print("Zohan: Que dices Lester ¿Lo haras o eres un cobarde?")
    sleep(1)
    print("Lester: Esta bien")
    sleep(1)
    print("\nTe acercas lentamente a la cosplayer, estas congelado y no sabes que decir\n")
    sleep(1)
    print("Lester: MmMmMmMmM")
    sleep(1)
    print("Lester: Oye Amiga")
    sleep(1)
    print("Lester: MmMmMmMmM")
    sleep(1)
    print("Cosplayer de Chica Anime: ¿Que se te ofrece amigo?")
    sleep(1)
    print("Lester: MmMmMmMmM")
    sleep(1)
    print("Lester: No se si sea posible que me des unnnnn")
    sleep(1)
    print("Lester: MmMmMmMmM")
    sleep(1)
    print("Zohan: Carajo, Lester se trabó")
    sleep(1)
    print("Dax: Se le olvidaron todos los consejos que le di")
    sleep(1)
    print("Hugh: Que perdedor")
    sleep(1)
    print("Cosplayer de Chica Anime: ¿Un que?")
    sleep(1)
    print("Lester: U-un Beso a cambio d-de $2000")
    sleep(1)
    print("Cosplayer de Chica Anime: ...")
    sleep(5)
    print("\nEstas demasiado nervioso porque se esta tardando en responder\n")
    sleep(1)
    print("Cosplayer de Chica Anime: Va ¿Porqué no?")
    dinero -= 2000
    primer_beso = True
    sleep(1)
    print("Zohan: Lo logró, ese bastardo lo logró")
    sleep(1)
    print("Dax: Parece que alguien se tiene que retractar por lo que dijo hace rato")
    sleep(1)
    print("Hugh: Por como lo hizo, no lo creo")
    sleep(1)
    print("\nEntraste en un extasís, al fin diste tu primer beso\n")
    sleep(1)
    print("Lester: ¡CHICOS! ¡LO LOGRE!\n")
    fin_juego = True

def novia_escena():
    global nom_ligue,primer_beso
    sleep(1)
    print("\n               En ese mismo momento                   \n")
    sleep(1)
    print(f"Lester: Oye {nom_ligue}")
    sleep(1)
    print(f"{nom_ligue}: Dime ¿Qué Ocurre?")
    sleep(1)
    print("Lester: Es que, bueno, tu sabes")
    sleep(1)
    print("Lester: Ya llevamos buen rato saliendo")
    sleep(1)
    print("Lester: y yo me preguntaba")
    sleep(1)
    print("Lester: ...")
    sleep(1)
    print("Lester: MmMmMmMmM")
    sleep(1)
    print("\nEstas congelado, tienes miedo, la incertidumbre te provoca inquietud\n")
    sleep(1)
    print(f"{nom_ligue}: Lester ¿Qué Pasa?")
    sleep(1)
    print(f"\nEscuchar la voz de {nom_ligue}, viendo su preocupación, te hace despertar\n")
    sleep(1)
    print(f"Lester: {nom_ligue}")
    sleep(1)
    print("Lester: ¿Quisieras ser mi novia?")
    sleep(1)
    print(f"{nom_ligue}: ...")
    sleep(5)
    print("\nEstas demasiado nervioso porque se esta tardando en responder\n")
    sleep(1)
    print(f"{nom_ligue}: Si")    
    sleep(1)
    print(f"{nom_ligue}: Si quiero ser tu novia")   
    sleep(1)
    print("\nNo lo puedes creer, lo lograste, quisieras que tus amigos estuvieran aqui para verlo \n")
    sleep(1)
    print(f"\nVes lentamente como {nom_ligue} se avalanza sobre ti\n")
    sleep(1)
    print("\nY\n")
    primer_beso = True
    sleep(1)
    print("\nEntraste en un extasís, al fin diste tu primer beso\n")
    sleep(1)
    print("Lester: (Wow)")
    sleep(1)
    print("Lester: (Lo Logré)\n")
    sleep(1)

def good_ending():
    global fin_juego,nom_ligue
    sleep(1)
    print("\n                        Un Año Despues                   \n")
    sleep(1)
    print(f"\nEstas apunto de celebrar el primer aniversario que estas junto a {nom_ligue}\n")
    sleep(1)
    print(f"{nom_ligue}: ¿Ya estas listo amor?")
    sleep(1)
    print("Lester: Si ¿y tú?")
    sleep(1)
    print(f"{nom_ligue}: Aun me falta maquillarme, esperame")
    sleep(1)
    print("Lester: Okey")
    sleep(1)
    print("\nDecides aprovechar el tiempo para hablar con tus amigos\n")
    sleep(1)
    print("Abres chat grupal que tienes con tus amigos\n")
    sleep(1)
    print(f"Lester: Bueno Chicos, hoy cumplo un año que estoy con {nom_ligue} y la verdad les quiero agradecer")
    sleep(1)
    print("Lester: Primero, Gracias Zohan, porque si no me hubieras puesto este absurdo reto")
    sleep(1)
    print("Lester: No hubiera conocido a una maravillosa persona")
    sleep(1)
    print("Zohan: De nada, para eso estamos Lester")
    sleep(1)
    print("Lester: Segundo, Gracias Dax, por apoyarme y darme consejos")
    sleep(1)
    print("Lester: Se que debi hacerte caso antes, pero al final si accedí y lo entendí todo")
    sleep(1)
    print("Dax: No hay nada que agradecer Lester, para eso estamos")
    sleep(1)
    print("Lester: y por ultimo gracias Hugh, se que no te importo, pero almenos estuviste ahi")
    sleep(1)
    print("Lester: y por eso te lo agradezco")
    sleep(1)
    print("Hugh: Okey")
    sleep(1)
    print("Lester: Bueno, ya me voy, gracias por todo chicos")
    sleep(1)
    print(f"\nTe desconectas para salir con {nom_ligue}\n")
    sleep(1)
    print("Zohan: Bro, realmente hicimos crecer a Lester")
    sleep(1)
    print("Dax: Y si, quien crería que Lester ya tiene novia")
    sleep(1)
    print("Hugh: Yo hubiera apostado mi casa a que moría virgen\n")
    fin_juego = True

#Acciones
def trabajar():
    global energia, dinero
    if energia >= 50:
        energia -= 50
        dinero += 50
        sleep(1)
        print("\nRegresas a Casa, despues de un arduo día de trabajo\n")
        sleep(1)
    else:
        print ("\nNo tienes ganas de ir a Trabajar\n")

def hablar():
    global nv_carisma
    shuffle(dax_chance)
    if dax_chance[0] == True:
        sleep(1)
        nv_carisma += 1
        print("\nDax te da unos buenos consejos para aumentar tu carisma\n")
        sleep(1)
    else:
        sleep(1)
        print ("\nParece ser que Dax no esta disponible\n")
        sleep(1)

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
                if nv_carisma < nv_carisma_chicas[0]:
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
                
                if nv_carisma == nv_carisma_chicas[0]:
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
                
                if nv_carisma > nv_carisma_chicas[0]:
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
                if nv_carisma < nv_carisma_chicas[1]:
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
                
                if nv_carisma == nv_carisma_chicas[1]:
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
                
                if nv_carisma > nv_carisma_chicas[1]:
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
                if nv_carisma < nv_carisma_chicas[2]:
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
                
                if nv_carisma == nv_carisma_chicas[2]:
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
                
                if nv_carisma > nv_carisma_chicas[2]:
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
    global energia, dinero, primer_beso
    if energia >= 30 and dinero >= 20:
        energia -= 30
        dinero -= 20
        print("\nTe escapas a escondidas de tu casa\nTomas el metro para llegar al centro de la ciudad\nEntras a la primera discoteca que ves\n")
        sleep(1)
        print("La estas pasando excelente\nParece que se acercan unas chicas interesadas en ti\nEs hora de usar tus habilidades de carisma\n")
        chicas()
        if primer_beso == True:
            sleep(1)
            dormir()
        else:
            sleep(1)
            print("Regresas a Casa de manera silenciosa, despues de una noche de locura\n")
            sleep(1)
    elif dinero < 20:
        print("\nNo tienes dinero para Salir de fiesta\n")
    elif energia < 30:
        print("\nNo tienes ganas de Salir de fiesta\n")

def tienda():
    global energia,nv_carisma,dinero
    while True:
        print("\nProductos disponibles:\n1.- Bebida Energetíca (+20 de Energia, -20 de Dinero)\n2.- Café Enbotellado (+10 de Energia, -15 de Dinero)\n3.- Perfume (+1 Nv. de Carisma, -150 de Dinero)")
        comprar = input("Selecciona el Producto que vayas a comprar o escribe S para salir de la tienda:\n")
        match comprar:
                case "1":
                    if energia == 100:
                        print("\nTienes toda la energía recargada\n")
                    elif dinero < 20:
                        print("\nNo te alcanza\n")
                    else:
                        energia += 20
                        dinero -= 20
                case "2":
                    if energia == 100:
                        print("\nTienes toda la energía recargada\n")
                    elif dinero < 15:
                        print("\nNo te alcanza\n")
                    else:
                        energia += 10
                        dinero -= 15
                case "3":
                    if nv_carisma == 10:
                        print("\nHas llegado al maximo nivel de carisma\n")
                    elif dinero < 150:
                        print("\nNo te alcanza\n")
                    else:
                        nv_carisma += 1
                        dinero -= 150
                case "S" | "s" :
                    print("\nCajero: Gracias por Comprar ¡Vuelva Pronto!\n")
                    sleep(1)
                    break
                case _:
                    print("Selecciona una opción valida\n")

def cita():
    global energia,dinero,nom_ligue,estado_relacion_xp,ligue_aprobacion,ligue,nv_carisma
    print(f"\nHas decido salir con {nom_ligue}")
    print("Lugares para tener una cita:\n1.- Sandwichería Local (-30 de Energía, -100 de Dinero)\n2.- Cafetería (-40 de Energía, -200 de Dinero)\n3.- Buffet Italiano (-40 de Energía, -350 de Dinero)\n4.- Estadio de Fútbol (-50 de Energía, -1000 de Dinero)\n")
    
    while True:
        cita_desicion = input("\nSelecciona un lugar para tener una cita o Escribe S para salir\n")

        match cita_desicion:
                case "1":
                    if energia < 30:
                        print("\nNo tienes ganas de salir hoy\n")
                    elif dinero < 100:
                        print("\nNo te alcanza\n")
                    else:
                        energia -= 30
                        dinero -= 100
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
                                nv_carisma -= 2
                                print("\nHiciste que tu ligue perdiera todo interes en tí\n")
                            else:
                                print(f"\nParece ser que {nom_ligue} no ha disfrutado la cita\n")
                        sleep(1)
                        print(f"\nRegresas a Casa, despues de salir con tu ligue\n")
                        sleep(1)
                        break
                case "2":
                    if energia < 40:
                        print("\nNo tienes ganas de salir hoy\n")
                    elif dinero < 200:
                        print("\nNo te alcanza\n")
                    else:
                        energia -= 40
                        dinero -= 200
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
                                nv_carisma -= 2
                                print("\nHiciste que tu ligue perdiera todo interes en tí\n")
                            else:
                                print(f"\nParece ser que {nom_ligue} no ha disfrutado la cita\n")
                        sleep(1)
                        print(f"\nRegresas a Casa, despues de salir con tu ligue\n")
                        sleep(1)
                        break
                case "3":
                    if energia < 40:
                        print("\nNo tienes ganas de salir hoy\n")
                    elif dinero < 350:
                        print("\nNo te alcanza\n")
                    else:
                        energia -= 40
                        dinero -= 350
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
                                nv_carisma -= 2
                                ligue = False
                                print("\nHiciste que tu ligue perdiera todo interes en tí\n")
                            else:
                                print(f"\nParece ser que {nom_ligue} no ha disfrutado la cita\n")
                        sleep(1)
                        print(f"\nRegresas a Casa, despues de salir con tu ligue\n")
                        sleep(1)
                        break
                case "4":
                    if energia < 50:
                        print("\nNo tienes ganas de salir hoy\n")
                    elif dinero < 1000:
                        print("\nNo te alcanza\n")
                    else:
                        energia -= 50
                        dinero -= 1000
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
                                nv_carisma -= 2
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
    global nom_ligue,estado_relacion_xp,ligue_aprobacion,ligue,nv_carisma
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
                nv_carisma -= 2
                print("\nHiciste que tu ligue perdiera todo interes en tí\n")
            else:
                print(f"\nParece ser que {nom_ligue} no ha disfrutado de la charla\n")
    else:
        print (f"\nParece ser que {nom_ligue} no esta disponible\n")

def dormir():
    global dias, energia, hablar_ligue_uso, hablar_uso
    sleep(1)
    dias += 1
    energia = 100
    hablar_uso = False
    hablar_ligue_uso = False

#Hub
def game():
    global dias,energia,dinero,nv_carisma,hablar_uso,dax_chance,ligue,nom_ligue,nv_carisma_ligue,estado_relacion,estado_relacion_xp,ligue_chance,hablar_ligue_uso,fin_juego
    while True:
        print(f"Día {dias}")
        print(f"Stats:\nEnergia: {energia}\nDinero: ${dinero}\nNv. de Carisma: {nv_carisma}")
        hub = input("\nSelecciona lo que quieres realizar:\n1.- Trabajar (-50 de Energia, +50 de Dinero)\n2.- Hablar con Dax (+1 Nv. de Carsima (Solo una vez por día))\n3.- Salir de Fiesta (-30 de Energia, -20 de Dinero)\n4.- Ir a la Tienda\n5.- Ligue\n6.- Dormir (Pasa al Sig. Día y Restablece Toda la Energia)\n7.- Guardar Partida\n8.- Volver al Menú\n")

        match hub:
            case "1":
                trabajar()
            case "2":
                if hablar_uso == False:
                    hablar()
                    hablar_uso = True
                elif hablar_uso == True and dax_chance[0] == True:
                    print("\nParece ser que ya has hablado con Dax\n")
                elif hablar_uso == True and dax_chance[0] == False:
                    print("\nParece ser que Dax no esta disponible\n")
                elif hablar_uso == True or hablar_uso == False and nv_carisma == 10:
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
                dormir()
                if dias == 50 and dinero < 2000:
                    bad_ending()
                    print("\nNo tienes el dinero suficiente para ejecutar el Plan De Lester, Perdiste el Juego\n")
                    save()
                    break
                elif dias == 50 and dinero >= 2000:
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
                if fin_juego == True and dias == 50 and dinero > 2000 and primer_beso == False:
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