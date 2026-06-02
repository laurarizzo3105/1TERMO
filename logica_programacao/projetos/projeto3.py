# 1. Utilizar tomada de decisão para elaboração do algoritmo
# 2. Utilizar estruturas condicionais para executar instruções com base em uma
# condição
# 3. Criar estruturas de repetição para executar um conjunto de instruções várias
# vezes
# 4. Aplicar operadores lógicos para avaliar e combinar condições booleanas
# 5. Utilizar lógica de programação para a resolução de problemas

# Projeto de Revisão: Sistema de Empréstimo "Biblioteca Digital"
# Contexto: Você foi contratado para desenvolver o módulo de validação de
# empréstimos de livros de uma biblioteca comunitária. O sistema precisa coletar os dados
# do usuário, do livro e decidir se o empréstimo será aprovado, negado ou se haverá
# cobrança de taxa de segurança.
# Regras de Negócio (O que o sistema deve fazer):
# 1. Classificação do Usuário: A biblioteca atende [1] Alunos e [2] Comunidade
# Geral.
# 2. Limite de Dias: * Alunos podem ficar com o livro por até 14 dias de graça.
# ○ A Comunidade Geral pode ficar por até 7 dias de graça.
# 3. Taxa de Renovação: Se o usuário quiser ficar mais tempo do que o limite do seu
# perfil, será cobrada uma taxa fixa de R$ 5,00 por dia adicional.
# 4. Restrição de Categoria: Livros da categoria "Raros" não podem ser emprestados
# para a Comunidade Geral, apenas para Alunos.

import tkinter as tk
from tkinter import messagebox

def validar_emprestimo():
    nome = nome_usuario.get()
    tipo = tipo_usuario.get()
    categoria = categoria_livro.get()
    dias = int(dias_emprestimo.get())

    if categoria == "Raros" and tipo == "Comunidade":
        messagebox.showerror("Negado", "Livros raros são apenas para alunos.")

    elif tipo == "Aluno":
        if dias <= 14:
            messagebox.showinfo("Aprovado", f"{nome}, empréstimo aprovado sem taxa.")
        else:
            taxa = (dias - 14) * 5
            messagebox.showinfo("Aprovado", f"Taxa: R$ {taxa}")

    elif tipo == "Comunidade":
        if dias <= 7:
            messagebox.showinfo("Aprovado", f"{nome}, empréstimo aprovado sem taxa.")
        else:
            taxa = (dias - 7) * 5
            messagebox.showinfo("Aprovado", f"Taxa: R$ {taxa}")

# Janela
janela = tk.Tk()
janela.title("Biblioteca Digital")
janela.geometry("300x250")

tk.Label(janela, text="Nome").grid(row=0, column=0)
nome_usuario = tk.Entry(janela)
nome_usuario.grid(row=0, column=1)

tk.Label(janela, text="Aluno ou Comunidade").grid(row=1, column=0)
tipo_usuario = tk.Entry(janela)
tipo_usuario.grid(row=1, column=1)

tk.Label(janela, text="Comum ou Raros").grid(row=2, column=0)
categoria_livro = tk.Entry(janela)
categoria_livro.grid(row=2, column=1)

tk.Label(janela, text="Dias").grid(row=3, column=0)
dias_emprestimo = tk.Entry(janela)
dias_emprestimo.grid(row=3, column=1)

tk.Button(janela, text="Validar", command=validar_emprestimo).grid(row=4, column=0)

janela.mainloop()
