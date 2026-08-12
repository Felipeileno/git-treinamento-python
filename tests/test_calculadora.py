import pytest
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
)

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

def test_fatorial():
    assert fatorial(5) == 120

def test_fatorial_zero():
    assert fatorial(0) == 1

def test_fatorial_negativo():
    with pytest.raises(ValueError):
        fatorial(-3)

def test_modulo():
    assert modulo(10, 3) == 1

def test_modulo_por_zero():
    with pytest.raises(ValueError):
        modulo(10, 0)

def test_media():
    assert media([2, 4, 6]) == 4

def test_media_lista_vazia():
    with pytest.raises(ValueError):
        media([])

def test_maximo():
    assert maximo([3, 7, 1, 9, 4]) == 9

def test_maximo_lista_vazia():
    with pytest.raises(ValueError):
        maximo([])

def test_minimo():
    assert minimo([3, 7, 1, 9, 4]) == 1

def test_minimo_lista_vazia():
    with pytest.raises(ValueError):
        minimo([])
@pytest.mark.parametrize("a, b, esperado", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300),
    (-5, -5, -10),
])
def test_soma_parametrizado(a, b, esperado):
    assert soma(a, b) == esperado


@pytest.mark.parametrize("a, b, esperado", [
    (10, 2, 5),
    (9, 3, 3),
    (-10, 2, -5),
    (7.5, 2.5, 3.0),
])
def test_divisao_parametrizado(a, b, esperado):
    assert divisao(a, b) == esperado


@pytest.mark.parametrize("valor, esperado", [
    (0, 1),
    (1, 1),
    (5, 120),
    (6, 720),
])
def test_fatorial_parametrizado(valor, esperado):
    assert fatorial(valor) == esperado


@pytest.mark.parametrize("numeros, esperado", [
    ([1, 2, 3], 2),
    ([10, 20, 30], 20),
    ([5], 5),
    ([-2, -4, -6], -4),
])
def test_media_parametrizado(numeros, esperado):
    assert media(numeros) == esperado


@pytest.mark.parametrize("valor", [-1, -5, -100])
def test_fatorial_negativo_parametrizado(valor):
    with pytest.raises(ValueError):
        fatorial(valor)