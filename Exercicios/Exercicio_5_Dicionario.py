# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

# 2 - Utilizando o dicionário criado no item 1:

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.
# 3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

pessoas = [{'nome': 'Nadia', 'idade' : '41', 'cidade' : 'Curitiba'},
           {'nome' : 'Ayrton', 'idade' : '33', 'cidade' : 'Sao José dos Pinhais'},
           {'nome' : 'Laura', 'idade' : '6', 'cidade' : 'Curitiba'},
           {'nome' : 'Sebastian', 'idade' : '6', 'cidade' : 'Curitiba'}]

pessoas[0]['idade'] = 20                                                            # forma de alterar a idade de um individuo
pessoas[1]['profissão'] = 'Não sei'
for pessoa in pessoas:                                                              # forma de alterar de todos.
    pessoa['idade'] = 20
    pessoa['nome'] = 'Naná' if pessoa['nome'] == 'Nadia' else pessoa['nome']        # alteração condicional
    pessoa['profissão'] = 'Advogada' if pessoa['nome'] == 'Naná' else "Pensando"    # Adicionando Profissão condicional
    del pessoa['cidade']                                                            # Remover um item
    print(pessoa)
    

