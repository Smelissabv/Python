respuestas = {
    "hola": "¡Hola! ¿En qué puedo ayudarte?",
    "como estas": "Estoy bien, gracias por preguntar.",
    "adios": "¡Hasta luego! Que tengas un buen día.",
}

def obtener_respuesta(mensaje):
    mensaje = mensaje.lower()
    print(mensaje)
    print(respuestas[mensaje])
    if mensaje in respuestas:
        return respuestas[mensaje]
    else:
        return "Lo siento, no entiendo esa pregunta."
    
print("¡Hola! Soy un chatbot. Escribe 'salir' para terminar la conversación")
while True:
    usuario = input("Tú: ")
    if usuario.lower() == "salir":
        print("Chatbot: ¡Adiós!")
        break
    respuesta = obtener_respuesta(usuario)
    print("Chatbot: ", respuesta)