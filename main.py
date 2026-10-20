from navegador import Navegador


def mostrar_menu():
    print("\n===== SIMULADOR DE NAVEGADOR WEB =====")
    print("1. Visitar una página web")
    print("2. Regresar a la página anterior")
    print("3. Mostrar la página actual")
    print("4. Mostrar el historial de navegación (descendente)")
    print("5. Verificar si el historial está vacío / eliminar historial")
    print("6. Salir")


def visitar(navegador):
    url = input("Ingresa la URL de la página: ").strip()
    if url == "":
        print("La URL no puede estar vacía.")
        return
    navegador.visitar(url)
    print(f"Visitando: {url}")


def regresar(navegador):
    resultado = navegador.regresar()
    if resultado is None:
        print("No hay una página anterior a la cual regresar.")
    else:
        cerrada, actual = resultado
        print(f"Se cerró: {cerrada}")
        print(f"Página actual: {actual}")


def mostrar_actual(navegador):
    actual = navegador.pagina_actual()
    if actual is None:
        print("No hay ninguna página abierta.")
    else:
        print(f"Página actual: {actual}")


def mostrar_historial(navegador):
    if navegador.esta_vacio():
        print("El historial está vacío.")
        return
    print("\n--- Historial (de la más reciente a la más antigua) ---")
    for i, url in enumerate(navegador.historial(), start=1):
        marca = "  <-- actual" if i == 1 else ""
        print(f"{i}. {url}{marca}")


def verificar_o_eliminar(navegador):
    if navegador.esta_vacio():
        print("El historial está vacío.")
        return
    print("El historial NO está vacío.")
    respuesta = input("¿Deseas eliminar el historial? (s/n): ").strip().lower()
    if respuesta == "s":
        navegador.eliminar_historial()
        print("Historial eliminado correctamente.")
    else:
        print("No se eliminó el historial.")


def main():
    navegador = Navegador()
    acciones = {
        "1": visitar,
        "2": regresar,
        "3": mostrar_actual,
        "4": mostrar_historial,
        "5": verificar_o_eliminar,
    }

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "6":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        elif opcion in acciones:
            acciones[opcion](navegador)
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()