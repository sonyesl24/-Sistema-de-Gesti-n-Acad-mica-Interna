# src/usuario.py

"""
Clase Usuario
---------------
Superclase base para representar un usuario del sistema académico.
Incluye nombre y cédula con encapsulamiento y validación.
Miembros del grupo:
- Nombre Apellido
- Nombre Apellido
- Nombre Apellido
- Nombre Apellido
"""

class Usuario:
    # Constructor de la clase Usuario, recibe nombre y cédula
    def __init__(self, nombre: str, cedula: str):
        self._nombre = None       # Atributo protegido para nombre
        self._cedula = None       # Atributo protegido para cédula
        self.nombre = nombre      # Se asigna usando el setter de nombre
        self.cedula = cedula      # Se asigna usando el setter de cédula

    # Getter del atributo nombre
    @property
    def nombre(self):
        return self._nombre

    # Setter del atributo nombre, con validación
    @nombre.setter
    def nombre(self, valor):
        # Verifica que el nombre no esté vacío
        if isinstance(valor, str) and valor.strip():
            self._nombre = valor.strip()  # Asigna el valor sin espacios extra
        else:
            raise ValueError("El nombre no puede estar vacío.")

    # Getter del atributo cédula
    @property
    def cedula(self):
        return self._cedula

    # Setter del atributo cédula, con validación
    @cedula.setter
    def cedula(self, valor):
        # Verifica que la cédula tenga exactamente 10 dígitos numéricos
        if isinstance(valor, str) and valor.isdigit() and len(valor) == 10:
            self._cedula = valor
        else:
            raise ValueError("La cédula debe tener exactamente 10 dígitos numéricos.")

    def __str__(self):
        return f"Nombre: {self.nombre} | Cédula: {self.cedula}"


# Bloque de prueba: se ejecuta solo si el archivo se corre directamente
if __name__ == "__main__":
    try:
        # Se crea una instancia de Usuario con datos válidos
        usuario1 = Usuario("Andrea Castillo", "1234567890")
        print(usuario1)  # Imprime los datos del usuario

        # Se actualiza el nombre y la cédula del usuario
        usuario1.nombre = "Luis Pérez"
        usuario1.cedula = "0987654321"
        print(usuario1)  # Muestra los nuevos datos

        # Estas líneas se pueden usar para probar errores:
        # usuario2 = Usuario("", "1234")
        # print(usuario2)

    except ValueError as e:
        print("Error:", e)  # Muestra el error si se ingresan datos inválidos
