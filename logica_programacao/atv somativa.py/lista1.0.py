# 1. Perfil de Gamer: Peça o nick (nome) do jogador e o nível atual. Exiba: "O
# jogador [nick] está no nível [nível] e pronto para a partida!"

# nick = input("Qual o seu nick? ")
# nivel = int(input("Qual o nivel do jogador? "))

# print("O jogador", nick , "está no nível", nivel , "e pronto para a partida")


# 2. Calculadora de Mesada: Peça o valor que o aluno ganha por semana e
# multiplique por 4 para mostrar quanto ele terá no final do mês.

# valor = float(input("Quanto o aluno recebe por semana? "))
# total = valor * 4
# print("O aluno terá, no final do mês, o valor de", total)


# 3. Conversor de Internet: Peça um valor em Gigabytes (GB) e converta para
# Megabytes (MB) (multiplique por 1024).

# valorgb = float(input("Diga um valor em GB: "))
# sla = valorgb * 1024 
# print("O valor convertido para Mb é de:", sla)

# 4. Média de Notas: Peça as notas de Matemática e Português. Calcule e mostre a
# média final.

# portugues = float(input("Qual a sua nota de português? "))
# matematica = float(input("Qual a sua nota de matemática? "))
# media = portugues + matematica
# total = media /2
# print("Sua média final é de:", total)

# 5. Seguidores: Peça a quantidade de seguidores atuais e quantos novos seguidores
# o aluno ganhou hoje. Exiba o total atualizado.

# seguidores = int(input("Quantos seguidores você tinha? "))
# ganho = int(input("Quantos seguidores você ganhou hoje? "))
# seguitotal = seguidores + ganho 
# print("Você agora tem total de", seguitotal, "seguidores")

# 6. Idade em Dias: Peça a idade do aluno e calcule aproximadamente quantos dias
# ele já viveu (idade * 365).

# idade = int(input("Qual sua idade? "))
# dias = idade * 365
# print("Você já viveu o total de", dias, "dias")

# 7. Consumo de Lanche: Peça o preço do salgado e o preço do suco. Exiba o valor
# total da conta.

# salgado = float(input("Qual o preço do salgado? "))
# suco = float(input("Qual o preço do suco? "))
# valorfinal = salgado + suco
# print("Sua conta deu", valorfinal, "reais")

# 8. Ano de Nascimento: Peça o ano atual e a idade do aluno. Calcule e exiba o ano
# em que ele nasceu.

# anoatual = int(input("Qual o ano atual? "))
# idade = int(input("Qual sua idade? "))
# anodenas = anoatual - idade 
# print("Você nasceu no ano de", anodenas)

# 9. Filtro de Idade (TikTok): Peça a idade do usuário. Se for menor que 13, exiba
# "Acesso restrito". Se tiver entre 13 e 17, "Acesso moderado". Se for 18 ou
# mais, "Acesso liberado".

# idade = int(input("Qual a sua idade? "))
# if idade < 13:
#     print("Acesso restrito")
# elif idade < 18:
#     print("Acesso moderado")
# else:
#     print("Acesso liberado")
    
# 10.Bateria do Celular: Crie um while que começa com a bateria em 100. A cada
# repetição, subtraia 10 e mostre: "Bateria em [valor]%". O loop para quando
# chegar em 10 e exibe: "Por favor, conecte o carregador!".

# bateria = 100
# while bateria > 10:
#     print(f"bateria esta em {bateria} %")
#     bateria -= 10  
# print(f"Bateria em {bateria}%")
# print("Por favor, conecte o celular")

# 11. Contagem de Curtidas: Use um for para simular a contagem de curtidas em uma
# foto. Peça ao usuário o limite de curtidas (ex: 5). O programa deve contar de 1 até
# esse número, printando: "Curtida no [i] recebida!".

# limite = int(input("Qual o limite de curtidas desejado? "))
# for i in range(1, limite + 1):
    # print(f"curtida N° {i} recebida")

# 12.Carrinho de Compras Online: Use um while para pedir nomes de produtos que o
# aluno quer comprar. O loop só para quando ele digitar "sair". No final, mostre
# quantas vezes ele adiciona itens ao carrinho (use um contador).

# contador = 0
# produto = ""

# print("carrinho de compras online")
# print("digite 'sair' para finalizar a compra")

# while produto.lower() != "sair":
#     produto = input("Digite o nome do produto  ")
#     contador += 1
# if produto.lower() != "sair":
#     print(f"produto '(produto)' adicionado ao carrinho")

# print(f"Compra finalizada, você adicionou {contador} itens ao seu carrinho")    