from abc import ABC, abstractmethod

class padariaABS(ABC):

    @abstractmethod
    def criar_bolo_chocolate(self) -> BoloChocolateABS:
        pass

    @abstractmethod
    def criar_bolo_mandioca(self) -> BoloMandiocaABS:
        pass

    @abstractmethod
    def criar_bolo_cenoura(self) -> BoloCenouraABS:
        pass

class padariaANIVERSARIO(padariaABS):
    
    def criar_bolo_chocolate(self) -> BoloChocolateABS:
        return BoloChocolateABS_ANIVERSARIO()

    def criar_bolo_mandioca(self) -> BoloMandiocaABS:
        return BoloMandiocaABS_ANIVERSARIO()

    def criar_bolo_cenoura(self) -> BoloCenouraABS:
        return BoloCenouraABS_ANIVERSARIO()

class padariaCASAMENTO(padariaABS):
    
    def criar_bolo_chocolate(self) -> BoloChocolateABS:
        return BoloChocolateABS_CASAMENTO()

    def criar_bolo_mandioca(self) -> BoloMandiocaABS:
        return BoloMandiocaABS_CASAMENTO()

    def criar_bolo_cenoura(self) -> BoloCenouraABS:
        return BoloCenouraABS_CASAMENTO()

class padariaINFORMAL(padariaABS):
    
    def criar_bolo_chocolate(self) -> BoloChocolateABS:
        return BoloChocolateABS_INFORMAL()

    def criar_bolo_mandioca(self) -> BoloMandiocaABS:
        return BoloMandiocaABS_INFORMAL()

    def criar_bolo_cenoura(self) -> BoloCenouraABS:
        return BoloCenouraABS_INFORMAL()

class BoloChocolateABS(ABC):
    @abstractmethod
    def sabor(self) -> str:
        return "bolo de chocolate feito"

class BoloChocolateABS_ANIVERSARIO(BoloChocolateABS):
    
    def cobertura(self) -> str:
        return "inserida cobertura de aniversário no bolo de chocolate"

class BoloChocolateABS_CASAMENTO(BoloChocolateABS):
    
    def cobertura(self) -> str:
        return "inserida cobertura de casamento no bolo de chocolate"

class BoloChocolateABS_INFORMAL(BoloChocolateABS):
    
    def cobertura(self) -> str:
        return "inserida cobertura informal no bolo de chocolate"

class BoloMandiocaABS(ABC):
    @abstractmethod
    def sabor(self) -> str:
        return "bolo de mandioca feito"

class BoloMandiocaABS_ANIVERSARIO(BoloMandiocaABS):
    
    def cobertura(self) -> str:
        return "inserida cobertura de aniversário no bolo de mandioca"

class BoloMandiocaABS_CASAMENTO(BoloMandiocaABS):
    
    def cobertura(self) -> str:
        return "inserida cobertura de casamento no bolo de mandioca"

class BoloMandiocaABS_INFORMAL(BoloMandiocaABS):
    
    def cobertura(self) -> str:
        return "inserida cobertura informal no bolo de mandioca"

class BoloCenouraABS(ABC):
    @abstractmethod
    def sabor(self) -> str:
        return "bolo de cenoura feito"

class BoloCenouraABS_ANIVERSARIO(BoloCenouraABS):
    
    def cobertura(self) -> str:
        return "inserida cobertura de aniversário no bolo de cenoura"

class BoloCenouraABS_CASAMENTO(BoloCenouraABS):
    
    def cobertura(self) -> str:
        return "inserida cobertura de casamento no bolo de cenoura"]

class BoloCenouraABS_INFORMAL(BoloCenouraABS):
    
    def cobertura(self) -> str:
        return "inserida cobertura informal no bolo de cenoura"

def cliente(factory: padariaABS) -> None:
    bolo_cenoura = factory.criar_bolo_cenoura()
    bolo_chocolate = factory.criar_bolo_chocolate()
    bolo_mandioca = factory.criar_bolo_mandioca()
    
if __name__ == "__main__":
    cliente(padariaANIVERSARIO)
    cliente(padariaCASAMENTO)
    cliente(padariaINFORMAL)

