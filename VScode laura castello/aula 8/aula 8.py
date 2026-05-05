# 1. O Problema da Idade
# idade = input("Digite sua idade: ")
# if idade >=18:
#     print("Você é maior de idade.")

# corrigido:

# idade = int(input("Digite sua idade: "))
# if idade >= 18:
#     print("Você é maior de idade")

# melhorado

# idade = int(input("Por favor, digite sua idade "))
# if idade >=18:
#     print("Você é maior de idade.")
# else:
#     print("Você é menor de idade")



# 2. A Escrita Fiel
# nome = "Mariana"
# print("Seja bem-vinda, nome!")

# corrigido:
# nome = "Mariana"
# print(f"Seja bem-vinda, {nome}")

# melhorado:
# nome = input("Qual o seu nome?")
# print(f"Seja bem-vinda, {nome}")



# 3. Falta de Espaço
# numero = 10
# if numero > 5:
#     print("O número é maior que cinco")
# else:
#     print("O número pe menor ou igual a cinco")

# corrigido: 
# numero = 10 
# numero = float(input("Qual o número?"))
# if numero > 5:
#     print("O número é maior que cinco.")
# else:
#     print("O númro é menor ou igual a cinco")

# melhorado:
# numero = float(input("Qual o número?  "))
# if numero > 5:
#     print("O número é maior que cinco.")
# elif numero == 5:
#     print("O número é igual a cinco")
# else:
#     print("O númro é menor que cinco")



# 4. Esquecimento Fatal
# usuario = "aluno123"
# if usuario == "aluno123"
# print("Login realizado com sucesso.")

# corrigido:
# usuario = "aluno123"
# if usuario == "aluno123":
#     print("Login realizado com sucesso")

# melhorado:
# usuario = "aluno123"
# if usuario == "aluno123":
#     print("Login realizado com sucesso")
# else:
#     print("Acesso negado")


# 5. Atribuição vs. Comparação
# clima = "ensolarado"
# if clima = "chuvoso":
# print("Leve um guarda-chuva")

# corrigido:
# clima = "ensolarado"
# if clima == "chuvoso":
#     print("Leve um guarda-chuva")

# melhorado:
# clima = input("O clima hoje está chuvoso ou ensolarado? ")
# if clima == "ensolarado":
#     print("O dia está lindo hoje!")
# else:
#     print("Leve um guarda-chuva")



# 6. Misturando Alhos com Bugalhos
# pontos = 50
# print("Parabéns! Você fez" + pontos + "pontos.")

# corrigido:
# pontos = 50
# print(f"Parabéns! Você fez {pontos} pontos.")

# melhorado:
# pontos = float(input("Quantos pontos você fez?"))
# print(f"Parabéns! Você fez {pontos} pontos")


# 7. A Ordem dos Fatores
# nota = 9.5
# if nota >=7:
#     print("Aprovado")
# elif nota >=9:
#     print("Excelente!")

# corrigido:
# nota = 9.5
# if nota >=9:
    # print("Excelente")
# else:
    # print("Aprovado")

# melhorado:
# nota = float(input("Qual a sua nota? "))
# if nota >=9:
#     print("Excelente!")
# elif nota >=6:
#     print("Aprovado")
# else:
#     print("Reprovado")



# 8. O Contador de 1 a 5
# for i in range(5):
#     print(i)


# corrigido: 
# for i in range(0, 6):
#     print(i)

# melhorado:
# limite = int(input("Até que número você quer contar? "))

# for i in range(1, limite + 1):
#     print(f"Número {i}")




# 9. O Loop Eterno
# tentativas = 1
# while tentativas <=3:
#     print("Tentando conectar...")

# corrigido:
# tentativas = 1
# while tentativas <= 3:
#     print(f"Tentativa {tentativas}: Tentando conectar...")
#     tentativas += 1 

# # melhorado:
# tentativas = 1
# sucesso = False

# while tentativas <= 3:
#     print(f"Tentativa {tentativas} de 3...")
#     tentativas += 1

# print("Falha ao conectar: Limite de tentativas excedido.")





# 10. A Senha Teimosa
# senha =""
# while senha == "python123":
#     senha = input("Digite a senha secreta: ")
# print("Acesso concedido")

# corrigido:
# senha = ""
# while senha != "python123":
#     senha = input("Digite a senha secreta: ")

# print("Acesso concedido!")
# senha = ""

# while senha != "python123":
#     senha = input("Digite a senha: ")
#     if senha != "python123":
#         print("Senha errada! Tente de novo.")

# print("Acesso concedido!")