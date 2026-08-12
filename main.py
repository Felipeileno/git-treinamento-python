from src.calculadora import soma, subtracao, multiplicacao, divisao, potencia, raiz_quadrada, porcentagem, fatorial, modulo, media, maximo, minimo, salvar_historico, ver_historico

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
    print("10 - Média de uma lista de números")
    print("11 - Máximo de uma lista de números")
    print("12 - Mínimo de uma lista de números")
    print("13 - Ver histórico de operações")

    escolha = input("Escolha uma opção: ")

    try:
        if escolha == "13":
            linhas = ver_historico()
            if not linhas:
                print("Nenhuma operação registrada ainda.")
            else:
                print("\n=== Histórico ===")
                for linha in linhas:
                    print(linha.strip())
            return

        if escolha == "7":
            valor = float(input("Digite o número: "))
            resultado = raiz_quadrada(valor)
            nome_op = "Raiz quadrada"
            valores_str = f"{valor}"
        elif escolha == "9":
            valor = int(input("Digite o número: "))
            resultado = fatorial(valor)
            nome_op = "Fatorial"
            valores_str = f"{valor}"
        elif escolha in ("10", "11", "12"):
            entrada = input("Digite os números separados por vírgula (ex: 2,4,6): ")
            numeros = [float(n.strip()) for n in entrada.split(",")]
            if escolha == "10":
                resultado = media(numeros)
                nome_op = "Média"
            elif escolha == "11":
                resultado = maximo(numeros)
                nome_op = "Máximo"
            else:
                resultado = minimo(numeros)
                nome_op = "Mínimo"
            valores_str = str(numeros)
        elif escolha in opcoes:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            nome_op, funcao = opcoes[escolha]
            resultado = funcao(a, b)
            valores_str = f"{a}, {b}"
        else:
            print("Opção inválida.")
            return

        if isinstance(resultado, float):
            resultado = round(resultado, 4)

        salvar_historico(nome_op, valores_str, resultado)
        print(f"Resultado: {resultado}")

    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    menu()
