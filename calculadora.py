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