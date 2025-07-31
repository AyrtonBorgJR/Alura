class Restaurante():
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_pizza = Restaurante()

restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Brasileiro'
"""1. Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca
 da classe Restaurante."""
restaurante_praca.categoria = "Italiano"
restaurantes = [restaurante_pizza, restaurante_praca]
print(restaurantes)
print(restaurante_praca.nome)

"""2. Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante."""
nome_instancia = restaurante_praca.nome
print(nome_instancia)

"""
3. Verifique o valor inicial do atributo ativo para a instância restaurante_praca 
e exiba uma mensagem informando se o restaurante está ativo ou inativo.
"""
if restaurante_praca.ativo == False:
    print("Restaurante inoperante")
else:
    print("Restaurante ativo")

"""
4. Acesse o valor do atributo de classe categoria diretamente da classe Restaurante 
e armazene em uma variável chamada categoria.
"""
categoria = Restaurante.categoria
print(f'a categoria é {categoria}')
"""
5. Altere o valor do atributo nome para 'Bistrô'.
"""
restaurante_pizza.nome = "Bistrô"
""""
6. Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 
'Pizza Place' e categoria 'Fast Food'.
"""
restaurante_place = Restaurante()
restaurante_place.nome = "Pizza Place"
restaurante_place.categoria = "Fast Food"
"""
7. Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
"""
if restaurante_place.categoria == "Fast Food":
    print("A categoria é Fast Food")
else:
    print("Categoria incorreta")
"""
8. Mude o estado da instância restaurante_pizza para ativo.
"""
restaurante_place.ativo = True
print(restaurante_place.ativo)
"""
9. Imprima no console o nome e a categoria da instância restaurante_praca.
"""
print(restaurante_praca.nome)
print(restaurante_praca.categoria)