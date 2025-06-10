from flask import Flask, request, jsonify
from flask_cors import CORS
from procesador import buscar_respuesta  # O usa directamente si no tienes este archivo

app = Flask(__name__)
CORS(app)  # 🔥 Esto habilita CORS para todas las rutas

@app.route("/preguntar", methods=["POST"])
def preguntar():
    datos = request.get_json()
    pregunta = datos.get("pregunta", "")
    respuesta = buscar_respuesta(pregunta)
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    print("Servidor Flask corriendo...")
    app.run(debug=True)
