import tkinter as tk
from tkinter import messagebox

perguntas = [
    {
        "pergunta": "1) Qual é a capital da Noruega?",
        "opcoes": ["A) Moscou", "B) Buskerud", "C) Oslo", "D) Okrugs"],
        "resposta": "3"
    },
    {
        "pergunta": "2) Resolva a equação de segundo grau x²−4x+3= 0",
        "opcoes": ["A) 1 e 2", "B) 1 e 3", "C) 2 e 3", "D) 9 e 1"],
        "resposta": "2",
    },
    {
        "pergunta": "3) Qual alternativa está na norma-padrão do português?",
        "opcoes": ["A) Fazem 10 anos que estudo inglês.", "B) Faz dois anos que não viajo para a praia.", "C) Fizeram uma boa prova pro concurso.", "D) Fazem muitos dias que ele não aparece."],
        "resposta": "2",
    },
    {
        "pergunta": "4) Quem foi o segundo presidente do Brasil",
        "opcoes": ["A) Campois Sales", "B) Getúlio Vargas", "C) Prudente de Morais", "D) Floriano Peixoto"],
        "resposta": "4",
    },
    {
        "pergunta": "5)Qual o maior orgão do corpo humano",
        "opcoes": ["A) Pele", "B) Coração", "C) Figado", "D) Esqueleto"],
        "resposta": "1",
    },
    {
        "pergunta": "6) Qual é o único metal que se encontra em estado líquido em tempoeratura ambiente.",
        "opcoes": ["A) Gálio", "B) Mercúrio", "C) Saturno", "D) Césio"],
        "resposta": "2",
    },
    {
        "pergunta": "7) O que determina a identidade química de um átomo",
        "opcoes": ["A) Prótons", "B) Elétrons", "C) Nêutrons", "D) Núcleos"],
        "resposta": "1",
    },
    ]

class ULTRAQUIZ:
    def __init__(self, root):
        self.root = root
        self.root.title("ULTRAQUIZ")
        self.root.geometry("1920x1080")
        root.configure(bg="#2c3e50") 
        
        self.indice_atual = 0
        self.pontuacao = 0

        self.lbl_pergunta = tk.Label(root, text="", font=("Arial", 14, "bold"), wraplength=400, justify="center")
        self.lbl_pergunta.pack(pady=20)

        self.botoes_opcoes = []
        for i in range(4):
            btn = tk.Button(
                root, text="", font=("Garamond", 12), width=35,
                command=lambda idx=i: self.verificar_resposta(idx)
            )
            btn.pack(pady=5)
            self.botoes_opcoes.append(btn)

        self.carregar_pergunta()

    def carregar_pergunta(self):
        if self.indice_atual < len(perguntas):
            p = perguntas[self.indice_atual]
            self.lbl_pergunta.config(text=p["pergunta"])
            for i, opcao in enumerate(p["opcoes"]):
                self.botoes_opcoes[i].config(text=opcao, state="normal")
        else:
            messagebox.showinfo(
                "Você conseguiu:", 
                f"Você terminou o quiz!\nSua pontuação foi {self.pontuacao} de 7"
            )
            self.root.quit()

    def verificar_resposta(self, escolha):
        p = perguntas[self.indice_atual]
        if escolha == p["resposta"]:
            self.pontuacao += (1)

        self.indice_atual += 1
        self.carregar_pergunta()

if __name__ == "__main__":
    janela = tk.Tk()
    app = ULTRAQUIZ(janela)
    janela.mainloop()
