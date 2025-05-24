

"""
Miembros del grupo:
- BRIONES PISCO FERNANDO STEVEN
- PADILLA CRESPIN THAIS MARIANA
- SALVATIERRA LAINEZ SONY ESAU
- TORRES GOMEZ AARON MAURICIO
"""
class Usuario:
    # Constructor de la clase Usuario. Se ejecuta al crear una nueva instancia.
    # Recibe los parámetros nombre y cédula.
    def __init__(self, nombre: str, cedula: str):
        self._nombre = None       # Se declara un atributo protegido _nombre (convención: "_" indica que no debe accederse directamente)
        self._cedula = None       # Se declara un atributo protegido _cedula
        self.nombre = nombre      # Se asigna el valor al atributo nombre usando el setter (valida el valor antes de guardar)
        self.cedula = cedula      # Se asigna el valor a la cédula usando el setter (valida que tenga 10 dígitos)

    # Getter del atributo nombre. Permite acceder al valor del nombre de forma controlada.
    @property
    def nombre(self):
        return self._nombre       # Devuelve el valor de _nombre (encapsulado)

    # Setter del atributo nombre. Permite establecer el valor del nombre validando que no esté vacío.
    @nombre.setter
    def nombre(self, valor):
        # Verifica que el valor sea una cadena y que no esté vacía (ni solo espacios)
        if isinstance(valor, str) and valor.strip():
            self._nombre = valor.strip()  # Asigna el valor al atributo _nombre quitando espacios iniciales/finales
        else:
            # Si la validación falla, se lanza una excepción
            raise ValueError("El nombre no puede estar vacío.")

    # Getter del atributo cedula. Permite acceder a la cédula de forma segura.
    @property
    def cedula(self):
        return self._cedula       # Devuelve el valor de _cedula (encapsulado)

    # Setter del atributo cedula. Valida que el valor tenga 10 dígitos numéricos.
    @cedula.setter
    def cedula(self, valor):
        # Verifica que sea una cadena de exactamente 10 caracteres y que sean todos dígitos
        if isinstance(valor, str) and valor.isdigit() and len(valor) == 10:
            self._cedula = valor  # Asigna el valor a _cedula si es válido
        else:
            # Si no cumple con los requisitos, se lanza un error
            raise ValueError("La cédula debe tener exactamente 10 dígitos numéricos.")

    # Metodo especial que define cómo se imprime un objeto de tipo Usuario
    def __str__(self):
        return f"Nombre: {self.nombre} | Cédula: {self.cedula}"  # Devuelve una representación legible del usuario


# Bloque de prueba: este código solo se ejecuta si este archivo se ejecuta directamente (no si se importa en otro script)
if __name__ == "__main__":
    try:
        # Se intenta crear un objeto Usuario con valores válidos
        usuario1 = Usuario("Andrea Castillo", "1234567890")
        print(usuario1)  # Se imprime la representación en texto del usuario

    except ValueError as e:
        # Si ocurre un error de validación en nombre o cédula, se muestra el mensaje de error
        print("Error:", e)

