"""Implementação 2: Sistema de Notas com Disciplinas Múltiplas
Baseado na questão 1, expande para gerenciar múltiplas disciplinas por aluno"""

print("==============================================================")
print("------SISTEMA DE NOTAS COM DISCIPLINAS MÚLTIPLAS-------------")
print("==============================================================")

lista_alunos = []
disciplinas_disponiveis = ["Matemática", "Português", "História", "Geografia", "Ciências", "Inglês", "Educação Física"]

def exibir_menu():
    print("\n" + "="*55)
    print("              MENU DE OPÇÕES")
    print("="*55)
    print("1. Cadastrar Aluno")
    print("2. Adicionar Nota em Disciplina")
    print("3. Consultar Boletim do Aluno")
    print("4. Consultar Todos os Alunos")
    print("5. Relatório por Disciplina")
    print("6. Calcular Média Geral")
    print("7. Alunos em Recuperação")
    print("8. Ranking por Disciplina")
    print("9. Atualizar Nota")
    print("10. Sair")
    print("="*55)

def validar_nota(nota_str):
    if not nota_str.replace('.', '', 1).isdigit():
        print("❌ Erro: Nota deve ser um número!")
        return False, 0
    
    nota = float(nota_str)
    if nota < 0 or nota > 10:
        print("❌ Erro: Nota deve estar entre 0 e 10!")
        return False, 0
    
    return True, nota

def validar_idade(idade_str):
    if not idade_str.isdigit():
        print("❌ Erro: Idade deve ser um número inteiro!")
        return False, 0
    
    idade = int(idade_str)
    if idade < 0 or idade > 120:
        print("❌ Erro: Idade deve estar entre 0 e 120 anos!")
        return False, 0
    
    return True, idade

def buscar_aluno(nome):
    for aluno in lista_alunos:
        if nome.lower() in [n.lower() for n in aluno.keys()]:
            return aluno
    return None

def cadastrar_aluno():
    print("\n--- 📝 Cadastrar Novo Aluno ---")
    nome = input("Digite o nome do aluno: ").strip()
    
    if not nome:
        print("❌ Erro: Nome não pode estar vazio!")
        return
    
    if buscar_aluno(nome):
        print(f"❌ Erro: Aluno '{nome}' já está cadastrado!")
        return
    
    idade_str = input("Digite a idade do aluno: ")
    valido, idade = validar_idade(idade_str)
    if not valido:
        return
    
    # Estrutura: {nome: (idade, {disciplina: [notas]})}
    aluno = {nome: (idade, {})}
    lista_alunos.append(aluno)
    print(f"✅ Aluno '{nome}' cadastrado com sucesso!")
    print("💡 Use a opção 2 para adicionar notas nas disciplinas.")

def exibir_disciplinas():
    print("\n� Disciplinas disponíveis:")
    for i, disciplina in enumerate(disciplinas_disponiveis, 1):
        print(f"{i}. {disciplina}")

def adicionar_nota():
    print("\n--- 📊 Adicionar Nota em Disciplina ---")
    nome = input("Digite o nome do aluno: ").strip()
    
    if not nome:
        print("❌ Erro: Nome não pode estar vazio!")
        return
    
    aluno = buscar_aluno(nome)
    if not aluno:
        print(f"❌ Aluno '{nome}' não encontrado!")
        return
    
    exibir_disciplinas()
    opcao_str = input("\nEscolha a disciplina (número): ")
    
    if not opcao_str.isdigit():
        print("❌ Digite um número válido!")
        return
    
    opcao = int(opcao_str)
    if 1 <= opcao <= len(disciplinas_disponiveis):
        disciplina = disciplinas_disponiveis[opcao - 1]
    else:
        print("❌ Opção inválida!")
        return
    
    nota_str = input(f"Digite a nota para {disciplina}: ")
    valido, nota = validar_nota(nota_str)
    if not valido:
        return
    
    # Adicionar nota à disciplina
    nome_aluno = list(aluno.keys())[0]
    idade, notas_disciplinas = aluno[nome_aluno]
    
    if disciplina not in notas_disciplinas:
        notas_disciplinas[disciplina] = []
    
    notas_disciplinas[disciplina].append(nota)
    aluno[nome_aluno] = (idade, notas_disciplinas)
    
    print(f"✅ Nota {nota} adicionada em {disciplina} para {nome_aluno}!")

