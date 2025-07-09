# IMPRIMA A FRASE Python na Escola de Programação da Alura.
print("Python na Escola de Programação da Alura.")

#Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
nome = "Ayrton"
idade = 33

print(f'Meu nome é {nome}, minha idade é {idade} anos')

# Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:
for i in "ALURA":
    print(i[0])
#OU
print('A','L','U','R','A',sep='\n')

#Imprima a frase: O valor arredondado de pi é: {pi_arredondado} use variável e arredondado para apenas duas casas decimais:
pi = 3.14159
print(f"O valor arredondado de pi é: {pi:.2f}")

def configurar_tempo_foco():
    tempo = input("Digite o tempo de foco (25-45 min): ")
    if 25 <= int(tempo) <= 45:
        print("Tempo configurado para", tempo, "minutos.")
    elif tempo < 25 or tempo > 45:
        print("Valor inválido. Configure um tempo entre 25 e 45 minutos.")
configurar_tempo_foco()