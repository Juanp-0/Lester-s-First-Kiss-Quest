#Lester's First Kiss Quest

import json
from personaje import Personaje
from ligue import Ligue
from item import Item, EnergItem, CarismaItem
from tienda import Tienda
import output

#Stats
dias = 1

#Factores RNG
dax_chance = [True, False]


#Verificadores
hablar_uso = False
dax_disponible = True  
tener_ligue = False
hablar_ligue_uso = False
primer_beso = False
fin_juego = False

tienda = Tienda([EnergItem("Bebida Energetíca", 20, 20, "+20 de Energia"), EnergItem("Café Enbotellado", 15, 10, "+10 de Energia"), CarismaItem("Perfume", 150, 1, "+1 Nv. de Carisma")])
lester = Personaje(100, 0, 0)
ligue = Ligue(None, 0, 0)

#Sistema de Guardado
def newgame():
    global dias, hablar_uso, hablar_ligue_uso, fin_juego, lester, ligue, tener_ligue, primer_beso, dax_disponible
    # Reiniciar variables globales
    dias = 1
    hablar_uso = False
    dax_disponible = True
    hablar_ligue_uso = False
    fin_juego = False
    tener_ligue = False
    primer_beso = False

    # Recrear personajes con valores iniciales
    lester = Personaje(100, 0, 0)
    ligue = Ligue(None, 0, 0)

    # Guardar estado inicial
    save_data = {
        "dias": 1,
        "energia": 100,
        "dinero": 0,
        "nv_carisma": 0,
        "hablar_uso": False,
        "dax_disponible": True,
        "tener_ligue": False,
        "primer_beso": False,
        "nom_ligue": None,
        "nv_carisma_ligue": 0,
        "estado_relacion_xp": 0,
        "hablar_ligue_uso": False,
        "fin_juego": False
    }
    with open("lester_sav.json", "w") as new_game:
        json.dump(save_data, new_game)

def load():
    global dias, hablar_uso, tener_ligue, primer_beso, hablar_ligue_uso, fin_juego, lester, ligue, dax_disponible
    try:
        with open("lester_sav.json", "r") as load_game:
            save_data = json.load(load_game)
            # Restaurar variables globales
            dias = save_data["dias"]
            hablar_uso = save_data["hablar_uso"]
            dax_disponible = save_data.get("dax_disponible", True)  # Compatible con guardos antiguos
            tener_ligue = save_data["tener_ligue"]
            primer_beso = save_data["primer_beso"]
            hablar_ligue_uso = save_data["hablar_ligue_uso"]
            fin_juego = save_data["fin_juego"]

        # Crear personaje con stats guardados
        lester = Personaje(save_data["energia"], save_data["dinero"], save_data["nv_carisma"])
        ligue = Ligue(save_data["nom_ligue"], save_data["nv_carisma_ligue"], save_data["estado_relacion_xp"])
        
        output.msg_key("juego_guardado")
        return True
    except FileNotFoundError:
        output.msg_key("no_guardado")
        return False

def save():
    save_data = {
        "dias": dias,
        "energia": lester.energia,
        "dinero": lester.dinero,
        "nv_carisma": lester.nv_carisma,
        "hablar_uso": hablar_uso,
        "dax_disponible": dax_disponible,
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
    output.msg_key("juego_guardado")

if __name__ == "__main__":
    print("Corriendo Juego.")