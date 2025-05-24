"""
Miembros del grupo:
- BRIONES PISCO FERNANDO STEVEN
- PADILLA CRESPIN THAIS MARIANA
- SALVATIERRA LAINEZ SONY ESAU
- TORRES GOMEZ AARON MAURICIO
"""
from src.Usuario import Usuario  # Importamos la clase Usuario desde el módulo correspondiente

# Definimos la clase Estudiante como subclase de Usuario
class Estudiante(Usuario):

    # Constructor: recibe nombre, cédula y matrícula
    def __init__(self, nombre: str, cedula: str, matricula: str):
        # Se definen los atributos protegidos heredados y el nuevo atributo matricula
        self._nombre = None       # Atributo protegido para el nombre (heredado de Usuario)
        self._cedula = None       # Atributo protegido para la cédula (heredado de Usuario)
        self._matricula = None    # Atributo protegido exclusivo de Estudiante

        # Se asignan los valores a través de los setters (incluyen validación)
        self.nombre = nombre      # Setter de nombre, ya definido en Usuario, valida que no esté vacío
        self.cedula = cedula      # Setter de cédula, valida que tenga exactamente 10 dígitos
        self.matricula = matricula  # Setter propio de matrícula, también con validación

    # Getter de matrícula: permite acceder de forma controlada al valor de la matrícula
    @property
    def matricula(self):
        return self._matricula

    # Setter de matrícula: valida que no esté vacío
    @matricula.setter
    def matricula(self, valor):
        # Validación: debe ser una cadena no vacía
        if isinstance(valor, str) and valor.strip():
            self._matricula = valor.strip()  # Se guarda el valor sin espacios al inicio/fin
        else:
            raise ValueError("La matrícula no puede estar vacía.")  # Lanza error si no cumple

    # Metodo especial para mostrar una representación legible del objeto Estudiante
    def __str__(self):
        return f"Nombre: {self._nombre} | Cédula: {self._cedula} | Matrícula: {self._matricula}"
        # Usamos directamente los atributos protegidos para mostrar sus valores

# Bloque de prueba: se ejecuta solo si el archivo es ejecutado directamente
if __name__ == "__main__":
    try:
        # Creamos una instancia válida de Estudiante
        estudiante1 = Estudiante("Carlos Vela", "1122334455", "MAT-2025-001")
        print(estudiante1)  # Se imprime el resultado del metodo __str__

    except ValueError as e:
        # Si se produce una excepción de validación, se muestra el mensaje de error
        print("Error:", e)


