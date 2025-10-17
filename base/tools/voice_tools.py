from multiprocessing import Process
import pyttsx3


# Crea el motor para que el asistente hable
def speak_process(text: str) -> None:
    try:
        # Crea la instancia
        engine = pyttsx3.init()
        # Establece que tan rapidp habla
        engine.setProperty('rate', 150)
        # Establece que tan alto habla (entre 0 y 1)
        engine.setProperty('volume', 0.9)
        # Establece la voz 
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        # Pronuncia el texto ingresado
        engine.say(text)
        engine.runAndWait()
        # Detiene el motor
        engine.stop()
    except Exception as e:
        print("Error en TTS:", e)

# Usa process para evitar problemas al ejecutar el motor varias veces
def speak_async(text: str) -> None:
    p = Process(target=speak_process, args=(text,))
    p.daemon = True
    p.start()