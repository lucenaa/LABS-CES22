class Bolo:
    def __init__(self):
        self.__massa = None
        self.__cobertura = None

    def setMassa(self, massa):
        self.__massa = massa

    def setCobertura(self, cobertura):
        self.__cobertura = cobertura

class Director:

    def escolherBuilder(self, builder):
        self.__builder = builder

    def fazerBolo(self):
        bolo = Bolo()
        massa = self.__builder.getMassa()
        bolo.setMassa(massa)

        cobertura = self.__builder.getCobertura()
        bolo.setCobertura(cobertura)

        return bolo

class Builder:

    def getMassa(self): pass
    def getCobertura(self): pass

class boloCasamento(Builder):

    def getMassa(self):
        massa = Massa()
        print("Escolha entre as massas disponíveis: Chocolate, Mandioca ou Cenoura")
        massa.tipo = str(input())
        return massa

    def getCobertura(self):
        cobertura = Cobertura()
        cobertura.tipo = "Casamento"
        return cobertura


class boloAniversario(Builder):

    def getMassa(self):
        massa = Massa()
        print("Escolha entre as massas disponíveis: Chocolate, Mandioca ou Cenoura")
        massa.tipo = str(input())
        return massa

    def getCobertura(self):
        cobertura = Cobertura()
        cobertura.tipo = "Aniversario"
        return cobertura

class boloInformal(Builder):

    def getMassa(self):
        massa = Massa()
        print("Escolha entre as massas disponíveis: Chocolate, Mandioca ou Cenoura")
        massa.tipo = str(input())
        return massa

    def getCobertura(self):
        cobertura = Cobertura()
        cobertura.tipo = "Informal"
        return cobertura

class Massa:
    tipo = None

class Cobertura:
    tipo = None

def main():

    #exemplo para bolo de casamento:

    boloCasamento = boloCasamento()
    director = Director()
    director.escolherBuilder(boloCasamento)
    bolo = director.fazerBolo()

if __name__ == "main":
    main()