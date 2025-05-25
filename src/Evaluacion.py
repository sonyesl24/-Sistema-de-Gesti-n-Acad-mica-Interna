"""
Miembros del grupo:
- BRIONES PISCO FERNANDO STEVEN
- PADILLA CRESPIN THAIS MARIANA
- SALVATIERRA LAINEZ SONY ESAU
- TORRES GOMEZ AARON MAURICIO
"""


# Definición de la clase Evaluacion
class Evaluacion:
    """
    Clase base Evaluacion que representa una evaluación general.
    Contiene un metodo polimórfico calcularNota(), que será sobrescrito en las subclases
    como Examen, GestionFormativaPractica.
    """

    # Constructor que recibe la nota
    def __init__(self, nota):
        # Inicializamos el atributo protegido _nota en None
        self._nota = None

        # Asignamos el valor recibido usando el setter (con validación)
        self.nota = nota

    # Getter para obtener el valor de la nota
    @property
    def nota(self):
        return self._nota

    # Setter para asignar la nota con validación
    @nota.setter
    def nota(self, valor):
        # Verificamos que la nota sea un número (int o float) entre 1 y 10
        if isinstance(valor, (int, float)) and 1 <= valor <= 10:
            self._nota = valor
        else:
            raise ValueError("La nota debe estar entre 1 y 10.")

    # Metodo polimórfico que puede ser sobrescrito por las subclases
    def calcularNota(self):
        # En la clase base solo devuelve la nota tal como fue ingresada
        return self._nota

    # Metodo especial para imprimir la evaluación de forma legible
    def __str__(self):
        return f"Evaluación: nota = {self._nota}"


# Bloque de prueba para ejecutar este archivo directamente
if __name__ == "__main__":
    # Creamos una instancia básica de Evaluacion
    ev = Evaluacion(8)

    # Imprimimos los datos usando el metodo __str__
    print(ev)

    # Mostramos el resultado del metodo calcularNota (en este caso, la misma nota)
    print("Nota calculada:", ev.calcularNota())





