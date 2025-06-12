import tkinter as tk
import Database.DBService 

# Lista de nomes exemplo
nomes_exemplo = [
    "Ana Paula", "Bruno Henrique", "Carla Mendes", "Daniel Souza",
    "Eduarda Lima", "Felipe Rocha", "Gabriela Nunes", "Henrique Silva",
    "Isabela Castro", "João Pedro"
]


# Dicionários para armazenar presença e checkbox
checkboxes = {}

 #Função para salvar presença (simula mais uma aula)
def salvar_presenca():
    for nome, var in checkboxes.items():
       if var.get() == 0:
        Database.DBService.marcar_falta(nome)
       else:
          Database.DBService.marcar_presenca(nome) 
       Database.DBService.calcular_porcentagem(nome)
       Database.DBService.verificar_porcentagem(nome)
       var.set(0)
       chamada.quit()  # Limpa o checkbox para próxima aula


# Interface Tkinter
chamada = tk.Tk()
chamada.title("Chamada Escolar (Protótipo)")
chamada.geometry("800x600")

frame = tk.Frame(chamada, padx=30, pady=30)
frame.pack(anchor='w')

tk.Label(frame, text="Marque os alunos presentes:", font=('Arial', 16)).pack(anchor='w', pady=(0, 15))

for nome in Database.DBService.nome_alunos():
    var = tk.IntVar()
    cb = tk.Checkbutton(frame, text=nome, variable=var, font=('Arial', 12))
    cb.pack(anchor='w', pady=2)
    checkboxes[nome] = var

tk.Button(frame, text="Salvar Presença", font=('Arial', 12), command=salvar_presenca).pack(anchor='w', pady=20)

chamada.mainloop()
