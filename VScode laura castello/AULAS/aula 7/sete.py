# projeto cancela automatica



# Criar um algoritmo para que:

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

# passo1:

# print("Bem-vindo ao shoppping center!")
# print("Por favor digite as informações sobre seu veículo abaixo")
# print(input("Quala placa do veículo? "))
# print(input("Qual o modelo do veículo? "))
# entrada = input("Qual a opção de entrada? \n 1- Ticket \n 2- Tag \n 3- Interfone \n ")



# if entrada == "Ticket":
#     hora_entrada = float(input("Digite a hora de entrada ")) 
#     valor = float(input("Digite o valor do estacionamento"))
#     hora_saida = float(input("Digite a hora de saída"))
#     total = hora_entrada - hora_saida 
#     print(f"Seu tempo de permanência {total} em horas")
#     total_estacionamento = total * valor
#     print(f"O valor a ser cobrado foi de R${total_estacionamento:.2f}")

# elif entrada == "Tag":
#     print("Bem-Vindo ao Shopping")
#     print("Sua permanência no Shopping será cobrada na sua fatura")

# elif entrada == "Interfone":
#     print("Bem-Vindo ao Shopping")
#     print("Liberando acesso pelo Interfone")
#     print("Sua saída deverá ser feita também pelo Interfone")

# else:
#     print("Obrigado pela visita")
