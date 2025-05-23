import random
from datetime import datetime

emociones = {
    "feliz": ["alegre", "contento", "satisfecho", "optimista","emocionado", "entusiasmado", "eufórico", "jubiloso" , "feliz", "divertido", "sonrisa", "risa"],
    "triste": ["deprimido", "melancólico", "desanimado", "desesperanzado", "afligido", "desolado", "apático", "abrumado", "triste", "llanto", "lágrima"],
    "enojado": ["furioso", "irritado", "indignado", "molesto", "rabioso", "enfurecido", "exasperademoo", "cólera", "enojo", "ira", "rabia", "rencor"],
    "emocionado": ["entusiasmado", "excitante", "apasionado", "fascinado", "asombrado", "impresionado", "conmovido", "entusiasmado", "emocionado"],
    "nostalgico":["melancólico", "nostálgico", "recuerdos", "añoranza", "remembranza", "memoria", "evocación", "nostalgia", "nostálgico", "recuerdos", "añoranza", "remembranza", "memoria", "evocación"],
    "ansioso": ["nervioso", "inquieto", "preocupado", "tenso", "agitado", "estresado", "intranquilo", "ansioso", "ansiedad", "angustiado", "desasosiego", "inquietud"],
}

respuestas_emocionales = {
    "feliz":["Me alegra mucho leerte feliz!", "Que bueno que fue un gran día para ti"],
    "triste": ["Lamento que te sientas asi. Estoy para ti", "A veces estar triste es parte de sanar"],
    "enojado":["Respira profundo, mereces estar en paz", "Esta bien enojarse, pero no dejes que te consuma"],
    "emocionado":["Que bueno que te sientas asi! Cuéntame más", "Me alegra que estés emocionado, ¿qué te emociona?", "Cuéntame más sobre lo que te emociona"],
    "nostalgico":["La nostalgia puede ser hermosa, ¿qué recuerdos tienes?", "A veces recordar es una forma de sanar"],
    "ansioso":["La ansiedad puede ser difícil, pero estoy aquí para ti", "Respira profundo, todo estará bien"],
    "neutra": ["Entiendo, a veces no hay una emoción específica", "Está bien sentirse asi, ¿quieres hablar de algo en particular?"],
}

historial = []

emociones_positivas = ["feliz", "emocionado"]
emociones_negativas = ["triste", "enojado", "ansioso", "nostalgico"]

def obtener_contexto_dia():
    hoy = datetime.now()
    dia = hoy.strftime("%A") #Ingles
    dias_es = {
        "Monday": "Lunes",
        "Tuesday": "Martes",
        "Wednesday": "Miércoles",
        "Thursday": "Jueves",
        "Friday": "Viernes",
        "Saturday": "Sábado",
        "Sunday": "Domingo"
    }
    dia_es = dias_es[dia]

    if dia_es == "Lunes":
        return "Espero que hayas tenido un buen fin de semana. ¿Cómo te sientes hoy?"
    elif dia_es == "Viernes":
        return "¡Es viernes! ¿Tienes planes para el fin de semana?"
    elif dia_es == "Domingo":
        return "Es domingo, un buen día para reflexionar. ¿Cómo te sientes hoy?"
    else: 
        return f"Hoy es {dia_es}. ¿Cómo te sientes hoy?"
    
def analizar_emocion(texto):
    texto = texto.lower().split()
    puntajes = {emocion: 0 for emocion in emociones}

    for palabra in texto:
        for emocion, lista in emociones.items():
            if palabra in lista:
                puntajes[emocion] += 1

    emocion_dectectada = max(puntajes, key=puntajes.get)

    if puntajes[emocion_dectectada] == 0:
        return "neutra"

    return emocion_dectectada

def generar_respuesta(emocion):
    return random.choice(respuestas_emocionales.get(emocion, respuestas_emocionales["neutra"]))

def mostrar_el_historial():
    print("Historial de emociones:")
    conteo = {emocion: 0 for emocion in emociones}
    conteo["neutra"] = 0

    for entrada in historial:
        conteo[entrada["emocion"]] += 1
    
    for emocion, cantidad in conteo.items():
        print(f"{emocion.capitalize()}: {cantidad} veces")

    total_positivas = sum(conteo[e] for e in emociones_positivas)
    total_negativas = sum(conteo[e] for e in emociones_negativas)

    print("\nResumen de mi puntaje emocional diario:")
    print(f"Emociones positivas :) : {total_positivas} veces")
    print(f"Emociones negativas :( : {total_negativas} veces")
    if total_positivas > total_negativas:
        print("Hoy fue un buen día :)")
    elif total_positivas < total_negativas:
        print("Has tenido un día difícil :(, pero estoy aquí para ti")
    else:
        print("Tus emociones están equilibradas :)")

def agregar_palabras_personalizadas():
    print("¿Quieres agregar palabras personalizadas a alguna emoción?")
    emocion = input("Escribe la emocion a la que quieres agregar palabras (o 'no')").lower()
    if emocion in emociones:
        nuevas = input(f"Escribe las nuevas palabras separadas por comas para '{emocion}': ").lower().split(",")
        emociones[emocion].extend([palabra.strip() for palabra in nuevas])
        print(f"Palabras agregadas a '{emocion}'")
    elif emocion != "no":
        print("Emoción no válida. Intenta de nuevo.")


# EJECUCIÓN DEL ASISTENTE
print("Bienvenido a tu asistente emocional")
print(obtener_contexto_dia())
while True:
    entrada = input("\n Escribe tu entrada de hoy (o 'salir' para cerrar el asistente): ")
    if entrada.lower() == "salir":
        mostrar_el_historial()
        print("Gracias por usar el asistente emocional. ¡Cuídate!")
        break
    emocion = analizar_emocion(entrada)
    respuesta = generar_respuesta(emocion)
    print(f"\n Asistente: {respuesta}")
    historial.append({"entrada": entrada, "emocion": emocion})

    with open("historial.txt", "a", encoding="utf-8") as f:
        hoy = datetime.now().strftime("%Y-%m-%d")
        f.write(f"[{hoy}] {entrada} ---> {emocion}\n")
    
    agregar_palabras_personalizadas()