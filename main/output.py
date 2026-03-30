# output.py
# Canal único de salida de texto del juego.
# Por defecto imprime en consola; la GUI lo reemplaza para mostrar popups.

_handler = print   # función actualmente activa
_silent  = False   # cuando True, los mensajes se descartan silenciosamente

def msg(texto: str) -> None:
    """Muestra un mensaje al jugador a través del canal activo."""
    if not _silent:
        _handler(texto.strip())

def set_handler(fn) -> None:
    """Reemplaza el canal de salida (llamado por la GUI al arrancar)."""
    global _handler
    _handler = fn

def set_silent(silencio: bool) -> None:
    """Activa o desactiva el modo silencioso."""
    global _silent
    _silent = silencio
