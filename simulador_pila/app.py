from navegador import Navegador




def mostrar_menu():
    print("")
    print("===== NAVEGADOR WEB =====")
    print("1. Visitar una pagina web")
    print("2. Regresar a la pagina anterior")
    print("3. Mostrar la pagina actual")
    print("4. Mostrar el historial")
    print("5. Verificar si el historial esta vacio / eliminar historial")
    print("6. Salir")




def main():
    navegador = Navegador()


    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ")


        if opcion == "1":
            url = input("Escribe la pagina que quieres visitar: ")
            if url.strip() == "":
                print("No escribiste nada.")
            else:
                navegador.visitar(url)
        elif opcion == "2":
            navegador.regresar()
        elif opcion == "3":
            navegador.pagina_actual()
        elif opcion == "4":
            navegador.mostrar_historial()
        elif opcion == "5":
            navegador.verificar_o_eliminar()
        elif opcion == "6":
            print("Saliendo del programa, hasta luego!")
            break
        else:
            print("Opcion no valida, intenta de nuevo.")




if __name__ == "__main__":
    main()