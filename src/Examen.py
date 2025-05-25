"""
Miembros del grupo:
- BRIONES PISCO FERNANDO STEVEN
- PADILLA CRESPIN THAIS MARIANA
- SALVATIERRA LAINEZ SONY ESAU
- TORRES GOMEZ AARON MAURICIO
"""
# Importamos la clase base Evaluacion, que contiene lógica común para todas las evaluaciones
from src.Evaluacion import Evaluacion


class Examen(Evaluacion):
    """
    Clase que representa la evaluación de acreditación (examen final).
    Esta evaluación representa el 34% de la nota total del estudiante.
    Hereda de la clase Evaluacion.
    """

    def __init__(self, nota):
        """
        Constructor del examen.
        Inicializa el atributo protegido _nota (heredado) en 0 y luego le asigna el valor con validación.
        """
        self._nota = 0  # Se define directamente para asegurar la existencia del atributo
        self.nota = nota  # Se usa el setter para validar y asignar el valor recibido

    # Getter para obtener la nota del examen
    @property
    def nota(self):
        """
        Devuelve la nota bruta del examen (sin ponderación).
        """
        return self._nota

    # Setter que valida la nota esté entre 1 y 10
    @nota.setter
    def nota(self, valor):
        """
        Valida y asigna la nota del examen.
        La nota debe ser un número entero o flotante entre 1 y 10.
        """
        if isinstance(valor, (int, float)) and 1 <= valor <= 10:
            self._nota = valor
        else:
            raise ValueError("La nota del examen debe estar entre 1 y 10.")

    # Metodo sobrescrito de la clase Evaluacion (polimorfismo)
    def calcularNota(self):
        """
        Calcula y retorna la nota ponderada del examen.
        Como el examen representa el 34% de la nota total, se multiplica por 0.34.
        """
        return self._nota * 0.34

    def __str__(self):
        """
        Devuelve una representación legible del objeto Examen.
        Muestra tanto la nota bruta como la nota ponderada.
        """
        return (f"Evaluación Examen:\n"
                f" - Nota bruta: {self._nota}\n"
                f" - Ponderada (34%): {self.calcularNota():.2f}")


# Bloque de prueba: solo se ejecuta si el archivo se corre directamente
if __name__ == "__main__":
    # Se crea una instancia de Examen con una nota válida
    examen = Examen(7.8)

    # Se imprime el resultado de la evaluación
    print(examen)

