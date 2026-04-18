# output.py
# Canal único de salida de texto del juego.
# msg()      → texto directo (uso interno/legado)
# msg_key()  → texto desde dialogos.json["msgs"]
# escena()   → dispara una escena completa desde dialogos.json

import json
import os

_msg_handler   = print   # por defecto imprime en consola
_scene_handler = None    # registrado por la GUI
_dialogos      = None    # caché del JSON

def _get_dialogos():
    global _dialogos
    if _dialogos is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(base_dir, "dialogos.json"), encoding="utf-8") as f:
            _dialogos = json.load(f)
    return _dialogos

# ── Registrar handlers ──────────────────────────────────────────────────────
def set_handler(fn):
    """Reemplaza el canal de salida de mensajes (llamado por la GUI)."""
    global _msg_handler
    _msg_handler = fn

def set_scene_handler(fn):
    """Registra el handler que la GUI usa para iniciar escenas."""
    global _scene_handler
    _scene_handler = fn

# ── Enviar mensajes ─────────────────────────────────────────────────────────
def msg(texto: str):
    #Mostrar Mensaje en el GUI
    if _msg_handler:
        _msg_handler(texto.strip())

def msg_key(clave: str, **params):
    #Mostrar Mensaje en el GUI desde el JSON
    texto = _get_dialogos()["msgs"].get(clave, f"[{clave}]")
    if params:
        texto = texto.format(**params)
    msg(texto)

# ── Disparar escenas ────────────────────────────────────────────────────────
def escena(clave: str, **params):
    #Mostrar Escenas en el GUI desde el JSON
    if _scene_handler:
        _scene_handler(clave, params)
