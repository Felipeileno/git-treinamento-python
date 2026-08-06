from calculadora import soma, subtracao, multiplicacao
print("=== Treinamento Git ===")
a = 20
b = 10
print(f"Soma: {soma(a, b)}")
print(f"Subtração: {subtracao(a, b)}")
print(f"Multiplicação: {multiplicacao(a, b)}")
from calculadora import divisao
resultado = divisao(10, 2)
print(f"Resultado da divisão: {resultado}")
from src.calculadora import somar, dividir

def main():
    print(somar(5, 3))
    print(dividir(10, 2))

if __name__ == "__main__":
    main()