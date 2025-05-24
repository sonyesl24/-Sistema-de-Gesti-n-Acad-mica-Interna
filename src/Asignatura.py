class Asignatura:
    def __init__(self, nombre: str, codigo:str):
        self._nombre = None
        self._codigo = None
        self.nombre= nombre
        self.codigo= codigo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre (self, valor):
        if isinstance(valor, str) and valor.strip():
            self._nombre = valor.strip()
        else:
            raise ValueError("El nombre de la asignatura no peude estar vacia")

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo (self, valor):
        if isinstance(valor, str) and valor.strip():
            self._codigo=valor.strip()
        else:
            raise ValueError("El codigo de la asignatura no puede estar vacio")

    def __str__(self):
        return f"Codigo: {self._codigo}  //  Nombre: {self._nombre}"

if __name__ == "__main__":
    try:
        asignatura1 = Asignatura("Mate", "mat101")
        print(asignatura1)

    except ValueError as e:
        print("Error", e)
