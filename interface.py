import tkinter as tk
from tkinter import messagebox

from src.calculadora import (
    soma,
    subtracao,
    multiplicacao,
    divisao,
    potencia,
    porcentagem,
)


def calcular():
    try:
        a = float(entrada_a.get())
        b = float(entrada_b.get())
        operacao = operacao_selecionada.get()

        operacoes = {
            "Soma": soma,
            "Subtração": subtracao,
            "Multiplicação": multiplicacao,
            "Divisão": divisao,
            "Potência": potencia,
            "Porcentagem": porcentagem,
        }

        resultado = operacoes[operacao](a, b)
        if isinstance(resultado, float):
            resultado = round(resultado, 4)
        label_resultado.config(text=f"Resultado: {resultado}")

    except ValueError as e:
        messagebox.showerror("Erro", str(e))


janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x280")

tk.Label(janela, text="Primeiro número:").pack(pady=5)
entrada_a = tk.Entry(janela)
entrada_a.pack()

tk.Label(janela, text="Segundo número:").pack(pady=5)
entrada_b = tk.Entry(janela)
entrada_b.pack()

operacao_selecionada = tk.StringVar(janela)
operacao_selecionada.set("Soma")
menu_operacao = tk.OptionMenu(
    janela,
    operacao_selecionada,
    "Soma",
    "Subtração",
    "Multiplicação",
    "Divisão",
    "Potência",
    "Porcentagem",
)
menu_operacao.pack(pady=10)

botao_calcular = tk.Button(janela, text="Calcular", command=calcular)
botao_calcular.pack(pady=5)

label_resultado = tk.Label(janela, text="Resultado: ")
label_resultado.pack(pady=10)

janela.mainloop()
