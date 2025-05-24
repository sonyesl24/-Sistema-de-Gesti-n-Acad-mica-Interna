"""
Miembros del grupo:
- BRIONES PISCO FERNANDO STEVEN
- PADILLA CRESPIN THAIS MARIANA
- SALVATIERRA LAINEZ SONY ESAU
- TORRES GOMEZ AARON MAURICIO
"""
# Definición de la clase Asignatura
class Asignatura:
    # Constructor para inicializar una instancia de Asignatura con nombre y código
    def __init__(self, nombre: str, codigo: str):
        # Inicializamos los atributos protegidos en None (buenas prácticas para encapsulamiento)
        self._nombre = None        # Atributo protegido para el nombre de la asignatura
        self._codigo = None        # Atributo protegido para el código de la asignatura

        # Asignamos valores usando los setters, que incluyen validaciones
        self.nombre = nombre       # Se usa el setter de nombre, verifica que no esté vacío
        self.codigo = codigo       # Se usa el setter de código, también con validación

    # Getter para el atributo nombre
    @property
    def nombre(self):
        return self._nombre  # Devuelve el valor del nombre almacenado internamente

    # Setter para el atributo nombre
    @nombre.setter
    def nombre(self, valor):
        # Validación: el nombre debe ser una cadena no vacía
        if isinstance(valor, str) and valor.strip():
            self._nombre = valor.strip()  # Se guarda el nombre sin espacios innecesarios
        else:
            raise ValueError("El nombre de la asignatura no puede estar vacío.")  # Error si es inválido

    # Getter para el atributo código
    @property
    def codigo(self):
        return self._codigo  # Devuelve el código de la asignatura

    # Setter para el atributo código
    @codigo.setter
    def codigo(self, valor):
        # Validación: el código debe ser una cadena no vacía
        if isinstance(valor, str) and valor.strip():
            self._codigo = valor.strip()  # Se guarda el código limpio de espacios
        else:
            raise ValueError("El código de la asignatura no puede estar vacío.")  # Lanza error si no cumple

    # Metodo especial __str__: define cómo se imprime un objeto Asignatura
    def __str__(self):
        return f"Código: {self._codigo} | Nombre: {self._nombre}"
        # Se muestra el código y el nombre de la asignatura en formato legible

# Bloque para pruebas unitarias simples: se ejecuta solo si el archivo se corre directamente
if __name__ == "__main__":
    try:
        # Se crea una instancia válida de Asignatura
        asignatura1 = Asignatura("Matemáticas", "MAT101")

        # Se imprime la representación legible del objeto usando __str__
        print(asignatura1)

    except ValueError as e:
        # Si ocurre un error de validación, se muestra el mensaje
        print("Error:", e)

