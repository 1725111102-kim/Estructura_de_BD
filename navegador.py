from pila import Pila


class Navegador:
    """Simula el historial de un navegador web usando una pila."""

    def __init__(self):
        self._historial = Pila()

    def visitar(self, url):
        """Registra una nueva página visitada."""
        self._historial.push(url)

    def regresar(self):
        """
        Regresa a la página anterior.
        Devuelve (pagina_que_se_cerro, pagina_actual) o None si no hay
        una página anterior a la cual regresar.
        """
        if self._historial.tamano() < 2:
            return None
        cerrada = self._historial.pop()
        return cerrada, self._historial.peek()

    def pagina_actual(self):
        return self._historial.peek()

    def historial(self):
        """Historial en orden descendente (de la más reciente a la más antigua)."""
        return self._historial.desde_la_cima()

    def esta_vacio(self):
        return self._historial.esta_vacia()

    def eliminar_historial(self):
        self._historial.vaciar()