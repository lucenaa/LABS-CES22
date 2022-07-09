class Livros:
    def __init__(self):
        self.livros = []

    def inserir_livro(self, livro, preco, autor):
        self.livros.append(livro)
        self.livro.preco = preco
        self.livro.autor = autor

    def remover_livro(self, livro):
        if livro in self.livros:
            self.livros.remove(livro)

    def consultar_livro_nome(self, livro):
        if livro in self.livros:
            print("O livro consultado está em estoque")
        else:
            print("O livro consultado não está em estoque")

    def consultar_livro_autor(self, autor):
        x = []
        for livro in self.livros:
            if livro.autor == autor:
                x.append(livro)
        return x

    def imposto(self, livro, taxa):
        self.imposto = livro.preco * taxa
        return self.imposto

    def comprar(self, livro):
        if livro in self.livros:
            Cliente.comprar_livro(livro)
            self.livros.remove(livro)

class Cliente:
    def __init__(self, nome, email, compras):
        self.nome = nome
        self.email = email
        self.compras = compras

    def comprar_livro(self, livro):
        self.compras.append(livro)




    
