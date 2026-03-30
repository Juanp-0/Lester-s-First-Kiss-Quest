from random import choice
import output

nom_chicas = ["Romina", "Ariana", "Julieta", "María", "Maya", "Erika", "Sofía", "Carla", "Debanhi", "Deborah", "Katia", "Serena", "Ramona", "Ana", "Alejandra", "Tondelaya", "Victoria", "Nereida", "Violeta", "Fernanda", "Catalina"]
nv_carisma_chicas = [1,2,3,4,5,6,7,8,9,10]
nv_carisma_mayor = ["Si", "No", "No", "No", "Flechazo"]
nv_carisma_igual = ["Si", "Si", "No", "No", "Flechazo"]
nv_carisma_menor = ["Si", "Si", "Si", "No", "Flechazo"]

def generar_chicas(cant):
    from ligue import Ligue
    chicas = []
    for chica in range(cant):
        nombre = choice(nom_chicas)
        nv_carisma = choice(nv_carisma_chicas)
        chica = Ligue(nombre, nv_carisma, 0)
        chicas.append(chica)
    return chicas

def mostrar_chicas(chicas):
    for i, chica in enumerate(chicas, start=1):
        output.msg(f"{i}.- {chica.nombre}\nNivel de Carisma: {chica.nv_carisma}")

def ligue_exito(personaje, chica):
    global tener_ligue, primer_beso 
    if personaje.nv_carisma > chica.nv_carisma:
        eleccion = choice(nv_carisma_mayor)
    elif personaje.nv_carisma == chica.nv_carisma:
        eleccion = choice(nv_carisma_igual)
    else:
        eleccion = choice(nv_carisma_menor)
    
    if eleccion == "Si":
        tener_ligue = True
        chica.estado_relacion_xp = 5
        output.msg("Parece que tus habilidades de carisma, fueron efectivas")
    elif eleccion == "Flechazo":
        tener_ligue = True
        primer_beso = True
        chica.estado_relacion_xp = 21
        output.msg("Parece que tus habilidades de carisma, fueron superefectivas, tanto que acabas de dar tu primer beso")
    else:
        output.msg("Parece que tus habilidades de carisma, no fueron efectivas")

    
def chicas(personaje):
    chicas = generar_chicas(3)
    mostrar_chicas(chicas)
    seleccion = input("Selecciona a la chica con la que quieres intentar ligar (1, 2 o 3):\n")
    try:
        chica_index = int(seleccion) - 1
        if 0 <= chica_index < len(chicas):
            ligue_exito(personaje, chicas[chica_index])
        else:
            output.msg("Selecciona una opción válida")
    except ValueError:
        output.msg("Selecciona una opción válida")