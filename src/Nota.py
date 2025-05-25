

"""
Miembros del grupo:
- BRIONES PISCO FERNANDO STEVEN
- PADILLA CRESPIN THAIS MARIANA
- SALVATIERRA LAINEZ SONY ESAU
- TORRES GOMEZ AARON MAURICIO
"""
class Nota:
    """
    Clase que representa el resultado final del estudiante.
    Recibe dos evaluaciones como entrada:
    - Una evaluación de tipo GestionContinua (pondera el 66%)
    - Una evaluación de tipo Examen (pondera el 34%)

    La suma de ambas evaluaciones da como resultado la nota final del estudiante.
    """

    def __init__(self, evaluacion_continua, evaluacion_examen):
        """
        Constructor de la clase Nota.
        Se inicializa con dos objetos que representan las evaluaciones:
        - evaluacion_continua: instancia de la clase GestionContinua
        - evaluacion_examen: instancia de la clase Examen

        Ambos objetos deben implementar el metodo calcularNota() para permitir polimorfismo.
        """
        self.evaluacion_continua = evaluacion_continua  # Asignamos la evaluación continua
        self.evaluacion_examen = evaluacion_examen      # Asignamos la evaluación del examen final

    def calcularNotaFinal(self):
        """
        Calcula la nota final del estudiante combinando las dos evaluaciones.

        Usa polimorfismo al invocar calcularNota() de cada objeto,
        permitiendo que cada clase aplique su propia lógica interna.

        Devuelve:
        - Nota final redondeada a 2 decimales (float)
        """
        # Obtenemos la nota ponderada de la gestión continua (66%)
        nota_continua = self.evaluacion_continua.calcularNota()

        # Obtenemos la nota ponderada del examen final (34%)
        nota_examen = self.evaluacion_examen.calcularNota()

        # Sumamos ambas ponderaciones para obtener la nota total del estudiante
        nota_total = nota_continua + nota_examen

        # Retornamos la nota final redondeada a 2 decimales
        return round(nota_total, 2)

    def __str__(self):
        """
        Representación en forma de cadena del objeto.
        Devuelve un mensaje con la nota final del estudiante.
        """
        return f"Nota Final del Estudiante: {self.calcularNotaFinal()}/10"


# Bloque de prueba: se ejecuta solo si este archivo se corre directamente
if __name__ == "__main__":
    # Importamos las clases necesarias desde su ubicación en el proyecto
    from src.GestionContinua import GestionContinua
    from src.Examen import Examen

    # Creamos una instancia de Gestión Continua con dos notas (formativa y práctica)
    continua = GestionContinua(8.5, 9)  # Estas se promedian y luego se ponderan al 66%

    # Creamos una instancia de Examen con una nota final
    examen = Examen(7.8)  # Esta se pondera directamente al 34%

    # Creamos el objeto Nota que combina ambas evaluaciones
    nota_final = Nota(continua, examen)

    # Imprimimos el resultado final del estudiante
    print(nota_final)

