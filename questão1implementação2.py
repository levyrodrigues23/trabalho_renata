"""Implementação 1: Sistema de Relatórios e Estatísticas de Alunos
Baseado na questão 1, adiciona funcionalidades de análise de dados dos alunos"""

print("==============================================================")
print("--------SISTEMA DE RELATÓRIOS E ESTATÍSTICAS DE ALUNOS-------")
print("==============================================================")

lista_alunos = []

def exibir_menu():
    print("\n" + "="*60)
    print("                MENU DE OPÇÕES")
    print("="*60)
    print("1. Cadastrar Aluno")
    print("2. Consultar Alunos")
    print("3. Relatório de Notas")
    print("4. Estatísticas da Turma")
    print("5. Buscar Aluno por Nome")
    print("6. Alunos por Faixa de Idade")
    print("7. Ranking de Notas")
    print("8. Sair")
    print("="*60)

def validar_dados(idade_str, nota_str):
    if not idade_str.isdigit():
        print("Erro: Idade deve ser um número inteiro!")
        return False
    
    if not nota_str.replace('.', '', 1).isdigit():
        print("Erro: Nota deve ser um número!")
        return False
        
    idade = int(idade_str)
    nota = float(nota_str)
    
    if idade < 0 or idade > 120:
        print("Erro: Idade deve estar entre 0 e 120 anos!")
        return False
    elif nota < 0 or nota > 10:
        print("Erro: Nota deve estar entre 0 e 10!")
        return False
    
    return True

def aluno_existe(nome):
    for dicionario_aluno in lista_alunos:
        if nome.lower() in [n.lower() for n in dicionario_aluno.keys()]:
            return True
    return False

def cadastrar_aluno():
    print("\n--- Cadastrar Novo Aluno ---")
    nome = input("Digite o nome do aluno: ").strip()
    
    if not nome:
        print("Erro: Nome não pode estar vazio!")
        return
    
    if aluno_existe(nome):
        print(f"Erro: Aluno '{nome}' já está cadastrado!")
        return
    
    idade_str = input("Digite a idade do aluno: ")
    nota_str = input("Digite a nota final do aluno: ")
    
    if not validar_dados(idade_str, nota_str):
        return
        
    idade = int(idade_str)
    nota = float(nota_str)
    
    dicionario_aluno = {nome: (idade, nota)}
    lista_alunos.append(dicionario_aluno)
    print(f"✅ Aluno '{nome}' cadastrado com sucesso!")

def consultar_alunos():
    print("\n" + "="*60)
    print("LISTA COMPLETA DE ALUNOS:")
    print("="*60)
    
    if not lista_alunos:
        print("❌ Nenhum aluno cadastrado.")
        return
    
    for i, aluno_dados in enumerate(lista_alunos, 1):
        for nome, dados in aluno_dados.items():
            idade, nota = dados
            status = "✅ Aprovado" if nota >= 6.0 else "❌ Reprovado"
            print(f"{i:2d}. Nome: {nome}")
            print(f"     Idade: {idade} anos | Nota: {nota:.1f} | {status}")
            print("-" * 60)

def relatorio_notas():
    print("\n" + "="*60)
    print("RELATÓRIO DE NOTAS POR CATEGORIA:")
    print("="*60)
    
    if not lista_alunos:
        print("❌ Nenhum aluno cadastrado.")
        return
    
    aprovados = []
    reprovados = []
    excelentes = []
    
    for aluno_dados in lista_alunos:
        for nome, dados in aluno_dados.items():
            idade, nota = dados
            if nota >= 9.0:
                excelentes.append((nome, nota))
            elif nota >= 6.0:
                aprovados.append((nome, nota))
            else:
                reprovados.append((nome, nota))
    
    print(f"🏆 EXCELENTES (Nota ≥ 9.0): {len(excelentes)} alunos")
    for nome, nota in excelentes:
        print(f"   • {nome}: {nota:.1f}")
    
    print(f"\n✅ APROVADOS (6.0 ≤ Nota < 9.0): {len(aprovados)} alunos")
    for nome, nota in aprovados:
        print(f"   • {nome}: {nota:.1f}")
    
    print(f"\n❌ REPROVADOS (Nota < 6.0): {len(reprovados)} alunos")
    for nome, nota in reprovados:
        print(f"   • {nome}: {nota:.1f}")

