import tkinter as tk
import Database.DBService 



# Dicionário para armazenar presença com checkbox
checkboxes = {}

 #Função para salvar presença (simula mais uma aula)
def salvar_presenca():
    for nome, var in checkboxes.items():
       if var.get() == 0: #Confere se o aluno faltou, se for igual a zero é falta(checkbox vazia)
        Database.DBService.marcar_falta(nome)
       else:
          Database.DBService.marcar_presenca(nome) 
       Database.DBService.calcular_porcentagem(nome)
       Database.DBService.verificar_porcentagem(nome)
       var.set(0) #define a variável (checkbox) como zero para próxima aula
       chamada.quit()  # Limpa o checkbox para próxima aula


# Função para atualizar a lista de alunos na tela principal
def atualizar_lista_alunos():
    for widget in frame.winfo_children():
        widget.destroy()  # Remove todos os widgets existentes no frame

    tk.Button(frame, text="Adicionar aluno", font=('Arial', 12), command=abrir_tela_adicionar).pack(anchor='w', pady=(0, 10))

    tk.Label(frame, text="Marque os alunos presentes:", font=('Arial', 16)).pack(anchor='w', pady=(0, 15))

    for nome in Database.DBService.nome_alunos():
        var = tk.IntVar()
        linha_frame = tk.Frame(frame)  # Linha horizontal
        linha_frame.pack(anchor='w', pady=2, fill='x')
        cb = tk.Checkbutton(linha_frame, text=nome, variable=var, font=('Arial', 12))
        cb.pack(side='left', padx=(0, 15))  # Espaço entre nome e botão
        botao_remover = tk.Button(
        linha_frame,
        text="Remover Aluno",
        font=('Arial', 10),
        fg='white',
        bg='red'
        )
        botao_remover.pack(side='right', pady=2)
        checkboxes[nome] = var


    tk.Button(frame, text="Salvar Presença", font=('Arial', 12), command=salvar_presenca).pack(anchor='w', pady=20)

# Interface Tkinter
chamada = tk.Tk()
chamada.title("Chamada Escolar (Protótipo)")
chamada.geometry("1366x768")
frame = tk.Frame(chamada, padx=30, pady=30)
frame.pack(anchor='w')



def abrir_tela_adicionar():
    adicionar_tela = tk.Toplevel(chamada)
    adicionar_tela.title("Adicionar Aluno")
    adicionar_tela.geometry("400x300")

    tk.Label(adicionar_tela, text="Nome do Aluno:", font=('Arial', 12)).pack(anchor='w', pady=(10, 0))
    nome_entry = tk.Entry(adicionar_tela, font=('Arial', 12))
    nome_entry.pack(anchor='w', padx=20, pady=(0, 10))

    tk.Label(adicionar_tela, text="Telefone do Aluno:", font=('Arial', 12)).pack(anchor='w')
    telefone_entry = tk.Entry(adicionar_tela, font=('Arial', 12))
    telefone_entry.pack(anchor='w', padx=20, pady=(0, 20))
    
    def adicionar_aluno_callback():
        Database.DBService.adicionar_aluno(nome_entry.get(), telefone_entry.get())
        atualizar_lista_alunos()  # Atualiza a lista de alunos na tela principal
        adicionar_tela.destroy()  # Fecha a janela de adicionar aluno

    tk.Button(adicionar_tela, text="Adicionar aluno", font=('Arial', 12), command=adicionar_aluno_callback).pack(anchor='center', pady=(0, 10))

atualizar_lista_alunos()

tk.Button(frame, text="Salvar Presença", font=('Arial', 12), command=salvar_presenca).pack(anchor='w', pady=20)

chamada.mainloop()
