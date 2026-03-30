import output

class Tienda:
    def __init__(self, items):
        self.items = items
    
    def mostrar_items(self):
        for i, item in enumerate(self.items):
            output.msg(f"{i + 1}. {item.nombre} - Precio: ${item.precio}")

    def comprar_item(self, personaje, item_index):
        if 0 <= item_index < len(self.items):
            item = self.items[item_index]
            if personaje.dinero >= item.precio:
                personaje.dinero -= item.precio
                item.usar(personaje)
                output.msg(f"Has comprado {item.nombre} y lo has usado")
            else:
                output.msg("No tienes suficiente dinero para comprar este item")
        else:
            output.msg("Índice de item no válido")

    def tienda_menu(self, personaje):
        while True:
            self.mostrar_items()
            seleccion = input("\nSelecciona un producto o escribe S para salir:\n")
            
            match seleccion:
                case "S" | "s":
                    output.msg("Cajero: ¡Gracias por comprar! ¡Vuelva pronto!")
                    break
                
                case _:
                    try:
                        item_index = int(seleccion) - 1
                        self.comprar_item(personaje, item_index)
                    except ValueError:
                        output.msg("Selecciona una opción válida")    