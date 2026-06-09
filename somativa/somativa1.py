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
# janela.configure(bg="pink")

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

import tkinter as tk
from tkinter import messagebox

def janela_bemvindo():
    bar = pressao_usuario.get()
    
    if bar == "": 
        messagebox.showwarning("Aviso", "Digite a quantidade de bar")
    else:
        try:
            
            pressao_total = float(bar)
            valor_bar = 14.5
            resultado_final = pressao_total * valor_bar
            
            messagebox.showinfo("Bem-Vindo", f"quantidade de bar convertida é igual a: {resultado_final}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, digite a quantidade de bar")

janela = tk.Tk()
janela.title("Exemplo 2")
janela.geometry("300x300")
janela.configure(bg="pink") 

pressao_usuario = tk.Label(janela, text="Dogote a quantidade de bar: ")
pressao_usuario.grid(row=0, column=0, pady=10, padx=10)

peca_usuario = tk.Entry(janela, font=("Arial", 12))
peca_usuario.grid(row=1, column=0, pady=10, padx=10)

btn_mensagem = tk.Button(janela, text="Calcular", command=janela_bemvindo)
btn_mensagem.grid(row=2, column=0, pady=10, padx=10)

janela.mainloop()