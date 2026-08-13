import argparse
import logging
from typing import Callable

from src.calculadora import (
    soma,
    subtracao,
    multiplicacao,
    divisao,
    potencia,
    raiz_quadrada,
    porcentagem,
    fatorial,
    modulo,
    media,
    maximo,
    minimo,
    salvar_historico,
    ver_historico,
    celsius_para_fahrenheit,
    fahrenheit_para_celsius,
    metros_para_pes,
    pes_para_metros,
    quilos_para_libras,
    libras_para_quilos,
)
from src.logging_config import configurar_logging

OPERACOES: dict[str, tuple[str, Callable[..., float]]] = {
    "soma": ("Soma", soma),
    "subtracao": ("Subtração", subtracao),
    "multiplicacao": ("Multiplicação", multiplicacao),
    "divisao": ("Divisão", divisao),
    "potencia": ("Potência", potencia),
    "porcentagem": ("Porcentagem", porcentagem),
    "modulo": ("Módulo (resto da divisão)", modulo),
}

CONVERSOES: dict[str, tuple[str, Callable[..., float]]] = {
    "celsius-fahrenheit": ("Celsius para Fahrenheit", celsius_para_fahrenheit),
    "fahrenheit-celsius": ("Fahrenheit para Celsius", fahrenheit_para_celsius),
    "metros-pes": ("Metros para Pés", metros_para_pes),
    "pes-metros": ("Pés para Metros", pes_para_metros),
    "quilos-libras": ("Quilos para Libras", quilos_para_libras),
    "libras-quilos": ("Libras para Quilos", libras_para_quilos),
}


def _registrar_resultado(
    resultado: float | int, nome_op: str, valores_str: str
) -> None:
    """Arredonda, salva no histórico, loga e imprime o resultado de uma operação."""
    if isinstance(resultado, float):
        resultado = round(resultado, 4)
    salvar_historico(nome_op, valores_str, resultado)
    logging.info(
        f"Operação '{nome_op}' executada com sucesso. " f"Resultado: {resultado}"
    )
    print(f"Resultado: {resultado}")


def menu() -> None:
    opcoes: dict[str, tuple[str, Callable[..., float]]] = {
        "1": OPERACOES["soma"],
        "2": OPERACOES["subtracao"],
        "3": OPERACOES["multiplicacao"],
        "4": OPERACOES["divisao"],
        "5": OPERACOES["potencia"],
        "6": OPERACOES["porcentagem"],
        "8": OPERACOES["modulo"],
    }
    conversoes: dict[str, tuple[str, Callable[..., float]]] = {
        "14": CONVERSOES["celsius-fahrenheit"],
        "15": CONVERSOES["fahrenheit-celsius"],
        "16": CONVERSOES["metros-pes"],
        "17": CONVERSOES["pes-metros"],
        "18": CONVERSOES["quilos-libras"],
        "19": CONVERSOES["libras-quilos"],
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
    print("--- Conversões ---")
    for chave, (nome, _) in conversoes.items():
        print(f"{chave} - {nome}")

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
        elif escolha in conversoes:
            valor = float(input("Digite o valor: "))
            nome_op, funcao = conversoes[escolha]
            resultado = funcao(valor)
            valores_str = f"{valor}"
        elif escolha in opcoes:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            nome_op, funcao = opcoes[escolha]
            resultado = funcao(a, b)
            valores_str = f"{a}, {b}"
        else:
            print("Opção inválida.")
            logging.warning(f"Opção inválida selecionada: {escolha}")
            return

        _registrar_resultado(resultado, nome_op, valores_str)

    except ValueError as e:
        logging.error(f"Erro na operação: {e}")
        print(f"Erro: {e}")


def criar_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="calculadora",
        description=(
            "Calculadora de linha de comando. "
            "Sem argumentos, abre o menu interativo."
        ),
    )
    subparsers = parser.add_subparsers(dest="comando")

    for chave, (nome_op, _) in OPERACOES.items():
        sub = subparsers.add_parser(chave, help=f"{nome_op} de dois números")
        sub.add_argument("a", type=float)
        sub.add_argument("b", type=float)

    sub_raiz = subparsers.add_parser("raiz-quadrada", help="Raiz quadrada de um número")
    sub_raiz.add_argument("valor", type=float)

    sub_fatorial = subparsers.add_parser(
        "fatorial", help="Fatorial de um número inteiro"
    )
    sub_fatorial.add_argument("n", type=int)

    for chave, ajuda in (
        ("media", "Média de uma lista de números"),
        ("maximo", "Máximo de uma lista de números"),
        ("minimo", "Mínimo de uma lista de números"),
    ):
        sub = subparsers.add_parser(chave, help=ajuda)
        sub.add_argument("numeros", type=float, nargs="+")

    subparsers.add_parser("historico", help="Mostra o histórico de operações")

    sub_conv = subparsers.add_parser("converter", help="Converte unidades")
    sub_conv.add_argument("tipo", choices=sorted(CONVERSOES.keys()))
    sub_conv.add_argument("valor", type=float)

    return parser


def executar_comando(args: argparse.Namespace) -> None:
    comando = args.comando

    try:
        if comando == "historico":
            linhas = ver_historico()
            if not linhas:
                print("Nenhuma operação registrada ainda.")
            else:
                print("\n=== Histórico ===")
                for linha in linhas:
                    print(linha.strip())
            return

        if comando == "raiz-quadrada":
            resultado = raiz_quadrada(args.valor)
            nome_op = "Raiz quadrada"
            valores_str = f"{args.valor}"
        elif comando == "fatorial":
            resultado = fatorial(args.n)
            nome_op = "Fatorial"
            valores_str = f"{args.n}"
        elif comando in ("media", "maximo", "minimo"):
            numeros = list(args.numeros)
            if comando == "media":
                resultado = media(numeros)
                nome_op = "Média"
            elif comando == "maximo":
                resultado = maximo(numeros)
                nome_op = "Máximo"
            else:
                resultado = minimo(numeros)
                nome_op = "Mínimo"
            valores_str = str(numeros)
        elif comando == "converter":
            nome_op, funcao_conv = CONVERSOES[args.tipo]
            resultado = funcao_conv(args.valor)
            valores_str = f"{args.valor}"
        elif comando in OPERACOES:
            nome_op, funcao_op = OPERACOES[comando]
            resultado = funcao_op(args.a, args.b)
            valores_str = f"{args.a}, {args.b}"
        else:
            raise ValueError(f"Comando desconhecido: {comando}")

        _registrar_resultado(resultado, nome_op, valores_str)

    except ValueError as e:
        logging.error(f"Erro na operação: {e}")
        print(f"Erro: {e}")


def main() -> None:
    configurar_logging()
    logging.info("Calculadora iniciada")

    parser = criar_parser()
    args = parser.parse_args()

    if args.comando is None:
        menu()
    else:
        executar_comando(args)


if __name__ == "__main__":
    main()
