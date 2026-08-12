from datetime import datetime
from pathlib import Path


def soma(a: float, b: float) -> float:
    return a + b


def subtracao(a: float, b: float) -> float:
    return a - b


def multiplicacao(a: float, b: float) -> float:
    return a * b


def divisao(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Divisão por zero não permitida.")
    return a / b


def potencia(base: float, expoente: float) -> float:
    return base**expoente


def raiz_quadrada(valor: float) -> float:
    if valor < 0:
        raise ValueError("Não é possível calcular raiz de número negativo.")
    return valor**0.5


def porcentagem(valor: float, percentual: float) -> float:
    return valor * (percentual / 100)


def fatorial(n: int) -> int:
    if n < 0:
        raise ValueError("Não é possível calcular fatorial de número negativo.")
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def modulo(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Não é possível calcular resto da divisão por zero.")
    return a % b


def media(numeros: list[float]) -> float:
    if not numeros:
        raise ValueError("A lista não pode estar vazia.")
    return sum(numeros) / len(numeros)


def maximo(numeros: list[float]) -> float:
    if not numeros:
        raise ValueError("A lista não pode estar vazia.")
    return max(numeros)


def minimo(numeros: list[float]) -> float:
    if not numeros:
        raise ValueError("A lista não pode estar vazia.")
    return min(numeros)


HISTORICO_PATH = Path("logs/historico.txt")


def salvar_historico(operacao: str, valores: str, resultado) -> None:
    HISTORICO_PATH.parent.mkdir(exist_ok=True)
    linha = (
        f"{datetime.now():%d/%m/%Y %H:%M:%S} | {operacao} | "
        f"{valores} | Resultado: {resultado}\n"
    )
    with open(HISTORICO_PATH, "a", encoding="utf-8") as arquivo:
        arquivo.write(linha)


def ver_historico() -> list[str]:
    if not HISTORICO_PATH.exists():
        return []
    with open(HISTORICO_PATH, "r", encoding="utf-8") as arquivo:
        return arquivo.readlines()


def celsius_para_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32


def fahrenheit_para_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def metros_para_pes(metros: float) -> float:
    return metros * 3.28084


def pes_para_metros(pes: float) -> float:
    return pes / 3.28084


def quilos_para_libras(quilos: float) -> float:
    return quilos * 2.20462


def libras_para_quilos(libras: float) -> float:
    return libras / 2.20462
