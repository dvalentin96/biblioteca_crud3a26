class usuario: 
    def __init__(self, id_usuario, nombre, correo, carrera):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.matricula = matricula
        self.correo = correo
        self.carrera = carrera
        self.activo = True  # por defecto, el usuario está activo

    def activar(self):
        self.activo = True

    def desactivar(self):
        self.activo = False

    def mostrar_info(self):
        return f"Usuario ID: {self.id_usuario}, Nombre: {self.nombre}, Matricula: {self.matricula}, Correo: {self.correo}, Carrera: {self.carrera}, Activo: {self.activo}"
        
    

