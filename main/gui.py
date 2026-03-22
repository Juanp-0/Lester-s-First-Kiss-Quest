import tkinter as tk
from tkinter import font
import json
import os
import main

# ─── Cargar el JSON ────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, "dialogos.json"), encoding="utf-8") as f:
    DIALOGOS = json.load(f)

# ─── App ───────────────────────────────────────────────────────────────────────
app = tk.Tk()
app.title("Lester's First Kiss Quest")
app.geometry("500x350")

# ─── Estado del juego ──────────────────────────────────────────────────────────
escena_actual = []   # lista de entradas de la escena en curso
indice = [0]         # usamos lista para poder modificarlo dentro de funciones
timer_id = [None]    # ID del after() en curso, para poder cancelarlo

# ─── Función para cambiar de frame ────────────────────────────────────────────
def mostrar(frame):
    for f in (frame_menu, frame_escenas, frame_hub):
        f.pack_forget()
    if frame == frame_hub:
        actualizar_gui()
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

    if tipo == "separador":
        msg_texto.config(text=texto, font=separador_font)
    elif tipo == "narracion":
        msg_texto.config(text=texto, font=narrador_font)
    elif tipo == "dialogo":
        personaje = entrada["personaje"]
        msg_texto.config(text=f'{personaje}: {texto}', font=dialogo_font)

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

lbl_dia = tk.Label(frame_hub, justify="left")
lbl_dia.pack(pady=(10, 15))

lbl_energia = tk.Label(frame_hub, justify="left")
lbl_energia.pack(pady=(10, 15))

lbl_dinero = tk.Label(frame_hub, justify="left")
lbl_dinero.pack(pady=(10, 15))

lbl_carisma = tk.Label(frame_hub, justify="left")
lbl_carisma.pack(pady=(10, 15))

btn_trabajar = tk.Button(
    frame_hub,
    text="Trabajar",
    command=lambda: [main.lester.trabajar(), actualizar_gui()],
    pady=5
)
btn_trabajar.pack(pady=10)

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

btn_dormir = tk.Button(
    frame_hub,
    text="Dormir",
    command=accion_dormir,
    pady=5
)
btn_dormir.pack(pady=10)

btn_guardar = tk.Button(
    frame_hub,
    text="Guardar",
    command=lambda: main.save(),
    pady=5
)
btn_guardar.pack(pady=10)

btn_volver = tk.Button(
    frame_hub,
    text="Volver al Menú",
    command=lambda: mostrar(frame_menu),
    pady=5
)
btn_volver.pack(pady=10)

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
    wraplength=460
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
