# Calculadora Python 🧮

![Tests](https://github.com/Felipeileno/git-treinamento-python/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.14-blue)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

Calculadora de linha de comando desenvolvida em Python, criada como projeto de treinamento em lógica de programação, testes automatizados e Git/GitHub (incluindo CI/CD).

## 📋 Funcionalidades

| Opção | Operação | Observação |
|---|---|---|
| 1 | Soma | |
| 2 | Subtração | |
| 3 | Multiplicação | |
| 4 | Divisão | Bloqueia divisão por zero |
| 5 | Potência | |
| 6 | Porcentagem | |
| 7 | Raiz quadrada | Só pede 1 número |
| 8 | Módulo (resto da divisão) | |
| 9 | Fatorial | Só pede 1 número |
| 10 | Média de uma lista | Números separados por vírgula |
| 11 | Máximo de uma lista | Números separados por vírgula |
| 12 | Mínimo de uma lista | Números separados por vírgula |

## 🚀 Como executar

\`\`\`bash
git clone https://github.com/Felipeileno/git-treinamento-python.git
cd git-treinamento-python
python main.py
\`\`\`

## 🖥️ Interface gráfica (opcional)

Além do menu de linha de comando, o projeto também tem uma versão com interface gráfica:

\`\`\`bash
python interface.py
\`\`\`

## 🧪 Como testar

\`\`\`bash
pip install pytest
pytest
\`\`\`

## 📁 Estrutura do projeto

\`\`\`
git-treinamento-python/
├── .github/workflows/tests.yml
├── tests/test_calculadora.py
├── calculadora.py
├── main.py
├── conftest.py
├── requirements.txt
└── README.md
\`\`\`

## 🛠️ Tecnologias

- Python 3.14
- Pytest
- GitHub Actions (CI)

## 👤 Autor

Felipe Ileno — projeto de treinamento em Python e Git.
