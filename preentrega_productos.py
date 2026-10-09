productos = []

while True:
    print("=" * 40)
    print("Sistema de gestion de productos")
    print("=" * 40)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Elegi una de las opciones (1-5): ").strip()

    if opcion == "1":
        print("--- Agregar producto ---")

        nombre = input("Nombre del producto: ").strip()

        while nombre == "":
            print("Error: el nombre no puede estar vacio.")
            nombre = input("Nombre del producto: ").strip()

        categoria = input("Categoria del producto: ").strip()

        while categoria == "":
            print("Error: la categoria no puede estar vacia.")
            categoria = input("Categoria del producto: ").strip()

        precio_str = input("Precio (sin centavos): ").strip()

        while not precio_str.isdigit() or int(precio_str) <= 0:
            print("Error: ingresa un precio entero mayor que cero.")
            precio_str = input("Precio (sin centavos): ").strip()

        precio = int(precio_str)

        datos = [nombre, categoria, precio]
        productos.append(datos)

        print("Producto agregado correctamente.")

    elif opcion == "2":
        print("--- Lista de productos ---")

        if len(productos) == 0:
            print("Todavia no hay productos cargados.")
        else:
            for i in range(len(productos)):
                print(f"ID: {i + 1}")
                print(f"Nombre: {productos[i][0]}")
                print(f"Categoria: {productos[i][1]}")
                print(f"Precio: ${productos[i][2]}")
                print("-" * 30)

    elif opcion == "3":
        print("--- Buscar producto ---")

        if len(productos) == 0:
            print("Todavia no hay productos cargados.")
        else:
            busqueda = input(
                "Nombre del producto a buscar: "
            ).strip().lower()

            while busqueda == "":
                print("Error: escribi un nombre para buscar.")
                busqueda = input(
                    "Nombre del producto a buscar: "
                ).strip().lower()

            encontrado = 0

            for i in range(len(productos)):
                if busqueda in productos[i][0].lower():
                    print(f"ID: {i + 1}")
                    print(f"Nombre: {productos[i][0]}")
                    print(f"Categoria: {productos[i][1]}")
                    print(f"Precio: ${productos[i][2]}")
                    print("-" * 30)
                    encontrado += 1

            if encontrado == 0:
                print("No se encontraron resultados.")
            else:
                print(f"Productos encontrados: {encontrado}")

    elif opcion == "4":
        print("--- Eliminar producto ---")

        if len(productos) == 0:
            print("No hay productos registrados para eliminar.")
        else:
            for i in range(len(productos)):
                print(
                    f"{i + 1}. {productos[i][0]} - "
                    f"{productos[i][1]} - ${productos[i][2]}"
                )

            id_eliminar = input(
                "Numero de producto a eliminar: "
            ).strip()

            while (
                not id_eliminar.isdigit()
                or int(id_eliminar) < 1
                or int(id_eliminar) > len(productos)
            ):
                print("Error: ingresa un numero de producto valido.")
                id_eliminar = input(
                    "Numero de producto a eliminar: "
                ).strip()

            posicion = int(id_eliminar) - 1
            eliminado = productos.pop(posicion)

            print(f"Se elimino el producto: {eliminado[0]}")

    elif opcion == "5":
        print("Gracias por usar nuestro sistema.")
        break

    else:
        print("Opcion no valida. Elegi entre 1 y 5.")