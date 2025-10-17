import speech_recognition as sr


# Usa el microfono para escuchar y luego retorna lo escuchado en formato de texto
def listen_assistant() -> str:
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source, duration=1)

    print('Escuchando...')

    with mic as source:
        audio = r.listen(source)

    # Trata de devolver el audio recibido como un texto
    try:
        text = r.recognize_google(audio, language='es-ES').lower()

        return text
    # Si no se escucha nada devuelve un texto vacio
    except sr.UnknownValueError:
        return ""
    # Si sucede algun problema lo muestra
    except sr.RequestError as e:
        print("⚠️ Error al tratar con el servicio:", e)
        return "Hubo un error con el servicio de reconocimiento"