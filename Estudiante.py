from Usuario import Usuario # Importamos la clase base Usuario

class Estudiante(Usuario):
    # Constructor que inicializa nombre, cédula y matrícula
    def __init__(self, nombre: str, cedula: str, matricula: str):
        # Inicializamos los atributos protegidos heredados y propios
        self._nombre = None
        self._cedula = None
        self._matricula = None

        # Asignamos usando los setters para aplicar validaciones
        self.nombre = nombre
        self.cedula = cedula
        self.matricula = matricula

    # Getter para matrícula
    @property
    def matricula(self):
        return self._matricula

    # Setter para matrícula con validación simple
    @matricula.setter
    def matricula(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._matricula = valor.strip()
        else:
            raise ValueError("La matrícula no puede estar vacía.")


    def __str__(self):
        # Accedemos directamente a los atributos protegidos heredados para mostrar
        return f"Nombre: {self._nombre} | Cédula: {self._cedula} | Matrícula: {self._matricula}"


# Bloque para probar la clase cuando se ejecute este archivo
if __name__ == "__main__":
    try:
        # Crear instancia válida
        estudiante1 = Estudiante("Carlos Vela", "1122334455", "MAT-2025-001")
        print(estudiante1)  # Mostrar datos

        # Actualizar atributos
        estudiante1.nombre = "Valeria Ruiz"
        estudiante1.cedula = "1234567890"
        estudiante1.matricula = "MAT-2025-002"
        print(estudiante1)  # Mostrar datos actualizados

        # Para probar error de validación, descomenta la siguiente línea
        # estudiante2 = Estudiante("", "123", "")

    except ValueError as e:
        print("Error:", e)

