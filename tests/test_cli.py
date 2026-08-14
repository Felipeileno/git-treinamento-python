import argparse

import pytest

from calculadora.cli import (
    _registrar_resultado,
    criar_parser,
    executar_comando,
    main,
    menu,
)


@pytest.fixture(autouse=True)
def historico_temporario(tmp_path, monkeypatch):
    """Evita que os testes escrevam no historico.txt real do projeto."""
    caminho = tmp_path / "historico_teste.txt"
    monkeypatch.setattr("calculadora.core.HISTORICO_PATH", caminho)
    yield caminho


def _inputs(respostas):
    """Cria uma função substituta para input(), consumindo respostas em ordem."""
    it = iter(respostas)
    return lambda prompt="": next(it)


class TestRegistrarResultado:
    def test_arredonda_float(self, capsys):
        _registrar_resultado(5.123456, "Soma", "2, 3")
        assert "Resultado: 5.1235" in capsys.readouterr().out

    def test_mantem_int(self, capsys):
        _registrar_resultado(120, "Fatorial", "5")
        assert "Resultado: 120" in capsys.readouterr().out


class TestCriarParser:
    def test_operacao_binaria(self):
        args = criar_parser().parse_args(["soma", "2", "3"])
        assert args.comando == "soma"
        assert args.a == 2.0
        assert args.b == 3.0

    def test_raiz_quadrada(self):
        args = criar_parser().parse_args(["raiz-quadrada", "16"])
        assert args.valor == 16.0

    def test_fatorial(self):
        args = criar_parser().parse_args(["fatorial", "5"])
        assert args.n == 5

    def test_media(self):
        args = criar_parser().parse_args(["media", "1", "2", "3"])
        assert args.numeros == [1.0, 2.0, 3.0]

    def test_historico(self):
        args = criar_parser().parse_args(["historico"])
        assert args.comando == "historico"

    def test_converter(self):
        args = criar_parser().parse_args(["converter", "celsius-fahrenheit", "100"])
        assert args.tipo == "celsius-fahrenheit"
        assert args.valor == 100.0

    def test_sem_argumentos(self):
        args = criar_parser().parse_args([])
        assert args.comando is None

    def test_conversao_invalida_rejeitada(self):
        with pytest.raises(SystemExit):
            criar_parser().parse_args(["converter", "marte-para-plutao", "1"])


class TestExecutarComando:
    def test_operacao_binaria(self, capsys):
        executar_comando(argparse.Namespace(comando="soma", a=2.0, b=3.0))
        assert "Resultado: 5.0" in capsys.readouterr().out

    def test_raiz_quadrada(self, capsys):
        executar_comando(argparse.Namespace(comando="raiz-quadrada", valor=16.0))
        assert "Resultado: 4.0" in capsys.readouterr().out

    def test_fatorial(self, capsys):
        executar_comando(argparse.Namespace(comando="fatorial", n=5))
        assert "Resultado: 120" in capsys.readouterr().out

    @pytest.mark.parametrize(
        "comando,esperado", [("media", 4.0), ("maximo", 6.0), ("minimo", 2.0)]
    )
    def test_listas(self, capsys, comando, esperado):
        args = argparse.Namespace(comando=comando, numeros=[2.0, 4.0, 6.0])
        executar_comando(args)
        assert f"Resultado: {esperado}" in capsys.readouterr().out

    def test_converter(self, capsys):
        args = argparse.Namespace(
            comando="converter", tipo="celsius-fahrenheit", valor=100.0
        )
        executar_comando(args)
        assert "Resultado: 212.0" in capsys.readouterr().out

    def test_historico_vazio(self, capsys):
        executar_comando(argparse.Namespace(comando="historico"))
        assert "Nenhuma operação registrada ainda." in capsys.readouterr().out

    def test_historico_com_dados(self, capsys):
        executar_comando(argparse.Namespace(comando="soma", a=1.0, b=1.0))
        capsys.readouterr()
        executar_comando(argparse.Namespace(comando="historico"))
        assert "Histórico" in capsys.readouterr().out

    def test_erro_divisao_por_zero(self, capsys):
        executar_comando(argparse.Namespace(comando="divisao", a=1.0, b=0.0))
        assert "Erro:" in capsys.readouterr().out

    def test_comando_desconhecido(self, capsys):
        executar_comando(argparse.Namespace(comando="voar"))
        assert "Erro:" in capsys.readouterr().out


class TestMenu:
    def test_ver_historico_vazio(self, monkeypatch, capsys):
        monkeypatch.setattr("builtins.input", _inputs(["13"]))
        menu()
        assert "Nenhuma operação registrada ainda." in capsys.readouterr().out

    def test_ver_historico_com_dados(self, monkeypatch, capsys):
        monkeypatch.setattr("builtins.input", _inputs(["1", "2", "3"]))
        menu()
        capsys.readouterr()
        monkeypatch.setattr("builtins.input", _inputs(["13"]))
        menu()
        assert "Histórico" in capsys.readouterr().out

    def test_raiz_quadrada(self, monkeypatch, capsys):
        monkeypatch.setattr("builtins.input", _inputs(["7", "16"]))
        menu()
        assert "Resultado: 4.0" in capsys.readouterr().out

    def test_fatorial(self, monkeypatch, capsys):
        monkeypatch.setattr("builtins.input", _inputs(["9", "5"]))
        menu()
        assert "Resultado: 120" in capsys.readouterr().out

    @pytest.mark.parametrize(
        "escolha,esperado", [("10", 4.0), ("11", 6.0), ("12", 2.0)]
    )
    def test_listas(self, monkeypatch, capsys, escolha, esperado):
        monkeypatch.setattr("builtins.input", _inputs([escolha, "2,4,6"]))
        menu()
        assert f"Resultado: {esperado}" in capsys.readouterr().out

    def test_conversao(self, monkeypatch, capsys):
        monkeypatch.setattr("builtins.input", _inputs(["14", "100"]))
        menu()
        assert "Resultado: 212.0" in capsys.readouterr().out

    def test_operacao_binaria(self, monkeypatch, capsys):
        monkeypatch.setattr("builtins.input", _inputs(["1", "2", "3"]))
        menu()
        assert "Resultado: 5.0" in capsys.readouterr().out

    def test_opcao_invalida(self, monkeypatch, capsys):
        monkeypatch.setattr("builtins.input", _inputs(["99"]))
        menu()
        assert "Opção inválida." in capsys.readouterr().out

    def test_erro_valor(self, monkeypatch, capsys):
        monkeypatch.setattr("builtins.input", _inputs(["4", "1", "0"]))
        menu()
        assert "Erro:" in capsys.readouterr().out


class TestMain:
    def test_sem_argumentos_chama_menu(self, monkeypatch):
        chamado = {"valor": False}

        def menu_falso():
            chamado["valor"] = True

        monkeypatch.setattr("sys.argv", ["calculadora"])
        monkeypatch.setattr("calculadora.cli.menu", menu_falso)
        main()
        assert chamado["valor"] is True

    def test_com_argumentos_chama_executar_comando(self, monkeypatch, capsys):
        monkeypatch.setattr("sys.argv", ["calculadora", "soma", "2", "3"])
        main()
        assert "Resultado: 5.0" in capsys.readouterr().out
