# Importamos las clases necesarias desde sus respectivos módulos
from src.Estudiante import Estudiante
from src.Docente import Docente
from src.Asignatura import Asignatura
from src.GestionContinua import GestionContinua
from src.Examen import Examen
from src.Nota import Nota

"""
Miembros del grupo:
- BRIONES PISCO FERNANDO STEVEN
- PADILLA CRESPIN THAIS MARIANA
- SALVATIERRA LAINEZ SONY ESAU
- TORRES GOMEZ AARON MAURICIO
"""

# Este bloque se ejecuta solo si este archivo es el principal (no si es importado)
if __name__ == "__main__":
    print(" SISTEMA DE GESTIÓN ACADÉMICA INTERNA\n")

    try:
        # Crear y mostrar un objeto Estudiante con sus datos personales
        estudiante = Estudiante(nombre="Ana Torres", cedula="1102345678", matricula="2025A001")
        print(" Estudiante registrado:")
        print(estudiante)  # Se invoca el metodo __str__ de la clase Estudiante y Usuario
        print("-" * 50)

        # Crear y mostrar un objeto Docente con sus datos personales y especialidad
        docente = Docente(nombre="Luis Pérez", cedula="0912345678", especialidad="Magíster en Software")
        print(" Docente registrado:")
        print(docente)  # Se invoca el metodo __str__ de la clase Docente
        print("-" * 50)

        # Crear y mostrar un objeto Asignatura con su nombre y código
        asignatura = Asignatura(nombre="Programación Orientada a Objetos", codigo="INF-235")
        print(" Asignatura registrada:")
        print(asignatura)  # Se invoca el metodo __str__ de la clase Asignatura
        print("-" * 50)

        # Crear objeto de evaluación continua con dos notas (formativa y práctica)
        gestion = GestionContinua(nota_formativa=5.5, nota_practica=5.5)  # Se pondera al 66%

        # Crear objeto de evaluación tipo Examen con una sola nota
        examen = Examen(nota=10)  # Se pondera al 34%

        # Mostrar los datos de ambas evaluaciones
        print(" Evaluaciones registradas:")
        print(gestion)  # Se invoca el metodo __str__ de GestionContinua
        print(examen)   # Se invoca el metodo __str__ de Examen
        print("-" * 50)

        # Calcular la nota final combinando ambas evaluaciones
        nota_final = Nota(gestion, examen)

        # Mostrar el resultado final del estudiante
        print(" Resultado final:")
        print(nota_final)  # Se invoca el metodo __str__ de la clase Nota
        print("=" * 50)

    # Captura y muestra errores de validación de datos (por ejemplo, notas fuera de rango)
    except ValueError as ve:
        print(f" Error de validación: {ve}")

    # Captura y muestra errores inesperados durante la ejecución
    except Exception as e:
        print(f" Error inesperado: {e}")

