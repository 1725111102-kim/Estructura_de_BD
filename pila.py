class Pila:
    """Pila (LIFO): el último elemento en entrar es el primero en salir."""

    def __init__(self):
        self._elementos = []

    def push(self, elemento):
        """Apila un elemento en la cima."""
        self._elementos.append(elemento)

    def pop(self):
        """Desapila y devuelve el elemento de la cima. None si está vacía."""
        if self.esta_vacia():
            return None
        return self._elementos.pop()

    def peek(self):
        """Devuelve la cima sin quitarla. None si está vacía."""
        if self.esta_vacia():
            return None
        return self._elementos[-1]

    def esta_vacia(self):
        return len(self._elementos) == 0

    def tamano(self):
        return len(self._elementos)

    def vaciar(self):
        self._elementos.clear()

    def desde_la_cima(self):
        """Devuelve los elementos del último al primero (orden descendente)."""
        return list(reversed(self._elementos))