# # 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# # "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

# import tkinter as tk
# from tkinter import messagebox

# def janela_bemvindo():
#     nome = nome_usuario.get()
#     turno = turno_usuario.get()
#     if nome == "" and turno == "":
#         messagebox.showwarning("Aviso", "Digite seu nome e o turno")
#     else:
#         # messagebox.showinfo(f"Operador {nome} registrado no Turno {turno}. Boa jornada!")
#         messagebox.showinfo("Bem-Vindo", f"Operador {nome} registrado no turno {turno}. Boa jornada!")

# janela = tk.Tk()
# janela.title("Exemplo 2")
# janela.geometry("300x300")
# janela.configure(bg="blue")

# lbl_mensagem = tk.Label(janela, text="Digite seu nome ")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)
# lbl_turno = tk.Label(janela, text="Digite o turno A, B ou C")
# lbl_turno.grid(row=1, column=0, pady=10, padx=10)

# nome_usuario = tk.Entry(janela, font=("Arial", 12))
# nome_usuario.grid(row=0, column=1, pady=10, padx=10)
# turno_usuario = tk.Entry(janela, font=("Arial", 12))
# turno_usuario.grid(row=1, column=1, pady=10, padx=10)


# btn_mensagem = tk.Button(janela, text="Mensagem", command=janela_bemvindo)
# btn_mensagem.grid(row=2, column=0, pady=10, padx=10)

# janela.mainloop()







# # 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# # exiba quantas peças serão produzidas em um turno de 8 horas.

# import tkinter as tk
# from tkinter import messagebox

# def janela_bemvindo():
#     peca = peca_usuario.get()
    
#     if peca == "": 
#         messagebox.showwarning("Aviso", "Digite a quantidade de peças")
#     else:
#         try:
#             # Converte o texto digitado para número
#             peca_total = int(peca)
#             turno_horas = 8
#             resultado_final = peca_total * turno_horas
            
#             # Mostra o resultado final
#             messagebox.showinfo("Bem-Vindo", f"A quantidade produzida de peças em 8 horas será de: {resultado_final}")
#         except ValueError:
#             messagebox.showerror("Erro", "Por favor, digite apenas números inteiros")

# janela = tk.Tk()
# janela.title("Exemplo 2")
# janela.geometry("300x300")
# janela.configure(bg="pink") 

# lbl_mensagem = tk.Label(janela, text="Digite o número de peças:")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)

# peca_usuario = tk.Entry(janela, font=("Arial", 12))
# peca_usuario.grid(row=1, column=0, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Calcular", command=janela_bemvindo)
# btn_mensagem.grid(row=2, column=0, pady=10, padx=10)

# janela.mainloop()









# 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.

# import tkinter as tk
# from tkinter import messagebox

# def janela_bemvindo():
#     bar = int(pressao_usuario.get())
    
#     if bar == "": 
#         messagebox.showwarning("Aviso", "Digite a quantidade de bar")
#     else:
#         try:
            
#             pressao_total = float(bar)
#             valor_bar = 14.5
#             resultado_final = pressao_total * valor_bar
            
#             messagebox.showinfo("Bem-Vindo", f"quantidade de bar convertida é igual a: {resultado_final}")
#         except ValueError:
#             messagebox.showerror("Erro", "Por favor, digite a quantidade de bar")

# janela = tk.Tk()
# janela.title("Exemplo 2")
# janela.geometry("300x300")
# janela.configure(bg="green") 

# lbl_pressao_usuario = tk.Label(janela, text="Digite a quantidade de bar: ")
# lbl_pressao_usuario.grid(row=0, column=0, pady=10, padx=10)

# pressao_usuario = tk.Entry(janela, font=("Arial", 12))
# pressao_usuario.grid(row=1, column=0, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Calcular", command=janela_bemvindo)
# btn_mensagem.grid(row=2, column=0, pady=10, padx=10)

# janela.mainloop()







# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.

# import tkinter as tk
# from tkinter import messagebox

