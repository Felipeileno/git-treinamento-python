# Como Contribuir

Obrigado por considerar contribuir com este projeto! Aqui está o fluxo recomendado.

## Antes de começar

1. Certifique-se de ter o [Python 3.10+](https://www.python.org/downloads/) instalado
2. Clone o repositório e instale as dependências:
```bash
   pip install -r requirements.txt
   pip install pytest pytest-cov
```

## Fluxo de contribuição

1. **Crie uma branch** a partir da `main`, com um nome descritivo:
```bash
   git checkout -b feature/nome-da-sua-alteracao
```

2. **Faça suas alterações** no código

3. **Escreva ou atualize os testes** correspondentes em `tests/test_calculadora.py`

4. **Confirme que todos os testes passam** antes de enviar:
```bash
   pytest
```

5. **Verifique a cobertura de testes** (o `pytest` já falha automaticamente se cair abaixo de 100%):
```bash
   pytest --cov=calculadora --cov-report=term-missing
```

6. **Confirme que o mypy e o pre-commit passam**:
```bash
   mypy
   pre-commit run --all-files
```

7. **Faça o commit** seguindo o padrão de mensagens abaixo

8. **Envie a branch e abra um Pull Request**:
```bash
   git push -u origin feature/nome-da-sua-alteracao
```

## Padrão de mensagens de commit

Este projeto segue o padrão [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` — nova funcionalidade
- `fix:` — correção de bug
- `test:` — adição ou ajuste de testes
- `docs:` — mudanças na documentação
- `refactor:` — reorganização de código sem alterar comportamento
- `chore:` — tarefas de manutenção (dependências, configuração)

Exemplo: `feat: adiciona conversão de temperatura`

## Checklist antes de abrir o Pull Request

- [ ] Todos os testes passam (`pytest`)
- [ ] A cobertura de testes não diminuiu (`pytest` falha automaticamente abaixo de 100%)
- [ ] `mypy` não reporta erros
- [ ] `pre-commit run --all-files` passa (Black + Flake8 + mypy)
- [ ] A mensagem de commit segue o padrão acima