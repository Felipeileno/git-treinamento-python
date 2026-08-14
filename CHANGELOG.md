# Changelog

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

## [Não lançado]

### Adicionado
- Testes para `calculadora/cli.py` e `calculadora/logging_config.py` (cobertura volta a 100%, que tinha caído para 30% sem ninguém notar)
- Cobertura mínima de testes obrigatória (`--cov-fail-under=100`): o `pytest` agora falha se a cobertura cair, prevenindo essa regressão de se repetir

### Corrigido
- `.vscode/settings.json` ainda referenciava a pasta `src/`, removida no empacotamento
- `requirements.txt` convertido de UTF-16 para UTF-8

## [1.3.0] - 2026-08-13

### Adicionado
- Checagem estática de tipos com mypy (modo `strict`)
- CLI com argumentos via `argparse` (mantém o menu interativo como alternativa, sem argumentos)
- Empacotamento via pip: comando `calculadora` instalável globalmente (`pip install -e .`)
- `Dockerfile` para rodar a CLI em container
- Validação automática no CI: instalação do pacote, build e execução da imagem Docker

### Corrigido
- Pasta `logs/` não era criada automaticamente, causando erro em um clone novo do projeto
- Indentação incorreta no `.pre-commit-config.yaml` desativava Black e Flake8 na pasta `tests/` sem gerar nenhum aviso

## [1.2.0] - 2026-08-11

### Adicionado
- Funções de média, máximo e mínimo de listas de números
- Testes automatizados para as novas funções
- README com badges, tabela de funcionalidades e instruções completas

## [1.1.0] - 2026-08-06

### Adicionado
- Funções de fatorial e módulo (resto da divisão)
- Integração contínua (CI) via GitHub Actions
- Testes automatizados com pytest (20 testes)

### Corrigido
- Conflito de runner do GitHub Actions (troca de `windows-latest` para `ubuntu-latest`)

## [1.0.0] - 2026-08-06

### Adicionado
- Funções básicas: soma, subtração, multiplicação, divisão
- Funções de potência, raiz quadrada e porcentagem
- Menu interativo no `main.py`

### Corrigido
- Imports duplicados e conteúdo trocado entre `calculadora.py` e `main.py`
- Problemas de encoding (acentuação) nos arquivos
