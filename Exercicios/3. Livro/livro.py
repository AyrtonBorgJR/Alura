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
    def verificar_disponibilidade(ano):
        disponiveis = []
        print(f'TITULO DISPONIVEIS DE {ano}')
        print(f'{"Titulo":<18} | {"Autor":<15} | {"Publicação":<10} | {"Disponivel":<3}' )
        for livro in Livro.livros:
            if livro._ano_publicacao == ano and livro._disponivel:
                disponiveis.append(livro)
                print(f'{livro._titulo:<18} | {livro._autor:<15} | {livro._ano_publicacao:<10} | {livro.ativo:<3}')
        return disponiveis

    @property
    def ativo(self):
        return "✓" if self._disponivel else "⌧"

livro1 = Livro("Jantar Secreto", "Rafael Montes", "2025")
livro2 = Livro("Verity", "Colen Hoover", "2025")
livro3 = Livro("Jester", "GTA", "2025")

livro2.emprestar()

ver2025 = Livro.verificar_disponibilidade("2025")


