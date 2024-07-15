class ArchivoTemporario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.archivo = None
        print(f"Constructor: Creando archivo temporario '{self.nombre}'")
        try:
            self.archivo = open(self.nombre, 'w')
        except IOError as e:
            print(f"Error al crear el archivo: {e}")

    def escribir(self, texto):
        if self.archivo:
            self.archivo.write(texto)
            print(f"Escribiendo en '{self.nombre}': {texto}")

    def __del__(self):
        if self.archivo:
            self.archivo.close()
            print(f"Destructor: Cerrando y eliminando archivo temporario '{self.nombre}'")
            import os
            try:
                os.remove(self.nombre)
            except OSError as e:
                print(f"Error al eliminar el archivo: {e}")