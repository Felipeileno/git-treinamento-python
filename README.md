# Calculadora Python 🧮

![Tests](https://github.com/Felipeileno/git-treinamento-python/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10--3.14-blue)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![mypy](https://img.shields.io/badge/mypy-strict-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Calculadora em Python criada como projeto de treinamento em lógica de programação, testes automatizados, qualidade de código e Git/GitHub (incluindo CI/CD). Tem 3 formas de uso: CLI com argumentos, menu interativo e interface gráfica.

## 📋 Funcionalidades

| Comando (CLI) | Operação | Observação |
|---|---|---|
| `soma A B` | Soma | |
| `subtracao A B` | Subtração | |
| `multiplicacao A B` | Multiplicação | |
| `divisao A B` | Divisão | Bloqueia divisão por zero |
| `potencia A B` | Potência | |
| `porcentagem A B` | Porcentagem | |
| `modulo A B` | Módulo (resto da divisão) | Bloqueia módulo por zero |
| `raiz-quadrada N` | Raiz quadrada | |
| `fatorial N` | Fatorial | |
| `media N1 N2 ...` | Média de uma lista | |
| `maximo N1 N2 ...` | Máximo de uma lista | |
| `minimo N1 N2 ...` | Mínimo de uma lista | |
| `historico` | Ver histórico de operações | |
| `converter TIPO VALOR` | Conversão de unidades | Veja tipos abaixo |

**Tipos de conversão:** `celsius-fahrenheit`, `fahrenheit-celsius`, `metros-pes`, `pes-metros`, `quilos-libras`, `libras-quilos`

## 🚀 Como executar

```bash
git clone https://github.com/Felipeileno/git-treinamento-python.git
cd git-treinamento-python
pip install -r requirements.txt
```

### CLI com argumentos (uso rápido)

```bash
python main.py soma 2 3
python main.py raiz-quadrada 16
python main.py media 1 2 3 4
python main.py converter celsius-fahrenheit 100
python main.py historico
python main.py --help
```

### Menu interativo

Rodando sem argumentos, abre o menu de sempre (pergunta a operação e os números um por um):

```bash
python main.py
```

## 🖥️ Interface gráfica (opcional)

```bash
python interface.py
```

## 🐳 Docker

A CLI também pode rodar em um container Docker (o menu interativo e a interface gráfica ficam de fora, já que dependem de terminal/tela interativos):

```bash
docker build -t calculadora .
docker run --rm calculadora soma 2 3
docker run --rm calculadora converter celsius-fahrenheit 100
docker run --rm calculadora --help
```

Por padrão, o histórico gerado dentro do container é perdido quando ele termina. Para persistir fora do container:

```bash
docker run --rm -v ${PWD}/logs:/app/logs calculadora soma 2 3
```

### Usando a imagem já publicada (sem precisar buildar)

A cada mudança mesclada na `main`, uma imagem atualizada é publicada automaticamente no GitHub Container Registry:

```bash
docker pull ghcr.io/felipeileno/git-treinamento-python:latest
docker run --rm ghcr.io/felipeileno/git-treinamento-python:latest soma 2 3
```

## 🧪 Como testar

```bash
pytest
pytest --cov=calculadora --cov-report=term-missing
```

## 🔎 Verificação de tipos (mypy)

O projeto usa [mypy](https://mypy.readthedocs.io/) em modo `strict` para checagem estática de tipos em `calculadora/`, `main.py` e `interface.py`.

```bash
mypy
```

## ✅ Qualidade de código

Formatação e linting automatizados com [Black](https://black.readthedocs.io/) e [Flake8](https://flake8.pycqa.org/), aplicados via [pre-commit](https://pre-commit.com/) hooks a cada commit:

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

## 📁 Estrutura do projeto

git-treinamento-python/
├── .github/workflows/tests.yml
├── calculadora/
│ ├── core.py
│ ├── cli.py
│ └── logging_config.py
├── tests/
│ └── test_calculadora.py
├── main.py
├── interface.py
├── conftest.py
├── pyproject.toml
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .flake8
├── .gitignore
├── .pre-commit-config.yaml
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
└── README.md

## 🛠️ Tecnologias

- Python 3.10+ (testado em CI nas versões 3.10 a 3.14)
- Pytest + pytest-cov (testes e cobertura)
- mypy (checagem de tipos, modo strict)
- Black + Flake8 (formatação e linting)
- pre-commit (hooks de qualidade automatizados)
- argparse (CLI)
- tkinter (interface gráfica)
- setuptools (empacotamento via pip)
- Docker
- GitHub Actions (CI)

## 👤 Autor

Felipe Ileno — projeto de treinamento em Python e Git.