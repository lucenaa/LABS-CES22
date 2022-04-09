class Quadrilatero(object):
    def caracteristica(self):
        print("Sou um polígono de 4 lados")

class Retangulo(Quadrilatero):
    def metodo(self):
        super().caracteristica()
    

    def caracteristica1(self):
        print("Eu possuo 4 ângulos retos")

class Quadrado(Retangulo):
    def metodo1(self):
        super().metodo()
        super().caracteristica1()
    

    def caracteristica2(self):
        print("Eu possuo 4 lados iguais")

print("Quadrilátero:")
exemplo1 = Quadrilatero()
exemplo1.caracteristica()

print("Retângulo:")
exemplo2 = Retangulo()
exemplo2.metodo()
exemplo2.caracteristica1()

print("Quadrado:")
exemplo3 = Quadrado()
exemplo3.metodo1()
exemplo3.caracteristica2()

