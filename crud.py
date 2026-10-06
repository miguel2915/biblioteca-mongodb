from database import libros


def siguiente_id():
    ultimo_libro = libros.find_one(sort=[("id", -1)])

    if ultimo_libro is None:
        return 1

    return ultimo_libro["id"] + 1


def validar_datos(titulo, autor, genero, estado):
    if not titulo.strip():
        return False

    if not autor.strip():
        return False

    if not genero.strip():
        return False

    if estado not in ["Pendiente", "Leyendo", "Terminado"]:
        return False

    return True


def agregar_libro(titulo, autor, genero, estado):
    if not validar_datos(titulo, autor, genero, estado):
        print("Los datos del libro no son válidos.")
        return

    nuevo_libro = {
        "id": siguiente_id(),
        "titulo": titulo.strip(),
        "autor": autor.strip(),
        "genero": genero.strip(),
        "estado": estado
    }

    try:
        libros.insert_one(nuevo_libro)
        print("Libro agregado correctamente.")
    except Exception as e:
        print(f"Error al agregar el libro: {e}")


def mostrar_libros():
    try:
        resultados = libros.find().sort("id", 1)

        encontrados = False

        print("\n--- LISTA DE LIBROS ---")

        for libro in resultados:
            encontrados = True

            print(
                f"ID: {libro.get('id')} | "
                f"Título: {libro.get('titulo')} | "
                f"Autor: {libro.get('autor')} | "
                f"Género: {libro.get('genero')} | "
                f"Estado: {libro.get('estado')}"
            )

        if not encontrados:
            print("No hay libros registrados.")

    except Exception as e:
        print(f"Error al mostrar los libros: {e}")


def buscar_libros(texto):
    try:
        filtro = {
            "$or": [
                {"titulo": {"$regex": texto, "$options": "i"}},
                {"autor": {"$regex": texto, "$options": "i"}},
                {"genero": {"$regex": texto, "$options": "i"}}
            ]
        }

        resultados = libros.find(filtro).sort("id", 1)

        encontrados = False

        print("\n--- RESULTADOS DE BÚSQUEDA ---")

        for libro in resultados:
            encontrados = True

            print(
                f"ID: {libro.get('id')} | "
                f"Título: {libro.get('titulo')} | "
                f"Autor: {libro.get('autor')} | "
                f"Género: {libro.get('genero')} | "
                f"Estado: {libro.get('estado')}"
            )

        if not encontrados:
            print("No se encontraron libros.")

    except Exception as e:
        print(f"Error al buscar libros: {e}")


def actualizar_libro(id_libro, titulo, autor, genero, estado):
    if not validar_datos(titulo, autor, genero, estado):
        print("Los datos del libro no son válidos.")
        return

    try:
        resultado = libros.update_one(
            {"id": id_libro},
            {
                "$set": {
                    "titulo": titulo.strip(),
                    "autor": autor.strip(),
                    "genero": genero.strip(),
                    "estado": estado
                }
            }
        )

        if resultado.matched_count == 0:
            print("No se encontró un libro con ese ID.")
        else:
            print("Libro actualizado correctamente.")

    except Exception as e:
        print(f"Error al actualizar el libro: {e}")


def eliminar_libro(id_libro):
    try:
        resultado = libros.delete_one({"id": id_libro})

        if resultado.deleted_count == 0:
            print("No se encontró un libro con ese ID.")
        else:
            print("Libro eliminado correctamente.")

    except Exception as e:
        print(f"Error al eliminar el libro: {e}")