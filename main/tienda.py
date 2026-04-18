import output

class Tienda:
    def __init__(self, items):
        self.items = items
    
    def mostrar_items(self):
        for i, item in enumerate(self.items):
            output.msg(f"{i + 1}. {item.nombre} - Precio: ${item.precio} - {item.descripcion}")

    def comprar_item(self, personaje, item_index):
        if 0 <= item_index < len(self.items):
            item = self.items[item_index]
            if personaje.dinero >= item.precio:
                personaje.dinero -= item.precio
                item.usar(personaje)
                output.msg_key("tienda_compra_ok", item=item.nombre)
            else:
                output.msg_key("tienda_sin_dinero")
        else:
            output.msg_key("tienda_sin_dinero")

    def tienda_menu(self, personaje):
        while True:
            self.mostrar_items()
            seleccion = input("\nSelecciona un producto o escribe S para salir:\n")
            
            match seleccion:
                case "S" | "s":
                    output.msg_key("cajero_despedida")
                    break
                
                case _:
                    try:
                        item_index = int(seleccion) - 1
                        self.comprar_item(personaje, item_index)
                    except ValueError:
                        output.msg_key("hub_opcion_invalida")