def consultar_boletim():
    print("\n--- � Boletim do Aluno ---")
    nome = input("Digite o nome do aluno: ").strip()
    
    if not nome:
        print("❌ Erro: Nome não pode estar vazio!")
        return
    
    aluno = buscar_aluno(nome)
    if not aluno:
        print(f"❌ Aluno '{nome}' não encontrado!")
        return
    
    nome_aluno = list(aluno.keys())[0]
    idade, notas_disciplinas = aluno[nome_aluno]
    
    print(f"\n" + "="*50)
    print(f"📋 BOLETIM DE {nome_aluno.upper()}")
    print(f"👤 Idade: {idade} anos")
    print("="*50)
    
    if not notas_disciplinas:
        print("❌ Nenhuma nota cadastrada ainda.")
        return
    
    total_medias = 0
    count_disciplinas = 0
    
    for disciplina, notas in notas_disciplinas.items():
        if notas:
            media = sum(notas) / len(notas)
            total_medias += media
            count_disciplinas += 1
            status = "✅ Aprovado" if media >= 6.0 else "❌ Reprovado"
            
            print(f"📚 {disciplina}:")
            print(f"   Notas: {', '.join(map(str, notas))}")
            print(f"   Média: {media:.2f} {status}")
            print("-" * 50)
    
    if count_disciplinas > 0:
        media_geral = total_medias / count_disciplinas
        status_geral = "✅ APROVADO" if media_geral >= 6.0 else "❌ REPROVADO"
        print(f"🎯 MÉDIA GERAL: {media_geral:.2f} - {status_geral}")

def consultar_todos():
    print("\n" + "="*60)
    print("� RESUMO DE TODOS OS ALUNOS")
    print("="*60)
    
    if not lista_alunos:
        print("❌ Nenhum aluno cadastrado.")
        return
    
    for aluno in lista_alunos:
        nome_aluno = list(aluno.keys())[0]
        idade, notas_disciplinas = aluno[nome_aluno]
        
        total_medias = 0
        count_disciplinas = 0
        
        for disciplina, notas in notas_disciplinas.items():
            if notas:
                media = sum(notas) / len(notas)
                total_medias += media
                count_disciplinas += 1
        
        if count_disciplinas > 0:
            media_geral = total_medias / count_disciplinas
            status = "✅" if media_geral >= 6.0 else "❌"
        else:
            media_geral = 0
            status = "⏳"
        
        print(f"� {nome_aluno} ({idade} anos)")
        print(f"   Disciplinas: {count_disciplinas} | Média Geral: {media_geral:.2f} {status}")
        print("-" * 60)

