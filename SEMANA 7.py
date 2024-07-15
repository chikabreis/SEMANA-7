class FileHandler:
    def _init_(self, filename):
        """
        Constructor de la clase FileHandler.
        Este método se llama automáticamente cuando se crea una instancia de la clase.

        :param filename: Nombre del archivo que se va a manejar.
        """
        self.filename = filename
        self.file = None
        self.open_file()

    def open_file(self):
        """Método para abrir el archivo en modo lectura."""
        try:
            self.file = open(self.filename, 'r')
            print(f"Archivo '{self.filename}' abierto correctamente.")
        except FileNotFoundError:
            print(f"Error: El archivo '{self.filename}' no se encontró.")
            self.file = None

    def read_file(self):
        """Método para leer el contenido del archivo."""
        if self.file:
            content = self.file.read()
            print("Contenido del archivo:")
            print(content)
        else:
            print("No se puede leer el archivo porque no está abierto.")

    def _del_(self):
        """
        Destructor de la clase FileHandler.
        Este método se llama automáticamente cuando se elimina una instancia de la clase.
        Se utiliza para liberar recursos, como cerrar archivos abiertos.
        """
        if self.file:
            self.file.close()
            print(f"Archivo '{self.filename}' cerrado correctamente.")


# Uso de la clase FileHandler
if _name_ == "_main_":
    # Crear una instancia de FileHandler
    handler = FileHandler("ejemplo.txt")

    # Leer el contenido del archivo
    handler.read_file()

    # La instancia handler será destruida automáticamente al final del programa,
    # y el destructor (_del_) se llamará para cerrar el archivo.