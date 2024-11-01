# respuestas = {
#     "hola": "¡Hola! ¿En qué puedo ayudarte?",
#     "como estas": "Estoy bien, gracias por preguntar.",
#     "adios": "¡Hasta luego! Que tengas un buen día.",
# }
import csv
respuestas = {}

# with open("datosdechat.csv", "r") as archivo:
#     lector = csv.DictReader(archivo)
#     for fila in lector:
#         respuestas[fila["pregunta"]] = fila["respuesta"]
        

def obtener_respuesta(mensaje):
    mensaje = mensaje.lower()
    if mensaje in respuestas:
        return respuestas[mensaje]
    else:
        with open("salida.csv", "a", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([mensaje, "Pregunta por responder"])
        return "Lo siento, no entiendo esa pregunta."
    
print("¡Hola! Soy un chatbot. Escribe 'salir' para terminar la conversación")
while True:
    usuario = input("Tú: ")
    if usuario.lower() == "salir":
        print("Chatbot: ¡Adiós!")
        break
    respuesta = obtener_respuesta(usuario)
    print("Chatbot: ", respuesta)