# # .get() serve para buscar informação na caixa de texto
# def janela_bemvindo():
#     nota1 = float(um_usuario.get())
#     nota2 = float(dois_usuario.get())
#     nota3 = float(tres_usuario.get())
    


#     if nota1 == "" and nota2 == "" and nota3 == "":
#         messagebox.showwarning("Aviso", "Por favor, digite as notas")
#     else:
#         try:
            
#             valor_notas = nota1 + nota2 + nota3
#             resultado_final = valor_notas / 3
            
#             messagebox.showinfo("Bem-Vindo", f"O resultado das notas é: {resultado_final}")
#         except ValueError:
#             messagebox.showerror("Erro", "Por favor, digite as notas corretamente")    

# # Configurações da Janela
# janela = tk.Tk()
# janela.title("Exemplo 2")
# janela.geometry("300x300")
# janela.configure(bg="pink")

# # Componentes
# # Labels
# lbl_mensagem = tk.Label(janela, text="Digite a primeira nota de 0 a 10")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)
# lbl_idade = tk.Label(janela, text="Digite a segunda nota de 0 a 10")
# lbl_idade.grid(row=1, column=0, pady=10, padx=10)
# lbl_idade = tk.Label(janela, text="Digite a terceira nota de 0 a 10")
# lbl_idade.grid(row=2, column=0, pady=10, padx=10)

# # Entrys
# um_usuario = tk.Entry(janela, font=("Arial", 12))
# um_usuario.grid(row=0, column=1, pady=10, padx=10)
# dois_usuario = tk.Entry(janela, font=("Arial", 12))
# dois_usuario.grid(row=1, column=1, pady=10, padx=10)
# tres_usuario = tk.Entry(janela, font=("Arial", 12))
# tres_usuario.grid(row=2, column=1, pady=10, padx=10)


# btn_mensagem = tk.Button(janela, text="Mensagem", command=janela_bemvindo)
# btn_mensagem.grid(row=3, column=0, pady=10, padx=10)

# # Rodar interface
# janela.mainloop()






# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

# import tkinter as tk
# from tkinter import messagebox

# def janela_bemvindo():
#     temperatura = float(calor_usuario.get())
    
#     if temperatura == "": 
#         messagebox.showwarning("Aviso", "Por favor, informe a temnperatura do motor")
#     elif temperatura < 40:
#         messagebox.showinfo("temperatura", "Baixa carga")
#     elif temperatura <= 70:
#         messagebox.showinfo("temperatura", "Normal")
#     else:
#         messagebox.showinfo("temperatura", "ALERTA! Resfriamento ativado.")    


# janela = tk.Tk()
# janela.title("Exemplo 2")
# janela.geometry("300x300")
# janela.configure(bg="pink") 

# lbl_mensagem = tk.Label(janela, text="Por favor, informe a temperatura do motor")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)

# calor_usuario = tk.Entry(janela, font=("Arial", 12))
# calor_usuario.grid(row=1, column=0, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Calcular", command=janela_bemvindo)
# btn_mensagem.grid(row=2, column=0, pady=10, padx=10)

# janela.mainloop()





# 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".


import tkinter as tk
from tkinter import messagebox

def janela_bemvindo():
    lotes = float(calor_usuario.get())
    
    if lotes == "": 
        messagebox.showwarning("Aviso", "Por favor, insira o codigo do produto")
    elif lotes == ("A"):
        messagebox.showinfo("", "Baixa carga")
    elif lotes == ("E"):
        messagebox.showinfo("temperatura", "Normal")
    else:
        messagebox.showinfo("codigo", "Desconhecido")    


janela = tk.Tk()
janela.title("Exemplo 2")
janela.geometry("300x300")
janela.configure(bg="pink") 

lbl_mensagem = tk.Label(janela, text="Por favor, informe a temperatura do motor")
lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)

calor_usuario = tk.Entry(janela, font=("Arial", 12))
calor_usuario.grid(row=1, column=0, pady=10, padx=10)

btn_mensagem = tk.Button(janela, text="Calcular", command=janela_bemvindo)
btn_mensagem.grid(row=2, column=0, pady=10, padx=10)

janela.mainloop()