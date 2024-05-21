"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

# Crea una aplicación Flask (servidor web)
app = Flask(__name__)

# Deshabilita la restricción estricta de barras diagonales en las rutas
app.url_map.strict_slashes = False

# Habilita CORS para permitir solicitudes de orígenes cruzados (ejemplos de front-end que se ejecutan en un dominio diferente)
CORS(app)

# Crea un objeto de la clase FamilyStructure para la familia Jackson
jackson_family = FamilyStructure("Jackson")

# Maneja y serializa errores como un objeto JSON
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    # Convierte el error a un diccionario y lo devuelve en formato JSON junto con el código de estado HTTP
    return jsonify(error.to_dict()), error.status_code

# Genera un mapa del sitio con todos los puntos finales de la API
@app.route('/')
def sitemap():
    # Utiliza la función `generate_sitemap` para generar un mapa del sitio con las rutas de la API
    return generate_sitemap(app)

# Obtiene todos los miembros de la familia (GET /members)
@app.route('/members', methods=['GET'])
def get_all_members():
    # Obtiene todos los miembros de la familia Jackson utilizando el método `get_all_members` de la clase `FamilyStructure`
    members = jackson_family.get_all_members()
    # Devuelve la lista de miembros en formato JSON con código de estado HTTP 200 (OK)
    return jsonify(members), 200

# Agrega un nuevo miembro a la familia (POST /member)
@app.route('/member', methods=['POST'])
def add_member():
    # Obtiene el cuerpo de la solicitud (datos del nuevo miembro) en formato JSON
    request_body = request.json

    # Valida si el cuerpo de la solicitud está vacío
    if not request_body:
        # Devuelve un error con código de estado HTTP 400 (Solicitud incorrecta)
        return jsonify({"error": "Invalid input"}), 400

    # Agrega el nuevo miembro a la familia utilizando el método `add_member` de la clase `FamilyStructure`
    new_member = jackson_family.add_member(request_body)

    # Devuelve el miembro recién agregado en formato JSON con código de estado HTTP 200 (OK)
    return jsonify(new_member), 200

# Obtiene un miembro específico por su ID (GET /member/<int:member_id>)
@app.route('/member/<int:member_id>', methods=['GET'])
def get_single_member(member_id):
    # Busca un miembro con el ID proporcionado utilizando el método `get_member` de la clase `FamilyStructure`
    member = jackson_family.get_member(member_id)

    # Si se encuentra el miembro:
    if member:
        # Devuelve el miembro en formato JSON con código de estado HTTP 200 (OK)
        return jsonify(member), 200
    # Si no se encuentra el miembro:
    else:
        # Devuelve un error con código de estado HTTP 404 (No encontrado)
        return jsonify({"error": "Member not found"}), 404

# Elimina un miembro por su ID (DELETE /member/<int:member_id>)
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    # Elimina un miembro con el ID proporcionado utilizando el método `delete_member` de la clase `FamilyStructure`
    result = jackson_family.delete_member(member_id)

    # Si se elimina el miembro:
    if result:
        # Devuelve una confirmación en formato JSON con código de estado HTTP 200 (OK)
        return jsonify({"done": True}), 200
    # Si no se encuentra el miembro:
    else:
        # Devuelve un error con código de estado HTTP 404 (No encontrado)
        return jsonify({"error": "Member not found"}), 404


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
