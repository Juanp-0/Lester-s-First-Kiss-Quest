import tkinter as tk
from tkinter import font
import json
import os
import main
import output

# ─── Cargar el JSON ────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, "dialogos.json"), encoding="utf-8") as f:
    DIALOGOS = json.load(f)

# ─── Redirigir mensajes de juego a la GUI ─────────────────────────────────────
def mostrar_como_escena(texto: str):
    """Inserta el mensaje en la cola de la escena activa y la reproduce."""
    escena_actual.insert(indice[0], {"tipo": "mensaje", "texto": texto.strip()})
    # Si la pantalla de escenas no está visible, activarla primero
    if not frame_escenas.winfo_ismapped():
        mostrar(frame_escenas)
    mostrar_siguiente()

output.set_handler(mostrar_como_escena)

# ─── App ───────────────────────────────────────────────────────────────────────
app = tk.Tk()
app.title("Lester's First Kiss Quest")
app.geometry("500x450")

# ─── Estado del juego ──────────────────────────────────────────────────────────
escena_actual = []   # lista de entradas de la escena en curso
indice = [0]         # usamos lista para poder modificarlo dentro de funciones
timer_id = [None]    # ID del after() en curso, para poder cancelarlo

# ─── Función para cambiar de frame ────────────────────────────────────────────

def mostrar(frame):
    for f in (frame_menu, frame_escenas, frame_hub, frame_tienda, frame_ligue):
        f.pack_forget()
    if frame == frame_hub:
        actualizar_gui()
    elif frame == frame_ligue:
        actualizar_ligue()
    frame.pack(fill="both", expand=True)

# ─── Función principal: cargar y reproducir una escena ────────────────────────
def iniciar_escena(nombre_escena):
    global escena_actual
    escena_actual = DIALOGOS[nombre_escena]
    indice[0] = 0
    mostrar(frame_escenas)
    mostrar_siguiente()

def cancelar_timer():
    if timer_id[0] is not None:
        app.after_cancel(str(timer_id[0]))
        timer_id[0] = None

DELAY_MS = 2000

# ─── Fonts globales ────────────────────────────────────────────────────────────
separador_font = font.Font(slant="italic")
narrador_font  = font.Font(weight="bold")
dialogo_font   = font.Font(slant="roman")
mensaje_font   = font.Font(weight="bold", slant="italic")

def mostrar_siguiente():
    cancelar_timer()

    if indice[0] >= len(escena_actual):
        # Escena terminada → pasar a Hub automáticamente
        msg_texto.config(text="")
        msg_personaje.config(text="")
        mostrar(frame_hub)
        return

    entrada = escena_actual[indice[0]]
    tipo  = entrada["tipo"]
    texto = entrada["texto"].replace("\n", " ")

    separador_font = font.Font(slant="italic")
    narrador_font = font.Font(weight="bold")
    dialogo_font = font.Font(slant="roman")
    mensaje_font = font.Font(weight="bold", slant="italic")

    if tipo == "separador":
        msg_texto.config(text=texto, font=separador_font)
    elif tipo == "narracion":
        msg_texto.config(text=texto, font=narrador_font)
    elif tipo == "dialogo":
        personaje = entrada["personaje"]
        msg_texto.config(text=f'{personaje}: {texto}', font=dialogo_font)
    elif tipo == "mensaje":
        msg_texto.config(text=texto, font=mensaje_font)

    indice[0] += 1
    # Programar el siguiente diálogo automáticamente
    timer_id[0] = app.after(DELAY_MS, mostrar_siguiente)

# ─── Pantalla Menú ─────────────────────────────────────────────────────────────
frame_menu = tk.Frame(app)

tk.Label(
    frame_menu,
    text="Lester's First Kiss Quest",
).pack(pady=(30, 15))

tk.Button(
    frame_menu, text="Nuevo Juego",
    command=lambda: [main.newgame(), iniciar_escena("intro")]
).pack(pady=5)

tk.Button(
    frame_menu, text="Cargar Partida",
    command=lambda: [main.load(), mostrar(frame_hub)]
).pack(pady=5)

