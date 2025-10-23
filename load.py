from actions import ACTIONS
import  world_image

def secundari_load():
    """Generador que ejecuta una acción por iteración."""
    for obj in ACTIONS:
        world_image.areas[obj[0]] = obj[1]()
        yield  # Pausa hasta la siguiente llamada