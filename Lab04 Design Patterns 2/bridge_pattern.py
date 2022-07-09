from abc import abstractmethod

class Veiculo:
    def setMotorizacao(self, motorizacao):
        self.motorizacao = motorizacao

    def setNumeroDeRodas(self, NumeroDeRodas):
        self.NumeroDeRodas = NumeroDeRodas

    def setPeso(self, Peso):
        self.Peso = Peso
    

class Carro(Veiculo):
    def __init__(self, motorizacao, NumeroDeRodas, Peso):
        super().setMotorizacao(motorizacao)
        self.NumeroDeRodas = 4
        self.Peso = 1200

    def __str__(self):
        return f'Informacoes:{type(self).__name__}, Motorização: {self.Motorizacao}, Número de Rodas: {self.NumeroDeRodas}, Peso do veículo: {self.Peso}'

class Moto(Veiculo):
    def __init__(self, motorizacao, NumeroDeRodas, Peso):
        super().setMotorizacao(motorizacao)
        self.NumeroDeRodas = 2
        self.Peso = 150

    def __str__(self):
        return f'Informacoes:{type(self).__name__}, Motorização: {self.Motorizacao}, Número de Rodas: {self.NumeroDeRodas}, Peso do veículo: {self.Peso}'

class Caminhao(Veiculo):
    def __init__(self, motorizacao, NumeroDeRodas, Peso):
        super().setMotorizacao(motorizacao)
        self.NumeroDeRodas = 8
        self.Peso = 16000

    def __str__(self):
        return f'Informacoes:{type(self).__name__}, Motorização: {self.Motorizacao}, Número de Rodas: {self.NumeroDeRodas}, Peso do veículo: {self.Peso}'

class Motorizacao:
    def escolher(self): pass

class Eletrica(Motorizacao):
    def __init__(self):
        self.escolher()
    def escolher(self):
        self._motorizacao = "Elétrica"

class Hibrida(Motorizacao):
    def __init__(self):
        self.escolher()
    def escolher(self):
        self._motorizacao = "Híbrida"

class Combustao(Motorizacao):
    def __init__(self):
        self.escolher()
    def escolher(self):
        self._motorizacao = "Combustão"
    
veic1 = Moto(Combustao())
veic2 = Carro(Eletrica())
veic3 = Caminhao(Hibrida())

print(veic1)
print(veic2)
print(veic3)