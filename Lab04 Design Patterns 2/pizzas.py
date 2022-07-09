class Ingrediente:
    def getDescription(self):
        return self.__class__.__name__
    def getTotalCost(self):
        return self.__class__.cost

class Prato(Ingrediente):
    cost = 0.0

class Decorator(Ingrediente):
    def __init__(self, Ingrediente):
        self.ingrediente = Ingrediente
    def getTotalCost(self):
        return self.ingrediente.getTotalCost() + Ingrediente.getTotalCost(self)
    def getDescription(self):
        return self.ingrediente.getDescription() + " " + Ingrediente.getDescription(self)

class Massa(Ingrediente):
    cost = 5.50
    def __init__(self, Ingrediente):
        Decorator.__init__(self, Ingrediente)

class Molho(Ingrediente):
    cost = 2
    def __init__(self, Ingrediente):
        Decorator.__init__(self, Ingrediente)

class Queijo(Ingrediente):
    cost = 5
    def __init__(self, Ingrediente):
        Decorator.__init__(self, Ingrediente)

class Calabresa(Ingrediente):
    cost = 3
    def __init__(self, Ingrediente):
        Decorator.__init__(self, Ingrediente)

class Peperoni(Ingrediente):
    cost = 7
    def __init__(self, Ingrediente):
        Decorator.__init__(self, Ingrediente)

class Frango(Ingrediente):
    cost = 4
    def __init__(self, Ingrediente):
        Decorator.__init__(self, Ingrediente)

class Catupiry(Ingrediente):
    cost = 3
    def __init__(self, Ingrediente):
        Decorator.__init__(self, Ingrediente)

class Azeitona(Ingrediente):
    cost = 1
    def __init__(self, Ingrediente):
        Decorator.__init__(self, Ingrediente)

class Cebola(Ingrediente):
    cost = 1
    def __init__(self, Ingrediente):
        Decorator.__init__(self, Ingrediente)

class Ovo(Ingrediente):
    cost = 2
    def __init__(self, Ingrediente):
        Decorator.__init__(self, Ingrediente)


pizzaFrangoCatupiry = Massa(Molho(Frango(Catupiry(Azeitona(Prato)))))
print(pizzaFrangoCatupiry.getDescription()+": $" + str(pizzaFrangoCatupiry.getTotalCost()))