def relatorio_disciplina():
    print("\n--- � Relatório por Disciplina ---")
    exibir_disciplinas()
    
    opcao_str = input("\nEscolha a disciplina (número): ")
    if not opcao_str.isdigit():
        print("❌ Digite um número válido!")
        return
    opcao = int(opcao_str)
    if 1 <= opcao <= len(disciplinas_disponiveis):
        disciplina = disciplinas_disponiveis[opcao - 1]
    else:
        print("❌ Opção inválida!")
        return
    
    print(f"\n" + "="*50)
    print(f"📚 RELATÓRIO DE {disciplina.upper()}")
    print("="*50)
    
    alunos_com_nota = []
    
    for aluno in lista_alunos:
        nome_aluno = list(aluno.keys())[0]
        idade, notas_disciplinas = aluno[nome_aluno]
        
        if disciplina in notas_disciplinas and notas_disciplinas[disciplina]:
            notas = notas_disciplinas[disciplina]
            media = sum(notas) / len(notas)
            alunos_com_nota.append((nome_aluno, media, notas))
    
    if not alunos_com_nota:
        print("❌ Nenhum aluno tem notas nesta disciplina.")
        return
    
    # Ordenar por média (maior para menor)
    alunos_com_nota.sort(key=lambda x: x[1], reverse=True)
    
    soma_medias = 0
    for i, (nome, media, notas) in enumerate(alunos_com_nota, 1):
        status = "✅" if media >= 6.0 else "❌"
        emoji = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i:2d}º"
        
        print(f"{emoji} {nome} - Média: {media:.2f} {status}")
        print(f"    Notas: {', '.join(map(str, notas))}")
        soma_medias += media
    
    media_turma = soma_medias / len(alunos_com_nota)
    aprovados = len([x for x in alunos_com_nota if x[1] >= 6.0])
    print(f"\n📊 Estatísticas da turma em {disciplina}:")
    print(f"   Média da turma: {media_turma:.2f}")
    print(f"   Aprovados: {aprovados}/{len(alunos_com_nota)} ({aprovados/len(alunos_com_nota)*100:.1f}%)")

def calcular_media_geral():
    print("\n--- 🎯 Média Geral da Turma ---")
    
    if not lista_alunos:
        print("❌ Nenhum aluno cadastrado.")
        return
    
    soma_total = 0
    count_total = 0
    
    for aluno in lista_alunos:
        nome_aluno = list(aluno.keys())[0]
        idade, notas_disciplinas = aluno[nome_aluno]
        
        for disciplina, notas in notas_disciplinas.items():
            if notas:
                soma_total += sum(notas)
                count_total += len(notas)
    
    if count_total == 0:
        print("❌ Nenhuma nota cadastrada ainda.")
        return
    
    media_geral = soma_total / count_total
    print(f"🎯 Média geral da turma: {media_geral:.2f}")
    
    if media_geral >= 8.0:
        print("🏆 Excelente desempenho da turma!")
    elif media_geral >= 6.0:
        print("✅ Bom desempenho da turma!")
    else:
        print("⚠️ Turma precisa de atenção especial.")

def alunos_recuperacao():
    print("\n--- ⚠️ Alunos em Recuperação ---")
    
    alunos_recuperacao = []
    
    for aluno in lista_alunos:
        nome_aluno = list(aluno.keys())[0]
        idade, notas_disciplinas = aluno[nome_aluno]
        
        disciplinas_recuperacao = []
        
        for disciplina, notas in notas_disciplinas.items():
            if notas:
                media = sum(notas) / len(notas)
                if media < 6.0:
                    disciplinas_recuperacao.append((disciplina, media))
        
        if disciplinas_recuperacao:
            alunos_recuperacao.append((nome_aluno, disciplinas_recuperacao))
    
    if not alunos_recuperacao:
        print("🎉 Nenhum aluno em recuperação! Parabéns!")
        return
    
    print(f"⚠️ {len(alunos_recuperacao)} aluno(s) precisam de recuperação:")
    print("-" * 50)
    
    for nome, disciplinas in alunos_recuperacao:
        print(f"👤 {nome}:")
        for disciplina, media in disciplinas:
            print(f"   📚 {disciplina}: {media:.2f}")
        print("-" * 50)

