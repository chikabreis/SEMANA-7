class Libro:
    def _init_(self, titulo, autor):
        """Constructor: Inicializa los atributos 'titulo' y 'autor'."""
        self.titulo = titulo
        self.autor = autor
        print(f"Libro '{self.titulo}' por {self.autor} ha sido creado.")

    def _del_(self):
        """Destructor: Imprime un mensaje cuando el objeto es destruido."""
        print(f"Libro '{self.titulo}' por {self.autor} ha sido destruido.")


# Crear una instancia de la clase Libro
mi_libro = Libro("Cien Años de Soledad", "Gabriel García Márquez")

# Ejemplo de uso del objeto, que luego se destruye cuando sale del alcance o se elimina explícitamente
del mi_libro  # Esto invoca el destructor

# Explicación del código:
#
# 1. Constructor (_init_):
#    - El método _init_ es el constructor de la clase. Se llama automáticamente
#      cuando se crea una nueva instancia de la clase Libro.
#    - Inicializa los atributos 'titulo' y 'autor' con los valores proporcionados
#      como argumentos.
#    - Imprime un mensaje indicando que el libro ha sido creado.
#
# 2. Destructor (_del_):
#    - El método _del_ es el destructor de la clase. Se llama automáticamente
#      cuando el objeto es destruido o eliminado.
#    - Imprime un mensaje indicando que el libro ha sido destruido.
#    - El destructor se activa en dos situaciones principales:
#      a) Cuando el objeto sale del alcance y ya no es accesible.
#      b) Cuando el objeto se elimina explícitamente usando 'del'.
#
# 3. Creación y eliminación del objeto:
#    - Se crea una instancia de la clase Libro llamada 'mi_libro', pasando los
#      argumentos "Cien Años de Soledad" y "Gabriel García Márquez" al constructor.
#    - El constructor (_init_) se activa, inicializando los atributos y
#      imprimiendo el mensaje de creación.
#    - El objeto 'mi_libro' se elimina explícitamente usando 'del mi_libro'.
#    - El destructor (_del_) se activa, imprimiendo el mensaje de destrucción.