
nome = []
idade = []
estado = []
cidade = []

resposta = "Y"


while resposta == "Y":
    nome.append(input("Digite seu nome: "))
    idade.append(int(input("Digite sua idade: ")))
    estado.append(input("Digite seu estado: "))
    cidade.append(input("digite sua cidade: "))
    print(" ")
    resposta = input("Deseja continuar [Y/N]: ").upper()

else: print(" ")

for  indice in range(0, len(nome)) :
    print("\nPessoa", (indice+1))
    print("Nome....", nome[indice])
    print("Idade....", idade[indice])
    print("Estado....", estado[indice])
    print("Cidade....", cidade[indice])
    print("--------------------------")

busca=input("digite a cidade que você quer buscar: ")
print(" ")
for indice in range(0, len(cidade)):
    if busca==cidade[indice]:
        print("Nome....", nome[indice])
        print("Estado....", estado[indice])
        print("Idade.....", idade[indice])
        print("--------------------------")