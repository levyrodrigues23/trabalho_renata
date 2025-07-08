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
print("-------------GERENCIADOR DE CADASTRO DE ALUNOS--------------")
print("==============================================================")





def aluno():
    input_aluno = input("digite o nome do aluno: ")
    input_idade = int(input("digite a idade do idade: "))
    input_notafinal = int(input("digite a nota final do aluno: "))

    armazenamento = {"nome": input_aluno, "idade": input_idade, "nota_final": input_notafinal}
    lista_armazenamento = [armazenamento]
    usuario_tentativa = input("voce gostaria de adicionar outro aluno? ")
    if usuario_tentativa == "sim".lower():
        input_aluno = input("digite o nome do aluno: ")
        input_idade = int(input("digite a idade do idade: "))
        input_notafinal = int(input("digite a nota final do aluno: "))

        armazenamento = {"nome": input_aluno, "idade": input_idade, "nota_final": input_notafinal}
        lista_armazenamento = [armazenamento]
    elif usuario_tentativa == "não".lower():
        armazenamento = {"nome": input_aluno, "idade": input_idade, "nota_final": input_notafinal}
        lista_armazenamento = [armazenamento]
        return lista_armazenamento

    return lista_armazenamento



print(aluno())