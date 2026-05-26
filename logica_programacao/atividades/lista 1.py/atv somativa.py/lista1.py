# Atividade 1: Mensagem de Boas-Vindas
# Crie um script que use a função print() para exibir a mensagem "Bem-vindo ao mundo da
# programação em Python!".

print("Bem-vindo ao mundo da programação em Python!")

# Atividade 2: Informações Pessoais
# Escreva um programa que imprima seu nome completo em uma linha e sua idade em outra linha.
# Exemplo de saída:
# Fulano de Tal
# 30

print ("Bem-vindo")
nome = input("Qual o seu nome completo?" )
idade = int(input("Qual a sua idade?" ))

print("Seu nome é:", nome)
print("Sua idade é:" , idade)

# Atividade 3: Calculadora de Soma e Subtração
# Crie um script que exiba o resultado da soma de 135 com 246 e o resultado da subtração de 512
# por 128. Cada resultado deve ser exibido em uma linha separada.
# ● Dica: Use o print() diretamente com os operadores (print(135 + 246)).
# ● Obs: Realize também a mesma situação com variáveis

print (135 + 246)
print(512 - 128)
#com váriaveis

print("135 + 246")
print("512 - 128")

print("Primeira conta com soma")
valor1 = int(input("Digite o primeiro valor:"))
valor2 = int(input("Digite o segundo valor:"))
resultado = valor1 + valor2
print ("A sua soma deu:" , resultado)

print("Segunta conta com subtração")
valor3 = int(input("Digite o primeiro valor"))
valor4 = int(input("Digite o segundo valor"))
resultado2 = valor3 - valor4
print("A subtração deu:" , resultado2)
   
# Atividade 4: Multiplicação e Divisão
# Escreva um programa que mostre o resultado da multiplicação de 15 por 8 e o resultado da
# divisão de 78 por 3.

print(15*8)
print(78/3)

# Atividade 5: Potenciação
# Calcule e exiba o resultado de "5 elevado à 3a potência" (53).
# ● Dica: O operador de potenciação em Python é **.

print(5**3)

# Atividade 6: Concatenando Palavras
# Crie um script que declare o seu primeiro nome em uma string e seu sobrenome em outra. Use
# o operador + para concatenar (juntar) as duas strings e exibir seu nome completo.
# ● Exemplo: print("Maria" + " " + "Silva")

nome = input("seu primeiro nome ")
sobrenome = input("seu sobrenome ")
print (nome + sobrenome)

# Atividade 7: Cálculo de Eficiência (OEE)
# ● Peça a quantidade de peças produzidas e a quantidade de peças defeituosas. Calcule
# e exiba a taxa de aproveitamento (peças boas / total).

peças1 = int(input("qual a quantidade de peças produzidas?"))
peças2 = int(input("qual a quantidade de peças defeituosas"))
peçasboas = peças1 - peças2 
print ("a taxa de aproveitamento é:" , peçasboas/peças1)

# Atividade 8: Descrição com Cálculos
# Crie um script que exiba a seguinte frase, substituindo os cálculos pelos seus resultados:
# "Eu tenho 25 anos e, em 10 anos, terei 35 anos."
# ● Dica: Use a vírgula dentro do print() para combinar strings e cálculos.
# ● Ex: print("Texto", 25 + 10).

idade = int(input("Qual sua idade? "))
print ("Eu tenho", idade, "anos e em 10 anos terei", idade + 10, "anos")


# Atividade 9: Orçamento de Viagem (Cálculo com float)
# Imagine que você está planejando uma viagem. O custo do hotel é de R$ 250.50 por noite e
# o custo da passagem é R$ 412.00. Calcule e exiba o custo total para uma viagem por noites.
# ● Ex: Fórmula: (custo_hotel * 3) + custo_passagem

custoH = float(input("Qual o custo do hotel por noite? "))
custoP = float(input("qual o custo da passagem?"))
dias = int(input("Quantos dias de viagem?"))

print ("O preço da sua viagem será de:" , (custoH * dias) + custoP)


# Atividade 10: Desafio - Mini Relatório
# Crie um script que imprima um pequeno relatório. Use print() várias vezes para formatar a
# saída de forma organizada.
# ● Exemplo de saída:

# ==========================
# Relatório de Vendas
# ==========================
# Produto: Notebook Gamer
# Quantidade vendida: 15
# Preço unitário: R$ 5499.50
# Total de vendas: R$ 82492.50
# ==========================

print("Relatório de vendas na semana por produto\n \n")
produto = input("Qual o produto? ")
valor = int (input("Qual o valor unitário? "))
quantidade = int(input("Quantos foram vendidos? "))

print ("Relatório de vendas do produto:" , produto)
print ("Quantidade vendida:" , quantidade)
print ("Preço por unidade:" , valor)
print ("Valor total de vendas:" , valor * quantidade)





