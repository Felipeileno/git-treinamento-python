def soma(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não permitida")
    return a / b
def somar(a: float, b: float) -> float:
    return a + b
def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b
def calcular_porcentagem(valor: float, percentual: float) -> float:
    """Calcula o percentual de um valor.
    
    Args:
        valor: valor base.
        percentual: percentual a ser calculado (ex: 10 para 10%).

    Returns:
        Resultado do cálculo.
    """
    return valor * (percentual / 100)