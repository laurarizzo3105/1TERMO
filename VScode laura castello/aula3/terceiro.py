#Exercícios da aula 3
# 1. O laço 'for' (repetições determinadas)
# Use o 'for' quando vocêsabe xatamente quantas vezes algo deve acontecer (como ler sensores ou processar uma lista de peças)
# Exemplo: Relatório de produção diária
# imagine que você tem uma meta de produzir 5 lotes e quer nomear cada um: 

# Exemplo 1:


# for lote in range (1, 6):
#     print(f"processando lote número {lote} ...")
#     print("Quantidade verificada. [OK]")
#     print("produção do dia finalizada")


#exenplo 2:
 
# for b in range(10):
#     print(f"quantidade total {b} foi...")

#exemplo 3:
#imagine o seguinte cenário, iremos produzir 20 discos de vinil.

# for discos in range(1, 21):
#     print(f"Quantidade produzida {discos} ")
#     print("Disco verificado. [OK]")

#exemplo 4:

pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo"]
itempecas = ["Cilindicas", "Eixo cônico", "Radiais", "Madeira", "Bola", "Cabeça-chata", "Chave metalica verde"]
for item in pecas:
    print(f"Item em estoque: {item} e {itempecas}")
    for item2 in itempecas:
        print(f"item de peças em estoque: {itempecas}")


# Exemplo 5:
# imagine a seguinte situação, gostaria de ter um menu onde pudesse perguntar qual opção voce deseja e a partir da seleção ele listar os produtos

