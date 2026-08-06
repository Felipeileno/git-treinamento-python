from calculadora import soma, subtracao, multiplicacao, divisao
def menu():
    opcoes = {
        "1": ("Soma", soma),
        "2": ("Subtração", subtracao),
        "3": ("Multiplicação", multiplicacao),
        "4": ("Divisão", divisao),
    }

    print("=== Calculadora ===")
    for chave, (nome, _) in opcoes.items():
        print(f"{chave} - {nome}")

    escolha = input("Escolha uma opção: ")
    if escolha not in opcoes:
        print("Opção inválida.")
        return

    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return

    _, funcao = opcoes[escolha]

    try:
        resultado = funcao(a, b)
        print(f"Resultado: {resultado}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    menu()