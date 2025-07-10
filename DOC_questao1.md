# Documentação: Sistema de Cadastro de Alunos (Questão 1)

## Descrição Geral
Este sistema implementa um cadastro simples de alunos em Python, permitindo as operações de CRUD (Criar, Ler, Atualizar, Deletar) para alunos, com validação de dados e interface de menu interativo no terminal.

## Funcionalidades
- **Cadastrar Aluno:** Adiciona um novo aluno com nome, idade e nota final.
- **Consultar Alunos:** Lista todos os alunos cadastrados, mostrando nome, idade e nota.
- **Atualizar Dados do Aluno:** Permite alterar idade e nota de um aluno já cadastrado.
- **Deletar Aluno:** Remove um aluno do cadastro após confirmação.
- **Sair:** Encerra o programa.

## Estrutura de Dados
- **Lista de Dicionários:** Cada aluno é armazenado como um dicionário `{nome: (idade, nota)}` dentro de uma lista `lista_alunos`.

## Validações
- Nome não pode ser vazio e não pode ser duplicado.
- Idade deve ser um número inteiro não negativo.
- Nota deve ser um número entre 0 e 10.
- Atualização permite manter valores antigos pressionando ENTER.

## Fluxo do Programa
1. Exibe menu de opções.
2. Usuário escolhe a operação.
3. Para cada operação, solicita os dados necessários e realiza validações.
4. Mensagens de erro são exibidas para entradas inválidas.

## Diferenciais
- Não utiliza blocos try/except para validação, apenas condicionais.
- Interface simples e intuitiva para uso em terminal.

---
