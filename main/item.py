class Item:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def usar(self, personaje):
        pass
    
class EnergItem(Item):
    def __init__(self, nombre, precio, energia_restaurada):
        super().__init__(nombre, precio)
        self.energia_restaurada = energia_restaurada

    def usar(self, personaje):
        personaje.sumEnergia(self.energia_restaurada)

class CarismaItem(Item):
    def __init__(self, nombre, precio, carisma_aumentada):
        super().__init__(nombre, precio)
        self.carisma_aumentada = carisma_aumentada

    def usar(self, personaje):
        personaje.nv_carisma += self.carisma_aumentada