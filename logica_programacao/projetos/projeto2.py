# Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar.


# print("Bem-vindo!")

# andar_atual = 0

# while True:
#     print(f"\nElevador está no andar {andar_atual}")

#     try:
#         destino = int(input("Escolha o andar de destino (0 a 10): "))

#         if destino < 0 or destino > 10:
#             print("Andar inválido!")
#             continue

#         if destino > andar_atual:
#             print("Elevador subindo...")
#             for andar in range(andar_atual + 1, destino + 1):
#                 print(f"Andar {andar}")

#         elif destino < andar_atual:
#             print("Elevador descendo...")
#             for andar in range(andar_atual - 1, destino - 1, -1):
#                 print(f"Andar {andar}")

#         else:
#             print("O elevador já está nesse andar.")

#         andar_atual = destino

#         print(f"Elevador parou no andar {andar_atual}")

#     except ValueError:
#         print("Digite apenas números!")

   
#     resposta = input("\nDeseja escolher outro andar? (s/n): ").lower()

#     if resposta != "s":
#         print("Encerrando sistema...")
#         break