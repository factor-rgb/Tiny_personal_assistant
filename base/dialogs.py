from tools.file_tools import get_data
import random
import datetime


# Devuelve la hora y los minutos actuales
def get_time_now() -> str:
    time = datetime.datetime.now()
    time = time.strftime("%H:%M")
    return time

# Da la Bienvenida dependiendo de la hora
def welcome() -> str:
    time = datetime.datetime.now()
    hour = time.hour

    if 5<= hour < 12:
        return f"Buenos dias {get_data('user')}"
    elif 12 <= hour < 18:
        return f"Buenas tarder {get_data('user')}"
    else:
        return f"Buenas noches {get_data('user')}"

# Se presenta o presenta a alguien/algo registrado
def introduce(request: str) -> str:
    if request.__contains__('presentate'):
        return 'Buenas soy tu mini asistente personal te asistire en tareas simples'
    elif request.__contains__('tu creador'):
        return 'es alguien que me creo para asistir y ayudar'
    else:
        return 'No reconozco a ese individuo o dato'

# Devuelve un string aleatorio dependiendo de la peticion
def get_random_answer(request: str) -> str:
    match(request):
        case "confirmation":
            answers = (f'Entendido {get_data('user')}',
                        f'Enseguida {get_data('user')}',
                        f'Por supuesto {get_data('user')}',
                        'OK',
                        'De acuerdo',
                        'Entendido'
                        )
        case "joke":
            answers = ('que le dijo un pez a otro pez, glu glu', 
                       'por que la gallina cruzo el camino, para escapar de la granja'
                       )
    return random.choice(answers)