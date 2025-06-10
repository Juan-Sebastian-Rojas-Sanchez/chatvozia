from fuzzywuzzy import fuzz
from faq_data import faq_aliases

def buscar_respuesta(pregunta_usuario, umbral=60):
    pregunta_usuario = pregunta_usuario.lower()

    # BÚSQUEDA POR COINCIDENCIA EXACTA (palabras clave)
    for clave, data in faq_aliases.items():
        for keyword in data["preguntas"]:
            if keyword.lower() in pregunta_usuario:
                return data["respuesta"]

    # BÚSQUEDA DIFUSA (fuzzy)
    mejor_coincidencia = {"clave": None, "score": 0}
    for clave, data in faq_aliases.items():
        for pregunta in data["preguntas"]:
            score = fuzz.ratio(pregunta_usuario, pregunta.lower())
            if score > mejor_coincidencia["score"]:
                mejor_coincidencia = {"clave": clave, "score": score}

    if mejor_coincidencia["score"] >= umbral:
        return faq_aliases[mejor_coincidencia["clave"]]["respuesta"]
    else:
        return "No encontré información clara sobre eso."
