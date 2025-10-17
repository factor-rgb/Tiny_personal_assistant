import unicodedata
import re


# normaliza una cadena de texto, elimina tildes y caracteres no alfanumericos
def normalize(text: str) -> str:
    # Normaliza a forma NFD (descompone caracteres en base + tilde)
    text = unicodedata.normalize('NFD', text)
    # Elimina las marcas diacríticas (tildes, diéresis, etc.)
    text = re.sub(r'[\u0300-\u036f]', '', text)
    # Eliminar caracteres no alfanuméricos
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.lower()