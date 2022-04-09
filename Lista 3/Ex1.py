from abc import ABC, abstractclassmethod, abstractmethod


class Aluno(ABC): # define a classe abstrata aluno, que pode estar em qualquer semestre, é um exemplo simples mas mostra a utilidade de 
                  # se criar classes abstratas, as classes derivadas dessa, são todas alunos, porém cada um tem suas características
                  # (métodos), aqui, foi utilizado um simples exemplo para mostrar as matérias que cada tipo de aluno está tendo, a 
                  # depender do seu semestre
    @abstractmethod
    def mats_do_semestre(self):
        pass


class Aluno1(Aluno):
    def mats_do_semestre(self):
        print("Estou no primeiro semestre e tenho as matérias: MAT12 e MAT17")


class Aluno2(Aluno):
    def mats_do_semestre(self):
        print("Estou no segundo semestre e tenho as matérias: MAT22 e MAT27")


class Aluno3(Aluno):
    def mats_do_semestre(self):
        print("Estou no terceiro semestre e tenho as matérias: MAT32 e MAT36")


class Aluno4(Aluno):
    def mats_do_semestre(self):
        print("Estou no quarto semestre e tenho as matérias: MAT42 e MAT46")


aluno1 = Aluno1()
aluno1.mats_do_semestre()

aluno2 = Aluno2()
aluno2.mats_do_semestre()

aluno3 = Aluno3()
aluno3.mats_do_semestre()

aluno4 = Aluno4()
aluno4.mats_do_semestre()

class Aluno_Aprovado:
    @staticmethod
    def aprovado(nota):
        if nota >= 6.5:
            return True
        else:
            return False

resultado = (Aluno_Aprovado.aprovado(5)) # Aqui foi mostrado um método estático, não foi preciso instanciar um objeto para que fosse chamado o método
print(resultado)                         # o que pode ser uma vantagem quando não há necessidade de criar objetos ou quando se deseja utilizar um método
                                         # da função sem que seja necessariamente instanciado um objeto

class Aluno_Aprovado1: 
    def aprovado(self, nota):
        if nota >= 6.5:
            return True
        else:
            return False

aluno = Aluno_Aprovado1()
resultado = (aluno.aprovado(7)) # Aqui foi mostrado um método de instância, pois foi preciso instanciar um objeto para que o método fosse chamado
print(resultado)