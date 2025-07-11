"""1. Cadastro de Alunos
Descrição: Criar um programa que armazene e gerencie o cadastro de alunos,
incluindo nome, idade e nota final.
Estruturas utilizadas:
• Dicionário: Para armazenar os dados de cada aluno, onde a chave é o nome
e o valor é uma tupla contendo idade e nota final.
• Lista: Para armazenar todos os dicionários dos alunos.
• Laço while: Para permitir o cadastro de múltiplos alunos até que o usuário
decida parar.
• Condicionais (if, elif, else): Para verificar se o aluno já está cadastrado ou se
os dados foram inseridos corretamente."""

print("==============================================================")
print("----------SISTEMA DE CADASTRO DE ALUNOS-----------------------")
print("==============================================================")

lista_alunos = []

def validar_entrada(idade_str, nota_str):
    if not idade_str.isdigit():
        print("Erro: Idade deve ser um número inteiro!")
        return False
    
    if not nota_str.replace('.', '', 1).isdigit():
        print("Erro: Nota deve ser um número!")
        return False
    
    idade = int(idade_str)
    nota = float(nota_str)
    
    if idade < 0:
        print("Erro: Idade não pode ser negativa!")
        return False
    elif nota < 0 or nota > 10:
        print("Erro: Nota deve estar entre 0 e 10!")
        return False
    
    return True

def aluno_ja_cadastrado(nome):
    for aluno in lista_alunos:
        if nome.lower() in [n.lower() for n in aluno.keys()]:
            return True
    return False

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ").strip()
    if nome.lower() == 'sair':
        break

    if not nome:
        print("Erro: Nome não pode estar vazio!")
        continue

    if aluno_ja_cadastrado(nome):
        print(f"Erro: Aluno '{nome}' já está cadastrado!")
        continue

    idade_str = input("Digite a idade do aluno: ").strip()
    nota_str = input("Digite a nota final do aluno: ").strip()

    if not validar_entrada(idade_str, nota_str):
        continue

    idade = int(idade_str)
    nota = float(nota_str)
    
    dicionario_aluno = {nome: (idade, nota)}
    lista_alunos.append(dicionario_aluno)
    print(f"Aluno '{nome}' cadastrado com sucesso!")

# Exibindo todos os alunos cadastrados ao final
print("\n==============================================================")
print("ALUNOS CADASTRADOS:")
print("==============================================================")
for i, aluno in enumerate(lista_alunos, 1):
    for nome, dados in aluno.items():
        idade, nota = dados
        print(f"{i}. Nome: {nome} | Idade: {idade} | Nota Final: {nota}")
