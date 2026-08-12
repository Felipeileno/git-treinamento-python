# Changelog

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

## [Não lançado]

### Adicionado
- Estrutura de pastas `src/`, `tests/` e `docs/`

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
