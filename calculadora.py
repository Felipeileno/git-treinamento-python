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
