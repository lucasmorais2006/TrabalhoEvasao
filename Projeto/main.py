import tkinter as tk

# Lista de nomes exemplo
nomes_exemplo = [
    "Ana Paula", "Bruno Henrique", "Carla Mendes", "Daniel Souza",
    "Eduarda Lima", "Felipe Rocha", "Gabriela Nunes", "Henrique Silva",
    "Isabela Castro", "João Pedro"
]


# Dicionários para armazenar presença e checkbox
checkboxes = {}
historico_presenca = {nome: {'presentes': 0, 'total': 0} for nome in nomes_exemplo}

 #Função para salvar presença (simula mais uma aula)
def salvar_presenca():
    for nome, var in checkboxes.items():
       historico_presenca[nome]['total'] += 1
       if var.get():
           historico_presenca[nome]['presentes'] += 1
    var.set(0)  # Limpa o checkbox para próxima aula
#    calcular_presenca()

# Função para calcular e exibir presença
#def calcular_presenca():
#    print("\n--- Frequência dos alunos ---")
#    for nome, dados in historico_presenca.items():
#        total = dados['total']
#        presentes = dados['presentes']
#        if total > 0:
#            porcentagem = (presentes / total) * 100
#            print(f"{nome}: {porcentagem:.1f}% ({presentes}/{total})")
#        else:
#            print(f"{nome}: Nenhuma aula registrada.")
#    print()

# Interface Tkinter
root = tk.Tk()
root.title("Chamada Escolar (Protótipo)")
root.geometry("800x600")

frame = tk.Frame(root, padx=30, pady=30)
frame.pack(anchor='w')

tk.Label(frame, text="Marque os alunos presentes:", font=('Arial', 16)).pack(anchor='w', pady=(0, 15))

for nome in nomes_exemplo:
    var = tk.IntVar()
    cb = tk.Checkbutton(frame, text=nome, variable=var, font=('Arial', 12))
    cb.pack(anchor='w', pady=2)
    checkboxes[nome] = var

tk.Button(frame, text="Salvar Presença", font=('Arial', 12), command=salvar_presenca).pack(anchor='w', pady=20)

root.mainloop()
