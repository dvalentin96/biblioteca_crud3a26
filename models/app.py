from dao.libro_dao import LibroDAO
from models.libro import libro

def main(): 
    try:
        libro_dao = LibroDAO()

        libros = libro_dao.obtener_todos()

        print("=== Libros en la biblioteca===")

        if len(libros)== 0:
            print("No hay libros registrados")
        else:
            for libro in libros:
                print("------------------------------------------")

                print(
                    f"ID: {libro.id}, Titulo: {libro.titulo},"
                    f"Autor: {libro.autor}, ISBN: {libro.isbn},"
                    f"Disponible: {'Si'if libro.disponible else 'No'}"
                )
                print("------------------------------------------")
        print("\n Conexion a la base de datos")
    except Exception as e:
        print("Error:")
        print (e)

if_name_=="_main_":
    main()

