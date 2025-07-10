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
print("----------SISTEMA DE GERENCIAMENTO DE ALUNOS-----------------")
print("==============================================================")

lista_alunos = []

def exibir_menu():
    print("\n" + "="*50)
    print("           MENU DE OPÇÕES")
    print("="*50)
    print("1. Cadastrar Aluno")
    print("2. Consultar Alunos")
    print("3. Atualizar Dados do Aluno")
    print("4. Deletar Aluno")
    print("5. Sair")
    print("="*50)

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

def buscar_aluno(nome):
    for i, dicionario_aluno in enumerate(lista_alunos):
        if nome.lower() in [n.lower() for n in dicionario_aluno.keys()]:
            return i
    return -1

def cadastrar_aluno():
    print("\n--- Cadastrar Novo Aluno ---")
    nome = input("Digite o nome do aluno: ").strip()
    
    if not nome:
        print("Erro: Nome não pode estar vazio!")
        return
    
    if buscar_aluno(nome) != -1:
        print(f"Erro: Aluno '{nome}' já está cadastrado!")
        return
    
    idade_str = input("Digite a idade do aluno: ")
    nota_str = input("Digite a nota final do aluno: ")
    
    if not validar_entrada(idade_str, nota_str):
        return
        
    idade = int(idade_str)
    nota = float(nota_str)
    
    dicionario_aluno = {nome: (idade, nota)}
    lista_alunos.append(dicionario_aluno)
    print(f"Aluno '{nome}' cadastrado com sucesso!")

def consultar_alunos():
    print("\n==============================================================")
    print("ALUNOS CADASTRADOS:")
    print("==============================================================")
    
    if not lista_alunos:
        print("Nenhum aluno cadastrado.")
        return
    
    for i, aluno_dados in enumerate(lista_alunos, 1):
        for nome, dados in aluno_dados.items():
            idade, nota_final = dados
            print(f"{i}. Nome: {nome}")
            print(f"   Idade: {idade} anos")
            print(f"   Nota Final: {nota_final}")
            print("-" * 50)

def atualizar_aluno():
    print("\n--- Atualizar Dados do Aluno ---")
    nome = input("Digite o nome do aluno que deseja atualizar: ").strip()
    
    if not nome:
        print("Erro: Nome não pode estar vazio!")
        return
    
    indice = buscar_aluno(nome)
    if indice == -1:
        print(f"Aluno '{nome}' não encontrado!")
        return
    
    print(f"Aluno encontrado: {nome}")
    idade_atual, nota_atual = list(lista_alunos[indice].values())[0]
    print(f"Dados atuais - Idade: {idade_atual}, Nota: {nota_atual}")
    
    nova_idade = input("Digite a nova idade (ou ENTER para manter atual): ")
    nova_nota = input("Digite a nova nota (ou ENTER para manter atual): ")
    
    if nova_idade == "":
        nova_idade = str(idade_atual)
    if nova_nota == "":
        nova_nota = str(nota_atual)
    
    if not validar_entrada(nova_idade, nova_nota):
        return
    
    lista_alunos[indice] = {nome: (int(nova_idade), float(nova_nota))}
    print(f"Dados do aluno '{nome}' atualizados com sucesso!")

def deletar_aluno():
    print("\n--- Deletar Aluno ---")
    nome = input("Digite o nome do aluno que deseja deletar: ").strip()
    
    if not nome:
        print("Erro: Nome não pode estar vazio!")
        return
    
    indice = buscar_aluno(nome)
    if indice == -1:
        print(f"Aluno '{nome}' não encontrado!")
        return
    
    confirmacao = input(f"Tem certeza que deseja deletar o aluno '{nome}'? (sim/não): ").lower()
    if confirmacao == "sim":
        lista_alunos.pop(indice)
        print(f"Aluno '{nome}' deletado com sucesso!")
    else:
        print("Operação cancelada.")

def main():
    while True:
        exibir_menu()
        opcao = input("Digite sua opção: ").strip()
        
        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            consultar_alunos()
        elif opcao == "3":
            atualizar_aluno()
        elif opcao == "4":
            deletar_aluno()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Digite um número de 1 a 5.")

main()