tk.Button(
    frame_menu, text="Salir del Juego",
    command=app.quit,
).pack(pady=5)

# ─── Pantalla HUB ─────────────────────────────────────────────────────────────
frame_hub = tk.Frame(app)

def actualizar_gui():
    lbl_dia.config(text=f"Día {main.dias}")
    lbl_energia.config(text=f"Energia: {main.lester.energia}")
    lbl_dinero.config(text=f"Dinero: ${main.lester.dinero}")
    lbl_carisma.config(text=f"Nv. de Carisma: {main.lester.nv_carisma}")

# ── Stats ─────────────────────────────────────────────────────────────────────
lbl_dia     = tk.Label(frame_hub, justify="left")
lbl_energia = tk.Label(frame_hub, justify="left")
lbl_dinero  = tk.Label(frame_hub, justify="left")
lbl_carisma = tk.Label(frame_hub, justify="left")

lbl_dia    .pack(pady=(10, 2))
lbl_energia.pack(pady=2)
lbl_dinero .pack(pady=2)
lbl_carisma.pack(pady=(2, 10))

# ── Botones (grid 2 columnas) ──────────────────────────────────────────────────
frame_botones = tk.Frame(frame_hub)
frame_botones.pack(pady=10)

frame_botones.columnconfigure(0, weight=1, minsize=140)
frame_botones.columnconfigure(1, weight=1, minsize=140)

def accion_hablar_dax():
    main.hablar_uso, main.dax_disponible = main.lester.hablar(main.dax_chance, main.hablar_uso, main.dax_disponible)
    actualizar_gui()

def accion_dormir():
    main.dias = main.lester.dormir(main.dias)
    main.hablar_uso = False
    main.dax_disponible = True
    if main.dias == 50 and main.lester.dinero < 2000:
        main.save()
    elif main.dias == 50 and main.lester.dinero >= 2000:
        main.save()
    elif main.primer_beso == True:
        main.save()
    actualizar_gui()

def accion_ir_tienda():
    mostrar(frame_tienda)

def checar_ligue():
    if main.tener_ligue == True:
        mostrar(frame_ligue)
    else:
        output.msg("No tienes un ligue")

btn_trabajar  = tk.Button(frame_botones, text="Trabajar",       command=lambda: [main.lester.trabajar(), actualizar_gui()], pady=5)
btn_hablar_dax = tk.Button(frame_botones, text="Hablar con Dax", command=accion_hablar_dax,          pady=5)
btn_dormir    = tk.Button(frame_botones, text="Dormir",          command=accion_dormir,              pady=5)
btn_tienda    = tk.Button(frame_botones, text="Ir a la Tienda",  command=accion_ir_tienda,           pady=5)
btn_ligue     = tk.Button(frame_botones, text="Ligue",  command=checar_ligue,           pady=5)
btn_guardar   = tk.Button(frame_botones, text="Guardar",         command=lambda: main.save(),        pady=5)
btn_volver    = tk.Button(frame_botones, text="Volver al Menú",  command=lambda: mostrar(frame_menu), pady=5)

btn_trabajar  .grid(row=0, column=0, padx=10, pady=6, sticky="ew")
btn_hablar_dax.grid(row=0, column=1, padx=10, pady=6, sticky="ew")
btn_dormir    .grid(row=1, column=0, padx=10, pady=6, sticky="ew")
btn_tienda    .grid(row=1, column=1, padx=10, pady=6, sticky="ew")
btn_ligue     .grid(row=2, column=0, padx=10, pady=6, sticky="ew")
btn_guardar   .grid(row=2, column=1, padx=10, pady=6, sticky="ew")
btn_volver    .grid(row=3, column=0, padx=10, pady=6, sticky="ew")

# ─── Pantalla Tienda ──────────────────────────────────────────────────────────
frame_tienda = tk.Frame(app)

tk.Label(
    frame_tienda,
    text="Tienda",
).pack(pady=(20, 10))

lbl_tienda_msg = tk.Label(
    frame_tienda,
    text="",
    wraplength=420,
    justify="center",
    font=mensaje_font,
)
lbl_tienda_msg.pack(pady=(0, 8))

