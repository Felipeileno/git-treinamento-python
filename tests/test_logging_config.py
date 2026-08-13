import logging

from calculadora.logging_config import configurar_logging


def test_configurar_logging_cria_pasta_e_handlers(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    handlers_originais = logging.root.handlers[:]
    logging.root.handlers = []
    try:
        configurar_logging()

        assert (tmp_path / "logs").is_dir()
        assert len(logging.root.handlers) == 2
        assert any(isinstance(h, logging.FileHandler) for h in logging.root.handlers)
        assert any(isinstance(h, logging.StreamHandler) for h in logging.root.handlers)
    finally:
        for handler in logging.root.handlers[:]:
            handler.close()
        logging.root.handlers = handlers_originais
