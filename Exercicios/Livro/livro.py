class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._ano_publicacao} | {self.ativo:<3}'
    
    @classmethod
    def listar_livros(cls):
        print(f'{"Titulo":<18} | {"Autor":<15} | {"Publicação":<10} | {"Disponivel":<3}' )
        for livro in cls.livros:
            print(f'{livro._titulo:<18} | {livro._autor:<15} | {livro._ano_publicacao:<10} | {livro.ativo:<3}')
    
    def emprestar(self):
        self._disponivel = False 

    @staticmethod
    if 

    @property
    def ativo(self):
        return "✓" if self._disponivel else "⌧"


livro1 = Livro("Jantar Secreto", "Rafael Montes", "2018")
livro2 = Livro("Verity", "Colen Hoover", "2016")
livro3 = Livro("Jester", "GTA", "2025")

livro2.emprestar()

Livro.listar_livros()


"""

4. Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como
parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

5. Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

6. No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível
ou não após o empréstimo.

7. No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros
disponíveis publicados em um ano específico.

8. Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da
classe Livro e exiba a mensagem formatada utilizando o método str."""
