# Documentação: Sistema de Cadastro de Alunos Multidisciplinar (Questão 1 Implementação 1)

## Descrição Geral
Esta versão aprimorada do sistema de cadastro de alunos permite o registro de múltiplas disciplinas para cada aluno, associando notas específicas a cada disciplina. O sistema é totalmente baseado em validação condicional, sem uso de try/except.

## Funcionalidades
- **Cadastrar Aluno:** Adiciona um novo aluno, permitindo cadastrar várias disciplinas e notas para cada uma.
- **Consultar Alunos:** Exibe todos os alunos cadastrados, listando suas disciplinas e respectivas notas.
- **Atualizar Dados:** Permite atualizar disciplinas e notas de um aluno.
- **Deletar Aluno:** Remove um aluno do sistema.
- **Sair:** Encerra o programa.

## Estrutura de Dados
- **Lista de Dicionários:** Cada aluno é um dicionário `{nome: {'idade': idade, 'disciplinas': {disciplina: nota, ...}}}` armazenado em uma lista.

## Validações
- Nome não pode ser vazio ou duplicado.
- Idade deve ser inteiro não negativo.
- Disciplinas não podem ser duplicadas para o mesmo aluno.
- Notas devem ser números entre 0 e 10.
- Todas as validações são feitas com condicionais.

## Fluxo do Programa
1. Exibe menu de opções.
2. Usuário escolhe operação e fornece dados.
3. Para cada disciplina, solicita nome e nota.
4. Validações são feitas antes de qualquer alteração.

## Diferenciais
- Suporte a múltiplas disciplinas por aluno.
- Estrutura de dados mais complexa e flexível.
- Validação robusta sem uso de exceções.

---
