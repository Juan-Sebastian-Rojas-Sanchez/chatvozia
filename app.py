from flask import Flask, request, jsonify
from procesador import buscar_respuesta

app = Flask(__name__)

@app.route('/')
def home():
    return 'Servidor Flask activo'

@app.route('/salud')
def salud():
    return 'OK'

@app.route('/preguntar', methods=['POST'])
def preguntar():
    data = request.get_json()
    pregunta = data.get('pregunta', '')
    respuesta = buscar_respuesta(pregunta)
    return jsonify({"respuesta": respuesta})

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))  # Render asigna dinámicamente un puerto
    app.run(host='0.0.0.0', port=port)
