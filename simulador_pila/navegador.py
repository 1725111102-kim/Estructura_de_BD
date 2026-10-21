from Pila import Pila


class Navegador:
    def __init__(self):
        self.historial = Pila()


    def visitar(self, url):
        self.historial.push(url)
        print("Visitando:", url)


    def regresar(self):
        if self.historial.esta_vacia():
            print("No hay paginas en el historial.")
        elif self.historial.tamano() == 1:
            print("No hay pagina anterior, solo estas en:", self.historial.peek())
        else:
            quitada = self.historial.pop()
            print("Saliste de:", quitada)
            print("Ahora estas en:", self.historial.peek())


    def pagina_actual(self):
        if self.historial.esta_vacia():
            print("No hay ninguna pagina abierta.")
        else:
            print("Pagina actual:", self.historial.peek())


    def mostrar_historial(self):
        if self.historial.esta_vacia():
            print("El historial esta vacio.")
        else:
            print("Historial (de la mas reciente a la mas antigua):")
            paginas = self.historial.todos()
            i = len(paginas) - 1
            while i >= 0:
                print("-", paginas[i])
                i = i - 1


    def verificar_o_eliminar(self):
        if self.historial.esta_vacia():
            print("El historial esta vacio.")
        else:
            print("El historial tiene", self.historial.tamano(), "paginas.")
            respuesta = input("Quieres eliminarlo? (s/n): ")
            if respuesta.lower() == "s":
                self.historial.vaciar()
                print("Historial correctamente eliminado.")
            else:
                print("No se elimino el historial.")