def ranking_disciplina():
    print("\n--- 🏆 Ranking por Disciplina ---")
    exibir_disciplinas()
    
    opcao_str = input("\nEscolha a disciplina (número): ")
    if not opcao_str.isdigit():
        print("❌ Digite um número válido!")
        return
    opcao = int(opcao_str)
    if 1 <= opcao <= len(disciplinas_disponiveis):
        disciplina = disciplinas_disponiveis[opcao - 1]
    else:
        print("❌ Opção inválida!")
        return
    
    alunos_ranking = []
    
    for aluno in lista_alunos:
        nome_aluno = list(aluno.keys())[0]
        idade, notas_disciplinas = aluno[nome_aluno]
        
        if disciplina in notas_disciplinas and notas_disciplinas[disciplina]:
            notas = notas_disciplinas[disciplina]
            media = sum(notas) / len(notas)
            alunos_ranking.append((nome_aluno, media))
    
    if not alunos_ranking:
        print(f"❌ Nenhum aluno tem notas em {disciplina}.")
        return
    
    alunos_ranking.sort(key=lambda x: x[1], reverse=True)
    
    print(f"\n🏆 RANKING DE {disciplina.upper()}")
    print("="*40)
    
    for i, (nome, media) in enumerate(alunos_ranking, 1):
        if i == 1:
            emoji = "🥇"
        elif i == 2:
            emoji = "🥈"
        elif i == 3:
            emoji = "🥉"
        else:
            emoji = f"{i:2d}º"
        
        status = "✅" if media >= 6.0 else "❌"
        print(f"{emoji} {nome} - {media:.2f} {status}")

def atualizar_nota():
    print("\n--- ✏️ Atualizar Nota ---")
    nome = input("Digite o nome do aluno: ").strip()
    
    if not nome:
        print("❌ Erro: Nome não pode estar vazio!")
        return
    
    aluno = buscar_aluno(nome)
    if not aluno:
        print(f"❌ Aluno '{nome}' não encontrado!")
        return
    
    nome_aluno = list(aluno.keys())[0]
    idade, notas_disciplinas = aluno[nome_aluno]
    
    if not notas_disciplinas:
        print("❌ Este aluno não tem notas cadastradas.")
        return
    
    print(f"\n� Disciplinas de {nome_aluno}:")
    disciplinas_aluno = list(notas_disciplinas.keys())
    for i, disciplina in enumerate(disciplinas_aluno, 1):
        notas = notas_disciplinas[disciplina]
        print(f"{i}. {disciplina} - Notas: {', '.join(map(str, notas))}")
    
    opcao_str = input("\nEscolha a disciplina (número): ")
    if not opcao_str.isdigit():
        print("❌ Digite um número válido!")
        return
    opcao = int(opcao_str)
    if 1 <= opcao <= len(disciplinas_aluno):
        disciplina_escolhida = disciplinas_aluno[opcao - 1]
    else:
        print("❌ Opção inválida!")
        return
    notas_atuais = notas_disciplinas[disciplina_escolhida]
    print(f"\nNotas atuais em {disciplina_escolhida}: {', '.join(map(str, notas_atuais))}")
    indice_str = input(f"Qual nota deseja alterar? (1 a {len(notas_atuais)}): ")
    if not indice_str.isdigit():
        print("❌ Digite um número válido!")
        return
    indice = int(indice_str) - 1
    if 0 <= indice < len(notas_atuais):
        nova_nota_str = input(f"Nova nota (atual: {notas_atuais[indice]}): ")
        valido, nova_nota = validar_nota(nova_nota_str)
        if valido:
            notas_atuais[indice] = nova_nota
            print(f"✅ Nota atualizada com sucesso!")
    else:
        print("❌ Índice inválido!")

def main():
    while True:
        exibir_menu()
        opcao = input("Digite sua opção: ").strip()
        
        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            adicionar_nota()
        elif opcao == "3":
            consultar_boletim()
        elif opcao == "4":
            consultar_todos()
        elif opcao == "5":
            relatorio_disciplina()
        elif opcao == "6":
            calcular_media_geral()
        elif opcao == "7":
            alunos_recuperacao()
        elif opcao == "8":
            ranking_disciplina()
        elif opcao == "9":
            atualizar_nota()
        elif opcao == "10":
            print("👋 Saindo do sistema...")
            break
        else:
            print("❌ Opção inválida! Digite um número de 1 a 10.")

if __name__ == "__main__":
    main()
