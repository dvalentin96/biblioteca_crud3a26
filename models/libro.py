class libro:

    # Constructor de la clase libro
    def __init__(self, id_libro, titulo, autor, isbn):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True  # por defecto, el libro está disponible

    def prestar(self):
            if self.disponible:
                self.disponible = False
                return True
            else:
                return False
    def devolver(self):
            self.disponible = True

    def mostrar_info(self):
        return f"Libro ID: {self.id_libro}, Titulo: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Disponible: {self.disponible}"
    