import tkinter as tk

def mostrar_estado():
    if var.get():
        rotulo.config(text="Presente")
    else:
        rotulo.config(text="Ausente")

AbaPrincipal = tk.Tk()
AbaPrincipal.title("Controle de presença")
AbaPrincipal.geometry("1280x720")
rotulo = tk.Label(AbaPrincipal, text="Controle de presença").grid(row=0, column=0, padx=1125, pady=20)
check_presenca = tk.BooleanVar()
check = tk.Checkbutton(AbaPrincipal, text="Opção", variable=check_presenca, command=mostrar_estado).grid(padx=1, pady=30)


AbaPrincipal.mainloop()

#for nome_alunos in Alunos