import tkinter as tk
from tkinter import ttk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("400x500")
        self.root.resizable(0, 0)
        self.root.configure(bg="#000000")
        
        self.total_expressao = ""
        self.atual_expressao = ""

        self.display_frame = self.criar_frame_display()
        self.label_total, self.label_atual = self.criar_labels_display()

        self.botao_frame = self.criar_frame_botoes()

        self.digitos = {
            '7': (1, 0), '8': (1, 1), '9': (1, 2),
            '4': (2, 0), '5': (2, 1), '6': (2, 2),
            '1': (3, 0), '2': (3, 1), '3': (3, 2),
            '0': (4, 0)
        }
        self.operadores = {
            '/': "\u00F7", '*': "\u00D7", '-': "\u2212", '+': "\u002B"
        }
        
        self.criar_botoes_digitos()
        self.criar_botoes_operadores()
        self.criar_botoes_especiais()
        self.criar_botao_igual()
    
    def criar_frame_display(self):
        frame = tk.Frame(self.root, height=100, bg="#000000")
        frame.pack(expand=False, fill="both")
        return frame
    
    def criar_labels_display(self):
        label_total = tk.Label(self.display_frame, text=self.total_expressao, anchor=tk.E, bg="#000000", fg="#FFFFFF", padx=24, font=("Arial", 16))
        label_total.pack(expand=True, fill="both")

        label_atual = tk.Label(self.display_frame, text=self.atual_expressao, anchor=tk.E, bg="#000000", fg="#FFFFFF", padx=24, font=("Arial", 40, "bold"))
        label_atual.pack(expand=True, fill="both")

        return label_total, label_atual

    def atualizar_display(self):
        self.label_atual.config(text=self.atual_expressao)
        self.label_total.config(text=self.total_expressao)

    def criar_frame_botoes(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        for i in range(5):
            frame.grid_rowconfigure(i, weight=1)
            frame.grid_columnconfigure(i, weight=1)
        return frame
    
    def adicionar_valor(self, valor):
        self.atual_expressao += str(valor)
        self.atualizar_display()

    def criar_botao_estilizado(self, text, row, column, command, bg_color, fg_color):
        button = tk.Button(self.botao_frame, text=text, bg=bg_color, fg=fg_color, font=("Arial", 24, "bold"),
                           borderwidth=0, command=command)
        button.grid(row=row, column=column, sticky=tk.NSEW, padx=5, pady=5)
        button.configure(width=1, height=1)

    def criar_botoes_digitos(self):
        for digito, grid_value in self.digitos.items():
            self.criar_botao_estilizado(digito, grid_value[0], grid_value[1], 
                                        lambda x=digito: self.adicionar_valor(x), "#505050", "#FFFFFF")

    def criar_botoes_operadores(self):
        i = 0
        for operador, simbolo in self.operadores.items():
            self.criar_botao_estilizado(simbolo, i, 3, 
                                        lambda x=operador: self.adicionar_operador(x), "#FF9500", "#FFFFFF")
            i += 1
    
    def criar_botoes_especiais(self):
        self.criar_botao_estilizado("C", 0, 0, self.limpar, "#A5A5A5", "#000000")
        self.criar_botao_estilizado("+/-", 0, 1, self.mudar_sinal, "#A5A5A5", "#000000")
        self.criar_botao_estilizado("%", 0, 2, self.porcentagem, "#A5A5A5", "#000000")

    def criar_botao_igual(self):
        self.criar_botao_estilizado("=", 4, 3, self.calcular, "#FF9500", "#FFFFFF")
    
    def adicionar_operador(self, operador):
        self.total_expressao += self.atual_expressao + operador
        self.atual_expressao = ""
        self.atualizar_display()
    
    def limpar(self):
        self.atual_expressao = ""
        self.total_expressao = ""
        self.atualizar_display()
    
    def mudar_sinal(self):
        if self.atual_expressao:
            self.atual_expressao = str(-1 * float(self.atual_expressao))
            self.atualizar_display()
    
    def porcentagem(self):
        if self.atual_expressao:
            self.atual_expressao = str(float(self.atual_expressao) / 100)
            self.atualizar_display()
    
    def calcular(self):
        self.total_expressao += self.atual_expressao
        try:
            self.atual_expressao = str(eval(self.total_expressao))
            self.total_expressao = ""
        except Exception as e:
            self.atual_expressao = "Erro"
        self.atualizar_display()
        self.atual_expressao = ""

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculadora(root)
    root.mainloop()
