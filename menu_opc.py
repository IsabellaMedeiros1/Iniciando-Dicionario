''' Menu de opções '''

print("Menu Principal") 
print("\n\n")
print("(C)adastras Nova (B)icicleta")
("Cadastrar (U)suário")
print ("(C)alcular seguro")
print("(L)istar Usuarios")
print ("Listar B(I)cicletas")
print("(E)xit")

print("Informe a opção desejada: ")
opcao = input().upper()[0] #[0] serve para pegar a primeira letra da palavra
if opcao == "B":
    print("Você escolheu a opção Cadastrar Bicicleta")
elif opcao == "U":
    print("Você escolheu a opção Cadastrar Usuário")
elif opcao == "C":
    print("Você escolheu a opção Calcular seguro")
elif opcao == "L":
    print("Você escolheu a opção Listar Usuarios")
elif opcao == "I":
    print("Você escolheu a opção Listar Bicicletas")
elif opcao == "E":
    print("Até breve")
else:
    print("Opção inválida")
