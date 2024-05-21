
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        # Almacena el apellido de la familia
        self.last_name = last_name

        # Lista privada para almacenar información de los miembros (diccionarios)
        self._members = [
            {"id": self._generateId(),  # Genera ID aleatorio para cada miembro
             "first_name": "John",
             "last_name": self.last_name,
             "age": 33,
             "lucky_numbers": [7, 13, 22]},
            {"id": self._generateId(),
             "first_name": "Jane",
             "last_name": self.last_name,
             "age": 35,
             "lucky_numbers": [10, 14, 3]},
            {"id": self._generateId(),
             "first_name": "Jimmy",
             "last_name": self.last_name,
             "age": 5,
             "lucky_numbers": [1]}
        ]

    # Método de solo lectura para generar ID aleatorios para nuevos miembros
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # Comprueba si el diccionario del miembro tiene una clave "id"
        if 'id' not in member:
            # Si no existe ID, genera uno
            member['id'] = self._generateId()
        # Agrega el diccionario completo del miembro a la lista de miembros
        self._members.append(member)
        # Devuelve el diccionario completo del miembro (incluyendo ID generado)
        return member

    def delete_member(self, id):
        # Itera a través de la lista de miembros
        for member in self._members:
            # Comprueba si el ID de un miembro coincide con el ID proporcionado
            if member["id"] == id:
                # Elimina el diccionario del miembro coincidente de la lista
                self._members.remove(member)
                # Devuelve True para indicar eliminación exitosa
                return True
        # Si no se encuentra ninguna coincidencia, devuelve False para indicar eliminación fallida
        return False

    def get_member(self, id):
        # Itera a través de la lista de miembros
        for member in self._members:
            # Comprueba si el ID de un miembro coincide con el ID proporcionado
            if member["id"] == id:
                # Devuelve el diccionario completo del miembro que contiene información del miembro
                return member
        # Si no se encuentra ninguna coincidencia, devuelve None para indicar que no se encontró el miembro
        return None

    # Método para obtener todos los miembros de la familia (sin cambios)
    def get_all_members(self):
        return self._members
