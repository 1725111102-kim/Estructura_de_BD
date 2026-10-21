class Pila:
    def __init__(self):
        self.items = []


    def push(self, elemento):
        self.items.append(elemento)


    def pop(self):
        if self.esta_vacia():
            return None
        return self.items.pop()


    def peek(self):
        if self.esta_vacia():
            return None
        return self.items[-1]


    def esta_vacia(self):
        return len(self.items) == 0


    def tamano(self):
        return len(self.items)


    def vaciar(self):
        self.items = []


    def todos(self):
        return self.items