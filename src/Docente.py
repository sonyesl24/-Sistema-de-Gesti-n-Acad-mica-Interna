"""
Miembros del grupo:
- BRIONES PISCO FERNANDO STEVEN
- PADILLA CRESPIN THAIS MARIANA
- SALVATIERRA LAINEZ SONY ESAU
- TORRES GOMEZ AARON MAURICIO
"""
from src.Usuario import Usuario  # Importamos la clase base Usuario

class Docente(Usuario):
    # Constructor para inicializar nombre, cédula y especialidad del docente
    def __init__(self, nombre: str, cedula: str, especialidad: str):
        # Llamamos explícitamente al constructor de Usuario para inicializar nombre y cédula
        Usuario.__init__(self, nombre, cedula)
        # Inicializamos el atributo protegido propio de Docente (especialidad) en None
        self._especialidad = None
        # Asignamos especialidad usando el setter, que incluye validación
        self.especialidad = especialidad

    # Getter para especialidad que devuelve el valor almacenado en _especialidad
    @property
    def especialidad(self):
        return self._especialidad

    # Setter para especialidad que valida que no sea una cadena vacía ni inválida
    @especialidad.setter
    def especialidad(self, valor):
        # Validamos que el valor sea cadena no vacía
        if isinstance(valor, str) and valor.strip():
            # Si pasa la validación, asignamos el valor limpiado (sin espacios extras)
            self._especialidad = valor.strip()
        else:
            # Si no pasa la validación, lanzamos un error para que se corrija
            raise ValueError("La especialidad no puede estar vacía.")

    # Metodo especial para imprimir información legible del objeto
    def __str__(self):
        # Retornamos una cadena con nombre, cédula y especialidad del docente
        return f"Nombre: {self._nombre} | Cédula: {self._cedula} | Especialidad: {self._especialidad}"

# Bloque para hacer pruebas al ejecutar este archivo directamente
if __name__ == "__main__":
    try:
        # Creamos un objeto Docente válido con nombre, cédula y especialidad
        docente1 = Docente("Ana Gómez", "9988776655", "Matemáticas")
        print(docente1)  # Imprimimos el estado del objeto

    except ValueError as e:
        # Capturamos e imprimimos cualquier error de validación que ocurra
        print("Error:", e)


