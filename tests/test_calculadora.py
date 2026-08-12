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
