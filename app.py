from crud import (
    agregar_libro,
    mostrar_libros,
    buscar_libros,
    actualizar_libro,
    eliminar_libro
)


def seleccionar_estado():
    print("\nEstado de lectura:")
    print("1. Pendiente")
    print("2. Leyendo")
    print("3. Terminado")

    opcion = input("Seleccione el estado: ")

    if opcion == "1":
        return "Pendiente"
    elif opcion == "2":
        return "Leyendo"
    elif opcion == "3":
        return "Terminado"
    else:
        print("Estado no válido.")
        return None


def menu():
    while True:
        print("\n===== BIBLIOTECA PERSONAL =====")
        print("1. Agregar libro")
        print("2. Actualizar libro")
        print("3. Eliminar libro")
        print("4. Mostrar todos los libros")
        print("5. Buscar libro")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        # AGREGAR
        if opcion == "1":
            print("\n--- AGREGAR LIBRO ---")

            titulo = input("Título: ")
            autor = input("Autor: ")
            genero = input("Género: ")

            estado = seleccionar_estado()

            if estado is None:
                continue

            agregar_libro(titulo, autor, genero, estado)

        # ACTUALIZAR
        elif opcion == "2":
            print("\n--- ACTUALIZAR LIBRO ---")

            try:
                id_libro = int(input("ID del libro: "))
            except ValueError:
                print("El ID debe ser un número.")
                continue

            titulo = input("Nuevo título: ")
            autor = input("Nuevo autor: ")
            genero = input("Nuevo género: ")

            estado = seleccionar_estado()

            if estado is None:
                continue

            actualizar_libro(
                id_libro,
                titulo,
                autor,
                genero,
                estado
            )

        # ELIMINAR
        elif opcion == "3":
            print("\n--- ELIMINAR LIBRO ---")

            try:
                id_libro = int(input("ID del libro: "))
            except ValueError:
                print("El ID debe ser un número.")
                continue

            eliminar_libro(id_libro)

        # MOSTRAR
        elif opcion == "4":
            mostrar_libros()

        # BUSCAR
        elif opcion == "5":
            print("\n--- BUSCAR LIBRO ---")

            texto = input(
                "Escriba el título, autor o género que desea buscar: "
            )

            buscar_libros(texto)

        # SALIR
        elif opcion == "6":
            print("\n¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()