# Documentação: Sistema de Cadastro de Alunos (Questão 1 Implementação 2)

## Descrição Geral
Esta implementação apresenta uma evolução do sistema de cadastro de alunos, com melhorias na estrutura de dados e nas funcionalidades, podendo incluir novos campos ou lógicas adicionais conforme solicitado.

## Funcionalidades
- **Cadastrar Aluno:** Adiciona um novo aluno com dados aprimorados (ex: mais campos além de nome, idade e nota).
- **Consultar Alunos:** Lista detalhada dos alunos cadastrados.
- **Atualizar Dados:** Permite atualização de qualquer campo do aluno.
- **Deletar Aluno:** Remove um aluno do cadastro.
- **Sair:** Encerra o sistema.

## Estrutura de Dados
- **Lista de Dicionários:** Estrutura pode ser `{nome: {'idade': idade, 'nota': nota, ...}}` permitindo expansão para mais informações.

## Validações
- Nome não pode ser vazio ou duplicado.
- Idade deve ser inteiro não negativo.
- Nota deve ser número entre 0 e 10.
- Validações feitas apenas com condicionais.

## Fluxo do Programa
1. Exibe menu de opções.
2. Usuário escolhe operação e fornece dados.
3. Validações são feitas antes de qualquer alteração.

## Diferenciais
- Estrutura de dados preparada para expansão.
- Código limpo, sem uso de try/except.
- Facilidade para adicionar novos campos ou regras.

---
