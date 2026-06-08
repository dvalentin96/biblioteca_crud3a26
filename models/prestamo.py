from models.libro import libro

class prestamo:
    
    # Constructor de la clase prestamo
    def __init__(self, id_prestamo, usuario, libro, fecha_prestamo, fecha_devolucion):
        self.id_prestamo = id_prestamo
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.devuelto = False  # por defecto, el prestamo no ha sido devuelto

    def registrar_devolucion(self):
        self.libro.devolver ()
        self.devuelto = True

    def mostrar_info(self):
        return f"Prestamo ID: {self.id_prestamo}, Usuario: {self.usuario.nombre}, Libro: {self.libro.titulo}, Fecha Prestamo: {self.fecha_prestamo}, Fecha Devolucion: {self.fecha_devolucion}, Devuelto: {self.devuelto}"


    