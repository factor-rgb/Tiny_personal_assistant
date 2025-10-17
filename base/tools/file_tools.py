import json
from pathlib import Path


# Crea la ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Obtiene un dato almacenado en data.json
def get_data(key: str) -> str:
    try:
        file = open(BASE_DIR / "files/data.json", "r")
        value = json.load(file)[key]
        file.close()
        return value
    except FileNotFoundError:
        set_data(key)
        return get_data(key)

# Establece/modifica un dato almacenado en data.json o crea el archivo
def set_data(key: str, value: str = 'default') -> None:
    try:
        archivo = open(BASE_DIR / "files/data.json", "r")
        data = json.load(archivo)
        data[key] = value
        archivo = open(BASE_DIR / "files/data.json", "w")
        json.dump(data, archivo, indent=4)
        archivo.close()
    except FileNotFoundError:
        archivo = open(BASE_DIR / "files/data.json", "w")
        data = {key: value}
        json.dump(data, archivo, indent=4)
        archivo.close()