# 2. o laço while (repetições interminadas)
# # use o while quando voce nao sabe quando vai parar, ele depende de uma condição(como um sensor de segurança ou um botao de emergencia)
# exemplo: monitor de temperatura  (loop infinito controlado)
# repete enquanto a temperatura estiver segura 
# inicio

# import time 
# temperatura = 30
# while temperatura < 80:
#     print(f"températura atual: {temperatura}°C. Sistema operando...")
#     time.sleep(1)
#     temperatura += 3 #simulando o aquecimento da maquina 
# print("ALERTA! Temperatura atingiu o limite. desligando motor...")

#lista de temperaturas lidas pelo sensor por minuto

# exemplo 2: monitoramento de teperatura com lista de leituras
# listas de temperatura lidas pelo sensor por minuto

# leituras = [70, 75, 82, 98,
#              110, 85, 80]

# for temp in leituras:
#     if temp > 100:
#         print(f"CRITICO: {temp}°C detectado! Acionando parada de emergencia.")
#         break #o loop para aqui e nao le os proximos valores (85 e 80)
#     print(f"A temperatura esta em {temp}°C. operação normal.")

# print("Sistema desligado. Aguardando manutenção")

 #exemplo 3

# materiais = ["metal", "metal", "plastico", "metal", "vidro", "metal"]
# for peca in materiais:
#     if peca != "metal":
#         print(f"Aviso: peça de {peca} detectada. Desviando para descarte...")
#         continue #pule o restante do código abaixo e vai para a proxima linha
#     #este codigo so roda se a peça for de metal
#     print(f"processando peça de {peca}. furando e polindo...")

# print("Fim do lote de produção")

# exercicio 1:
# tente criar um codigo de 1 a 10, mas use o continue para nao imprimir o 5 (simulando uma falha de sensor especifica no numero 5)

# for numero in range (1, 11):
#     if numero == 5:
#         print(f"Alerta: falha no sensor n° {numero} detectada")
#         continue
#     print("verificando sensores... OK")
        

# exemplo 3:
# simule um semaforo com parada para cada cor. determine o tempo que deseja para que quando mudar tal cor ele represente uma pausa para cada cor. Use o continue para pular a cor amarela (simulando um semaforo com defeito que nao acende a luz amarela)
# import time

# cores = ["verde", "amarelo", "vermelho"]
# for cor in cores:
#     if cor == "amarelo":
#         print(f"semaforo com defeito, pulando para a proxima cor {cor}")
#         continue 
#     print(f"semaforo da cor {cor} parando por 5 segundos")
#     time.sleep(5)


# #exercicio 3 
# total_consumo = 0
# for maquinas in range (1, 6):
#     consumo = float(input(f"Qual o consumo da maquina {maquinas}"))
#     total_consumo += consumo 
# print(f"O consumo total da fabrica é de {total_consumo} KWh.")


