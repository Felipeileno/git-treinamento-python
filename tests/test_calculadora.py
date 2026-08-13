import pytest
from calculadora.core import (
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
    celsius_para_fahrenheit,
    fahrenheit_para_celsius,
    metros_para_pes,
    pes_para_metros,
    quilos_para_libras,
    libras_para_quilos,
    salvar_historico,
    ver_historico,
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
@pytest.mark.parametrize("a, b, esperado", [
    (3, 4, 12),
    (-2, 5, -10),
    (0, 100, 0),
    (7, 7, 49),
    (-3, -3, 9),
])
def test_multiplicacao_parametrizado(a, b, esperado):
    assert multiplicacao(a, b) == esperado


@pytest.mark.parametrize("base, expoente, esperado", [
    (2, 3, 8),
    (5, 0, 1),
    (10, 2, 100),
    (2, 10, 1024),
    (3, 1, 3),
])
def test_potencia_parametrizado(base, expoente, esperado):
    assert potencia(base, expoente) == esperado


@pytest.mark.parametrize("a, b, esperado", [
    (10, 3, 1),
    (9, 3, 0),
    (7, 2, 1),
    (100, 10, 0),
    (5, 7, 5),
])
def test_modulo_parametrizado(a, b, esperado):
    assert modulo(a, b) == esperado


@pytest.mark.parametrize("numeros, esperado", [
    ([3, 7, 1, 9, 4], 9),
    ([-5, -1, -10], -1),
    ([100], 100),
    ([2, 2, 2], 2),
])
def test_maximo_parametrizado(numeros, esperado):
    assert maximo(numeros) == esperado


@pytest.mark.parametrize("numeros, esperado", [
    ([3, 7, 1, 9, 4], 1),
    ([-5, -1, -10], -10),
    ([100], 100),
    ([2, 2, 2], 2),
])
def test_minimo_parametrizado(numeros, esperado):
    assert minimo(numeros) == esperado
@pytest.mark.parametrize("celsius, esperado", [
    (0, 32.0),
    (100, 212.0),
    (-40, -40.0),
    (37, 98.6),
])
def test_celsius_para_fahrenheit_parametrizado(celsius, esperado):
    assert round(celsius_para_fahrenheit(celsius), 1) == esperado


@pytest.mark.parametrize("fahrenheit, esperado", [
    (32, 0.0),
    (212, 100.0),
    (-40, -40.0),
    (98.6, 37.0),
])
def test_fahrenheit_para_celsius_parametrizado(fahrenheit, esperado):
    assert round(fahrenheit_para_celsius(fahrenheit), 1) == esperado


def test_metros_para_pes():
    assert round(metros_para_pes(1), 2) == 3.28


def test_pes_para_metros():
    assert round(pes_para_metros(3.28084), 2) == 1.0


def test_quilos_para_libras():
    assert round(quilos_para_libras(1), 2) == 2.20


def test_libras_para_quilos():
    assert round(libras_para_quilos(2.20462), 2) == 1.0
def test_salvar_e_ver_historico(tmp_path, monkeypatch):
    caminho_temporario = tmp_path / "historico_teste.txt"
    monkeypatch.setattr("calculadora.core.HISTORICO_PATH", caminho_temporario)

    salvar_historico("Soma", "2, 3", 5)
    linhas = ver_historico()

    assert len(linhas) == 1
    assert "Soma" in linhas[0]
    assert "5" in linhas[0]


def test_ver_historico_vazio(tmp_path, monkeypatch):
    caminho_temporario = tmp_path / "historico_vazio.txt"
    monkeypatch.setattr("calculadora.core.HISTORICO_PATH", caminho_temporario)

    linhas = ver_historico()
    assert linhas == []
