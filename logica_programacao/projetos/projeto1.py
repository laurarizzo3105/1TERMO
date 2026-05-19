# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado
# As entrada deverão ser registradas por placa.
#
# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado
# Se possuir erros informar ao usuário

# Passo 2:
# Verificar tempo de permanência
# Valor a ser cobrado

# Passo 3:
# Saída como será?
# Calcular tempo de permanência
# Se for TAG gerar na fatura da TAG
# Pagar ticket
# Devolver ticket na saída

# Passo 4:
# Gerar relatório de entradas e saídas
# Tratamento de Erros
# Revisão do código


# print("Bem-vindo ao shopping!")
# metodo = print(input("Por favor, escolha o método de entrada: \n 1 - Ticket \n 2 - TAG \n 3 - interfone  \n "))

# if metodo == "Ticket":
#     print("Você escolheu ticket como método de entrada, responda as perguntas para que a cancela possa ser liberada:")
#     modelo = input("qual o modelo do veículo?  ")
#     placa = input("Por favor, digite a placa do veículo:  ")
#     cor = input("Qual a cor do veículo?  ")

#     hora_entrada = float(input("Digite a hora de entrada:  "))
#     valor = float(inpu("Digite o valor a cobrar"))









# print("***************************************")
# print("✨ Seja Bem-Vindo ao estacionamento ✨")
# print("***************************************")

# print("Menu")
# print("Leia e Selecione uma das opções abaixo")
# print("Opção 1: Emitir Tícket")
# print("Opção 2: Verificar TAG")
# print("Opção 3: Interfone")

# try:
#     entrada = int(input("Digite o numero da opção que deseja: "))

#     if entrada == 1:
#         print("Emitindo o ticket...")
#         placa = input("Digite a sua placa: ")
#         modelo = input("Digite o modelo do seu veiculo 🚗: ")
        
        
#         hora_entrada = float(input("Digite a hora de entrada 🕑: "))
#         valor_estacio = float(input("Digite o valor a cobrar por hora 💵: "))
#         hora_saida = float(input("Digite a hora da saida 🕑: "))
        
#         total_permanencia = hora_saida - hora_entrada
#         print(f"Seu tempo de permanencia foi de {total_permanencia}⏲︎ horas")
        
#         total_estacio = total_permanencia * valor_estacio
#         print(f"O valor a ser cobrado foi de R${total_estacio:.2f}💸")
#         print("Devolver ticket")

#     elif entrada == 2:
#         print("Verificando a TAG...")
#         placa = input("Digite a sua placa: ")
#         modelo = input("Digite o modelo do seu veiculo 🚗: ")
#         print("Sua estadia no shopping será cobrada na sua fatura🧾")
#         print("Tenha uma boa estadia!⭐")

#     elif entrada == 3: 
#         print("Acesso pelo interfone 📞")
#         placa = input("Digite a sua placa: ")
#         modelo = input("Digite o modelo do seu veiculo 🚗: ")
#         print("Liberando o seu acesso pelo interfone...")
#         print("Lembrando que sua saida também deverá ser realizada pelo interfone.")
#         print("Tenha uma boa estadia!⭐")
        
#     else:
#         print("Opção inválida. Obrigado pela visita, volte sempre!")

# except ValueError:
#     print("❌ ERRO: Você digitou um valor inválido. Por favor, digite números inteiros para o menu e números para horas/valores (ex: 10.5).")

# print("***************************************************************")


    
