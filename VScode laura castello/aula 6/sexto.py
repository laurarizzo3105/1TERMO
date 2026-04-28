# Clean code - aula 6 
# para que usar?
# como usar?
# print ("clean code - aula6")
# aula = 6
# print(f"estamos na aula {aula} de clean code")

# texto = "  Python é muito legal!  "
# print(texto.strip().upper()) 
# print(texto.strip().lower()) 
# print(texto.strip().capitalize()) 
# print(texto.strip().title()) 
# print(texto.strip().replace(" ", "_")) 
# print(texto.strip().split()) 

# # # Escrevendo
# with open("notas.txt", "w") as arquivo:
#     arquivo.write("Estudar Python hoje!")
#     arquivo.write("\nLer sobre clean code")



# # lendo
# with open("notas.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)


# exercicio 1
# crie um programa que peça um usuario para inserir uma frase e, em seguida, exiba a frase com  as seguintes transformações: remova os espaçoes extras no inicio e no final da frase

# frase = input("  Qual a frase desejada?  ")
# print(frase.strip().upper())           

# exemplo 1 
# crie um programa que leia o conteudo de um arquivo de texto e conte quantas vezes a palavra pyhon aparece no arquivo. exiba o resultado para o usuario

# print("Contagem de palavras em arquivo")
# with open("notas.txt", "r") as arquivo:
#     conteudo = arquivo.read() 
#     contagem = conteudo.count("Python")
#     print(f"A contagem de palavras {contagem} é de...")


# execução de comandos do sistema
import os #importa o modulo os para interagir com o sistema operacional

# #onde estou?
# print(os.getcwd())
# #listar arquivos na pasta 
# print(os.listdir())
# print(os.listdir(".."))
# print(os.listdir("..\\.."))
# print(os.listdir("C:\\"))
# print(os.listdir("C:\\Users"))
# print(os.listdir("C:\\Users\\Public"))


# outros comandos uteis:

# criar pasta 
# os.mkdir("nova_pasta")

# # renomear pasta 
# os.rename("nova_pasta", "pasta_renomeada")

# # excluir pasta
# os.rmdir("pasta_renomeada")

# exercicio 2
# crie um script que mostre o caminho da pasta atual 

# print(os.getcwd())

# # exercicio 3
# # liste os arquivos da pasta atual

# print(os.listdir())

# # exercicio 4 
# # crie uma pasta chamada projetos e depois renomeie para meus projetos. por fim, exclua a pasta


# os.mkdir("projetos")
# os.rename("projetos", "meus_projetos")
# os.rmdir("meus_projetos")


# exericio 5
# crie um arquivo chamado "log.txt" e escreva a mensagem "log de atividades". depois, leia o conteudo do arquivo e exiba na tela

# with open("log.txt", "w") as arquivo:
#    arquivo.write("log de atividades")

# with open("log.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)  


# exemplo de dicionario 
# crie um dicionario copm informaçoes sobre uma pessoa e acesso um valor usando uma chave

# pessoa = {
#     "nome": "alice",
#     "idade": 30,
#     "cidade" : "São paulo",
#     "profissão": "Engenharia"
 
# }

# pessoa2 =  {
#     "nome": "Bruno",
#     "idade": 25,
#     "cidade": "SP",
#     "profissão": "desingner"

# }

# print(pessoa["cidade"])
# print(pessoa2["nome"], pessoa["idade"])

# exemplo 2: desligar o pc(comando para Windows)

with open("desliga.bat", "w") as desligar:
    desligar.write("shutdown -s -t 3600 -c \"Desligamento programado para daqui a 1 hora. Salve seu trabalho!\"")
    # -s comando para desligar
    # -t tempo definir
    # -a cancelar desligamento
    # with open("desliga.bat", "r") as desligar

