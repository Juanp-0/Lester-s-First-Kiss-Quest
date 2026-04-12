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
    for _ in range(cant):
        nombre = choice(nom_chicas)
        nv_carisma = choice(nv_carisma_chicas)
        chicas.append(Ligue(nombre, nv_carisma, 0))
    return chicas

def ligue_exito(personaje, chica):
    """Intenta ligar con la chica seleccionada. Actualiza main directamente."""
    import main as _main
    if personaje.nv_carisma > chica.nv_carisma:
        eleccion = choice(nv_carisma_mayor)
    elif personaje.nv_carisma == chica.nv_carisma:
        eleccion = choice(nv_carisma_igual)
    else:
        eleccion = choice(nv_carisma_menor)

    if eleccion == "Si":
        _main.tener_ligue = True
        _main.ligue = chica
        chica.estado_relacion_xp = 5
        output.msg(f"Parece que tus habilidades de carisma fueron efectivas. ¡{chica.nombre} es tu nuevo ligue!")
    elif eleccion == "Flechazo":
        _main.tener_ligue = True
        _main.primer_beso = True
        _main.ligue = chica
        chica.estado_relacion_xp = 21
        output.msg(f"¡Flechazo! {chica.nombre} y tú se besaron. ¡Diste tu primer beso!")
    else:
        output.msg(f"Parece que tus habilidades de carisma no fueron suficientes con {chica.nombre}.")