def hacer_accion_compra(indice_item):
    def accion():
        # Capturar el mensaje de compra sin salir de la tienda
        mensajes = []
        output.set_handler(mensajes.append)
        main.tienda.comprar_item(main.lester, indice_item)
        output.set_handler(mostrar_como_escena)  # restaurar handler normal

        lbl_tienda_msg.config(text=mensajes[0] if mensajes else "")
        lbl_dinero.config(text=f"Dinero: ${main.lester.dinero}")
        lbl_energia.config(text=f"Energia: {main.lester.energia}")
        lbl_carisma.config(text=f"Nv. de Carisma: {main.lester.nv_carisma}")
    return accion

for i, item in enumerate(main.tienda.items):
    tk.Button(
        frame_tienda,
        text=f"{item.nombre}  —  ${item.precio}  —  {item.descripcion}",
        command=hacer_accion_compra(i),
        pady=5,
    ).pack(pady=5, fill="x", padx=40)

def accion_volver_hub():
    mostrar(frame_hub)

tk.Button(
    frame_tienda,
    text="Volver al Hub",
    command=accion_volver_hub,
    pady=5,
).pack(pady=15)
# ─── Pantalla Ligue ──────────────────────────────────────────────────────────
frame_ligue = tk.Frame(app)

def actualizar_ligue():
    nombre = main.ligue.nombre or "???"
    btn_hablar_ligue.config(text=f"Hablar con {nombre}")
    btn_cita_ligue  .config(text=f"Cita con {nombre}")

btn_hablar_ligue = tk.Button(frame_ligue, text="Hablar con ligue", command=lambda: main.ligue.hablar_ligue(main.lester), pady=5)
btn_cita_ligue   = tk.Button(frame_ligue, text="Cita con ligue",   command=lambda: main.ligue.cita(main.lester),         pady=5)
btn_volver_hub   = tk.Button(frame_ligue, text="Volver al Hub",    command=accion_volver_hub,                            pady=5)

btn_hablar_ligue.pack(pady=6)
btn_cita_ligue  .pack(pady=6)
btn_volver_hub  .pack(pady=6)

# ─── Pantalla Citas ──────────────────────────────────────────────────────────
frame_citas = tk.Frame(app)

def actualizar_citas():
    nombre = main.ligue.nombre or "??"
    btn_cine.config(text=f"Cine con {nombre}")
    btn_parque.config(text=f"Parque con {nombre}")
    btn_restaurante.config(text=f"Restaurante con {nombre}")

btn_cine = tk.Button(frame_citas, text="Cine", command=lambda: main.ligue.cita(main.lester, "cine"), pady=5)
btn_parque = tk.Button(frame_citas, text="Parque", command=lambda: main.ligue.cita(main.lester, "parque"), pady=5)
btn_restaurante = tk.Button(frame_citas, text="Restaurante", command=lambda: main.ligue.cita(main.lester, "restaurante"), pady=5)
btn_volver_hub = tk.Button(frame_citas, text="Volver al Hub", command=accion_volver_hub, pady=5)

btn_cine.pack(pady=6)
btn_parque.pack(pady=6)
btn_restaurante.pack(pady=6)
btn_volver_hub.pack(pady=6)

# ─── Pantalla Escenas ──────────────────────────────────────────────────────────
frame_escenas = tk.Frame(app)

msg_personaje = tk.Message(
    frame_escenas,
    text="",
    anchor="w"
)
msg_personaje.pack(fill="x", padx=20, pady=(20, 5))

msg_texto = tk.Label(
    frame_escenas,
    text="",
    justify="left",
    anchor="nw",
    wraplength=460,
)
msg_texto.pack(fill="both", expand=True, padx=20)

# Actualizar wraplength cuando cambie el tamaño de la ventana
def actualizar_wraplength(event):
    msg_texto.config(wraplength=event.width - 40)
frame_escenas.bind("<Configure>", actualizar_wraplength)

# ─── Arrancar ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    mostrar(frame_menu)
    app.mainloop()
