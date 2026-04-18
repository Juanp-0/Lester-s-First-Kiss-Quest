class Item:
    def __init__(self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def usar(self, personaje):
        pass
    
class EnergItem(Item):
    def __init__(self, nombre, precio, energia_restaurada, descripcion):
        super().__init__(nombre, precio, descripcion)
        self.energia_restaurada = energia_restaurada

    def usar(self, personaje):
        personaje.sumEnergia(self.energia_restaurada)

class CarismaItem(Item):
    def __init__(self, nombre, precio, carisma_aumentada, descripcion):
        super().__init__(nombre, precio, descripcion)
        self.carisma_aumentada = carisma_aumentada

    def usar(self, personaje):
        personaje.nv_carisma += self.carisma_aumentada