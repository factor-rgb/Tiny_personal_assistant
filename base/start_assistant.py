# Herramientas
from tools.voice_tools import speak_async
from tools.text_tools import normalize
from tools.file_tools import set_data, get_data
# Devolver strings
from get_petition import listen_assistant
from dialogs import introduce, get_random_answer, welcome, get_time_now
# funcionalidades
from search_pages import Search_pages
import time


def main():
    # Consigue el nombre del asistente
    ASSIST_NAME = get_data('assistant')

    # Da la Bienvenida
    speak_async(f'{welcome()}, soy {ASSIST_NAME} como puedo ayudarte')

    # Inicia y ejecuta el bucle hasta que se indique terminarlo
    while True:
        petition = listen_assistant()
        norm_petition = normalize(petition)

        # Cuando se diga el nombre del asistente se procesa la peticion
        if ASSIST_NAME in petition:
            # Abre una o varias ventana en el navegador a peticion
            if norm_petition.__contains__('busca') or norm_petition.__contains__('abre la pagina') or norm_petition.__contains__('abre youtube'):
                succes = Search_pages(petition)
                if succes:
                    speak_async(get_random_answer('confirmation'))
            # Se presenta o presenta a alguien
            elif norm_petition.__contains__('presenta') or norm_petition.__contains__('quien'):
                speak_async(introduce(norm_petition))
            # cuanta un chiste
            elif norm_petition.__contains__('dime un') or norm_petition.__contains__('cuentame un') and norm_petition.__contains__('chiste'):
                speak_async(get_random_answer('joke'))
            # Da la hora
            elif norm_petition.__contains__('dime la hora') or norm_petition.__contains__('hora es'):
                speak_async(f"son las {get_time_now()}")
            # Modifica el nombre del usuario o el nombre del asistente
            elif norm_petition.__contains__('cambia'):
                key = ""
                if norm_petition.__contains__('usuario'):
                    key = "user"
                elif norm_petition.__contains__('tu nombre'):
                    key = "assistant"
                speak_async('cual sera el nuevo nombre')
                time.sleep(2)
                new_name = normalize(listen_assistant())
                if new_name:
                    if key == 'user':
                        speak_async(f'quieres que te llame {new_name}')
                    else:
                        speak_async(f'quieres llamarme {new_name}')
                    while True:
                        confir = normalize(listen_assistant())
                        if 'si' in confir:
                            speak_async(f'entendido el nuevo nombre sera {new_name}')
                            set_data(key, new_name)
                            ASSIST_NAME = get_data('assistant')
                            break
                        elif 'no' in confir:
                            speak_async('Cambio cancelado')
                            break
                else:
                    speak_async('lo lamento no escuche')
            # Detiene el bucle
            elif norm_petition.__contains__('suficiente') or norm_petition.__contains__('adios'):
                speak_async('muy bien que tenga un buen rato')
                print('muy bien que tenga un buen rato')
                time.sleep(6)
                break
        # Si no se llama al asistente sigue escuchando
        print('')

if __name__ == "__main__":
    main()