# DAO: Data access object
# libro_dao: objeto de acceso a datos para la tabla libro
from database.conexion import Conexion 
from models.libro import Libro 

class libroDAO:

    #SELEC * from libro
    def obtener_todos (self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM libro")
        registros = cursor.fetchall()

        libros = []
        for registro in registros:
            libro = Libro(registro.id, registro.titulo, registro.autor, registro.isbn, registro.disponible)
            libros.append(libro)

        cursor.close()
        conexion.close()
        return libros

