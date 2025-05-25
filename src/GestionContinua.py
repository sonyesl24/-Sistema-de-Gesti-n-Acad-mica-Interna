"""
Miembros del grupo:
- BRIONES PISCO FERNANDO STEVEN
- PADILLA CRESPIN THAIS MARIANA
- SALVATIERRA LAINEZ SONY ESAU
- TORRES GOMEZ AARON MAURICIO
"""
from src.Evaluacion import Evaluacion


# La clase GestionContinua hereda de Evaluacion
class GestionContinua(Evaluacion):
    """
    Clase que representa la gestión continua del estudiante.
    Combina dos notas: formativa y práctica, cada una con peso del 50%(esa nota representa la mitad del valor dentro de un cálculo promedio o ponderado).
    El resultado se multiplica por 0.66 porque esta evaluación representa el 66%
    del total de la nota final del estudiante.
    """

    def __init__(self, nota_formativa, nota_practica):
        # En vez de usar __init__(), inicializamos _nota directamente
        self._nota = 0  # Será calculado con el metodo calcularNota()

        # Guardamos las notas formativa y práctica usando los setters con validación
        self.nota_formativa = nota_formativa
        self.nota_practica = nota_practica

    # Getter para la nota formativa
    @property
    def nota_formativa(self):
        return self._nota_formativa

    # Setter para la nota formativa con validación
    @nota_formativa.setter
    def nota_formativa(self, valor):
        # Validamos que esté en el rango de 1 a 10
        if isinstance(valor, (int, float)) and 1 <= valor <= 10:
            self._nota_formativa = valor
        else:
            raise ValueError("La nota formativa debe estar entre 1 y 10.")

    # Getter para la nota práctica
    @property
    def nota_practica(self):
        return self._nota_practica

    # Setter para la nota práctica con validación
    @nota_practica.setter
    def nota_practica(self, valor):
        # Validamos que esté en el rango de 1 a 10
        if isinstance(valor, (int, float)) and 1 <= valor <= 10:
            self._nota_practica = valor
        else:
            raise ValueError("La nota práctica debe estar entre 1 y 10.")

    # Sobrescribimos el metodo polimórfico calcularNota()
    def calcularNota(self):
        # Se promedian ambas notas y luego se aplica el 66% de ponderación
        promedio = (self.nota_formativa * 0.5 + self.nota_practica * 0.5)
        return promedio * 0.66  # Peso total de esta evaluación

    # Metodo para mostrar todos los datos de forma clara y legible
    def __str__(self):
        return (f"Gestión Continua:\n"
                f" - Nota Formativa: {self.nota_formativa}\n"
                f" - Nota Práctica: {self.nota_practica}\n"
                f" - Ponderada (66%): {self.calcularNota():.2f}")


# Prueba de la clase si se ejecuta este archivo directamente
if __name__ == "__main__":
    # Creamos una instancia con notas válidas
    gestion = GestionContinua(8.5, 9)

    # Imprimimos el resultado utilizando el metodo __str__
    print(gestion)