def estatisticas_turma():
    print("\n" + "="*60)
    print("ESTATÍSTICAS DA TURMA:")
    print("="*60)
    
    if not lista_alunos:
        print("❌ Nenhum aluno cadastrado.")
        return
    
    notas = []
    idades = []
    
    for aluno_dados in lista_alunos:
        for nome, dados in aluno_dados.items():
            idade, nota = dados
            notas.append(nota)
            idades.append(idade)
    
    # Estatísticas das notas
    media_notas = sum(notas) / len(notas)
    maior_nota = max(notas)
    menor_nota = min(notas)
    
    # Estatísticas das idades
    media_idades = sum(idades) / len(idades)
    maior_idade = max(idades)
    menor_idade = min(idades)
    
    print(f"📊 TOTAL DE ALUNOS: {len(lista_alunos)}")
    print(f"📈 NOTAS:")
    print(f"   • Média: {media_notas:.2f}")
    print(f"   • Maior nota: {maior_nota:.1f}")
    print(f"   • Menor nota: {menor_nota:.1f}")
    print(f"👥 IDADES:")
    print(f"   • Média: {media_idades:.1f} anos")
    print(f"   • Maior idade: {maior_idade} anos")
    print(f"   • Menor idade: {menor_idade} anos")
    print(f"📊 APROVEITAMENTO: {(len([n for n in notas if n >= 6.0]) / len(notas) * 100):.1f}%")

def buscar_aluno():
    print("\n--- Buscar Aluno por Nome ---")
    nome_busca = input("Digite o nome (ou parte do nome) para buscar: ").strip().lower()
    
    if not nome_busca:
        print("Erro: Digite um nome para buscar!")
        return
    
    encontrados = []
    for aluno_dados in lista_alunos:
        for nome, dados in aluno_dados.items():
            if nome_busca in nome.lower():
                encontrados.append((nome, dados))
    
    if not encontrados:
        print(f"❌ Nenhum aluno encontrado com '{nome_busca}'")
        return
    
    print(f"\n🔍 Encontrados {len(encontrados)} resultado(s):")
    for nome, dados in encontrados:
        idade, nota = dados
        status = "✅ Aprovado" if nota >= 6.0 else "❌ Reprovado"
        print(f"• {nome} - {idade} anos - Nota: {nota:.1f} - {status}")

def alunos_por_faixa_idade():
    print("\n--- Alunos por Faixa de Idade ---")
    
    if not lista_alunos:
        print("❌ Nenhum aluno cadastrado.")
        return
    
    criancas = []      # 0-12
    adolescentes = []  # 13-17
    jovens = []        # 18-24
    adultos = []       # 25+
    
    for aluno_dados in lista_alunos:
        for nome, dados in aluno_dados.items():
            idade, nota = dados
            if idade <= 12:
                criancas.append((nome, idade, nota))
            elif idade <= 17:
                adolescentes.append((nome, idade, nota))
            elif idade <= 24:
                jovens.append((nome, idade, nota))
            else:
                adultos.append((nome, idade, nota))
    
    print(f"👶 CRIANÇAS (0-12 anos): {len(criancas)} alunos")
    for nome, idade, nota in criancas:
        print(f"   • {nome} ({idade} anos) - Nota: {nota:.1f}")
    
    print(f"\n🧒 ADOLESCENTES (13-17 anos): {len(adolescentes)} alunos")
    for nome, idade, nota in adolescentes:
        print(f"   • {nome} ({idade} anos) - Nota: {nota:.1f}")
    
    print(f"\n👨 JOVENS (18-24 anos): {len(jovens)} alunos")
    for nome, idade, nota in jovens:
        print(f"   • {nome} ({idade} anos) - Nota: {nota:.1f}")
    
    print(f"\n👴 ADULTOS (25+ anos): {len(adultos)} alunos")
    for nome, idade, nota in adultos:
        print(f"   • {nome} ({idade} anos) - Nota: {nota:.1f}")

def ranking_notas():
    print("\n" + "="*60)
    print("🏆 RANKING DE NOTAS (Maior para Menor):")
    print("="*60)
    
    if not lista_alunos:
        print("❌ Nenhum aluno cadastrado.")
        return
    
    # Criar lista de alunos com notas
    alunos_notas = []
    for aluno_dados in lista_alunos:
        for nome, dados in aluno_dados.items():
            idade, nota = dados
            alunos_notas.append((nome, idade, nota))
    
    # Ordenar por nota (decrescente)
    alunos_ordenados = sorted(alunos_notas, key=lambda x: x[2], reverse=True)
    
    for i, (nome, idade, nota) in enumerate(alunos_ordenados, 1):
        if i == 1:
            emoji = "🥇"
        elif i == 2:
            emoji = "🥈"
        elif i == 3:
            emoji = "🥉"
        else:
            emoji = f"{i:2d}º"
        
        status = "✅" if nota >= 6.0 else "❌"
        print(f"{emoji} {nome} - {nota:.1f} ({idade} anos) {status}")

def main():
    while True:
        exibir_menu()
        opcao = input("Digite sua opção: ").strip()
        
        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            consultar_alunos()
        elif opcao == "3":
            relatorio_notas()
        elif opcao == "4":
            estatisticas_turma()
        elif opcao == "5":
            buscar_aluno()
        elif opcao == "6":
            alunos_por_faixa_idade()
        elif opcao == "7":
            ranking_notas()
        elif opcao == "8":
            print("👋 Saindo do sistema...")
            break
        else:
            print("❌ Opção inválida! Digite um número de 1 a 8.")

if __name__ == "__main__":
    main()
