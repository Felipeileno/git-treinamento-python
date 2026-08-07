from calculadora import soma, subtracao, multiplicacao, divisao, potencia, raiz_quadrada, porcentagem, fatorial, modulo

def menu():
    opcoes = {
        "1": ("Soma", soma),
        "2": ("Subtração", subtracao),
        "3": ("Multiplicação", multiplicacao),
        "4": ("Divisão", divisao),
        "5": ("Potência", potencia),
        "6": ("Porcentagem", porcentagem),
        "8": ("Módulo (resto da divisão)", modulo),
    }

    print("=== Calculadora ===")
    for chave, (nome, _) in opcoes.items():
        print(f"{chave} - {nome}")
    print("7 - Raiz quadrada (só precisa de 1 número)")
    print("9 - Fatorial (só precisa de 1 número)")

    escolha = input("Escolha uma opção: ")

    try:
        if escolha == "7":
            valor = float(input("Digite o número: "))
            resultado = raiz_quadrada(valor)
        elif escolha == "9":
            valor = int(input("Digite o número: "))
            resultado = fatorial(valor)
        elif escolha in opcoes:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            _, funcao = opcoes[escolha]
            resultado = funcao(a, b)
        else:
            print("Opção inválida.")
            return

        print(f"Resultado: {resultado}")

    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    menu()
