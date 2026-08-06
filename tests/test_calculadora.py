import pytest
from calculadora import soma, subtracao, multiplicacao, divisao, potencia, raiz_quadrada, porcentagem

def test_soma():
    assert soma(2, 3) == 5

def test_subtracao():
    assert subtracao(10, 4) == 6

def test_multiplicacao():
    assert multiplicacao(3, 4) == 12

def test_divisao():
    assert divisao(10, 2) == 5

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        divisao(10, 0)

def test_potencia():
    assert potencia(2, 3) == 8

def test_raiz_quadrada():
    assert raiz_quadrada(9) == 3

def test_raiz_negativa():
    with pytest.raises(ValueError):
        raiz_quadrada(-4)

def test_porcentagem():
    assert porcentagem(200, 10) == 20
