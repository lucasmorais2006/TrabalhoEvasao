import tkinter as tk
from tkinter import font
import Database.DBService

checkboxes = {}

def salvar_presenca():
    for nome, var in checkboxes.items():
        if var.get() == 0:
            Database.DBService.marcar_falta(nome)
        else:
            Database.DBService.marcar_presenca(nome)
        Database.DBService.calcular_porcentagem(nome)
        Database.DBService.verificar_porcentagem(nome)
        var.set(0)
    chamada.quit()

def remover_aluno_e_atualizar(nome_do_aluno):
    Database.DBService.remover_aluno(nome_do_aluno)
    atualizar_lista_alunos()

def atualizar_lista_alunos(ordenado=False):
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Button(
        frame, text="➕ Adicionar Aluno", font=btn_font, bg="#4CAF50", fg="white",
        activebackground="#45A049", bd=0, padx=10, pady=5, command=abrir_tela_adicionar
    ).pack(anchor='w', pady=(0, 15))

    #button para ordenar por presença
    tk.Button(
        frame, text="🔽 Ordenar por Presença", font=btn_font, bg="#9C27B0", fg="white",
        activebackground="#7B1FA2", bd=0, padx=10, pady=5,
        command=lambda: atualizar_lista_alunos(ordenado=True)
    ).pack(anchor='w', pady=(0, 15))

    tk.Label(frame, text="✅ Marque os alunos presentes:", font=title_font, bg="#f0f0f0").pack(anchor='w', pady=(0, 15))

    #puxar dados dos alunos com a porcentagem
    alunos = Database.DBService.listar_por_presenca()

    if ordenado:
        alunos = sorted(alunos, key=lambda aluno: aluno[3], reverse=True)#ordem

    for nome, telefone, presenca, porcentagem in alunos:
        var = tk.IntVar()
        linha_frame = tk.Frame(frame, bg="#ffffff", padx=10, pady=5, highlightbackground="#ddd", highlightthickness=1)
        linha_frame.pack(anchor='w', pady=5, fill='x')

        texto_cb = f"{nome} - {porcentagem:.1f}%"
        cb = tk.Checkbutton(linha_frame, text=texto_cb, variable=var, font=body_font, bg="#ffffff")
        cb.pack(side='left')

        tk.Button(
            linha_frame, text="Remover", font=small_font, bg="#e74c3c", fg="white",
            activebackground="#c0392b", bd=0, padx=10, pady=3,
            command=lambda n=nome: remover_aluno_e_atualizar(n)
        ).pack(side='right')

        checkboxes[nome] = var

    tk.Button(
        frame, text="💾 Salvar Presença", font=btn_font, bg="#2196F3", fg="white",
        activebackground="#1976D2", bd=0, padx=10, pady=8, command=salvar_presenca
    ).pack(anchor='w', pady=30)


def abrir_tela_adicionar():
    adicionar_tela = tk.Toplevel(chamada)#tk.Toplevel cria uma nova janela que não é a principal.
    adicionar_tela.title("Adicionar Aluno")
    adicionar_tela.geometry("400x250")
    adicionar_tela.configure(bg='#ffffff')

    tk.Label(adicionar_tela, text="Nome do Aluno:", font=body_font, bg='#ffffff').pack(anchor='w', padx=20, pady=(20, 5))
    nome_entry = tk.Entry(adicionar_tela, font=body_font)
    nome_entry.pack(anchor='w', padx=20, fill='x')

    tk.Label(adicionar_tela, text="Telefone do Responsável:", font=body_font, bg='#ffffff').pack(anchor='w', padx=20, pady=(15, 5))
    telefone_entry = tk.Entry(adicionar_tela, font=body_font)
    telefone_entry.pack(anchor='w', padx=20, fill='x')

    def adicionar_aluno_callback():
        Database.DBService.adicionar_aluno(nome_entry.get(), telefone_entry.get())
        atualizar_lista_alunos()
        adicionar_tela.destroy()

    tk.Button(
        adicionar_tela, text="Adicionar", font=btn_font, bg="#4CAF50", fg="white",
        activebackground="#45A049", bd=0, padx=10, pady=8, command=adicionar_aluno_callback
    ).pack(pady=25)

# Janela principal
chamada = tk.Tk()
chamada.title("Chamada Escolar")
chamada.state('zoomed') #tela maximizada
chamada.geometry("800x600")
chamada.configure(bg='#f0f0f0')

# Fontes customizadas
title_font = font.Font(family="Arial", size=16, weight="bold")
body_font = font.Font(family="Arial", size=12)
btn_font = font.Font(family="Arial", size=12, weight="bold")
small_font = font.Font(family="Arial", size=10)

# Frame principal
container = tk.Frame(chamada, bg="#f0f0f0")
container.pack(fill='both', expand=True)

canvas = tk.Canvas(container, bg="#f0f0f0")
scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

scrollable_frame = tk.Frame(canvas, bg="#f0f0f0")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)


frame = tk.Frame(scrollable_frame, padx=30, pady=30, bg="#f0f0f0")
frame.pack(anchor='w', fill='both', expand=True)

atualizar_lista_alunos()
chamada.mainloop()
