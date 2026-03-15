class Tienda:
    def __init__(self, items):
        self.items = items
    
    def mostrar_items(self):
        for i, item in enumerate(self.items):
            print(f"{i + 1}. {item.nombre} - Precio: ${item.precio}")

    def comprar_item(self, personaje, item_index):
        if 0 <= item_index < len(self.items):
            item = self.items[item_index]
            if personaje.dinero >= item.precio:
                personaje.dinero -= item.precio
                item.usar(personaje)
                print(f"\nHas comprado {item.nombre} y lo has usado\n")
            else:
                print("\nNo tienes suficiente dinero para comprar este item\n")
        else:
            print("\nÍndice de item no válido\n")

    def tienda_menu(self, personaje):
        while True:
            self.mostrar_items()
            seleccion = input("\nSelecciona un producto o escribe S para salir:\n")
            
            match seleccion:
                case "S" | "s":
                    print("\nCajero: ¡Gracias por comprar! ¡Vuelva pronto!\n")
                    break
                
                case _:
                    try:
                        item_index = int(seleccion) - 1
                        self.comprar_item(personaje, item_index)
                    except ValueError:
                        print("Selecciona una opción válida\n")    