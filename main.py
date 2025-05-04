import json
import os

#Funções Auxiliares 
def carregar_dados(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []

def salvar_dados(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def listar_registros(titulo, registros):
    if not registros:
        print(f"Nenhum {titulo} cadastrado.")
        return
    print(f"\n--- {titulo} Cadastrados ---")
    for registro in registros:
        info = " | ".join([f"{chave.capitalize()}: {valor}" for chave, valor in registro.items()])
        print(info)

def buscar_registro(registros, chave, valor_busca):
    for i, registro in enumerate(registros):
        if str(registro.get(chave)).lower() == str(valor_busca).lower():
            return i, registro
    return -1, None

#Módulo de Estudantes
arquivo_estudantes = "estudantes.json"
estudantes = carregar_dados(arquivo_estudantes)

def incluir_estudante():
    print("\n--- Incluir Estudante ---")
    nome = input("Digite o nome do estudante: ")
    cpf = input("Digite o CPF do estudante: ")
    numero = input("Digite o número de matrícula do estudante: ")
    estudante = {"nome": nome, "cpf": cpf, "numero": numero}
    estudantes.append(estudante)
    salvar_dados(arquivo_estudantes, estudantes)
    print("Estudante adicionado com sucesso!")

def listar_estudantes():
    listar_registros("Estudantes", estudantes)

def editar_estudante():
    print("\n--- Editar Estudante ---")
    nome_busca = input("Digite o nome do estudante que deseja editar: ")
    indice, estudante = buscar_registro(estudantes, "nome", nome_busca)
    if estudante:
        print(f"Estudante encontrado: {estudante}")
        print("O que deseja editar?")
        print("1. Nome | 2. CPF | 3. Matrícula | 4. Tudo | 0. Cancelar")
        opcao = input("Digite a opção: ")
        if opcao == "1" or opcao == "4": estudante["nome"] = input("Novo nome: ")
        if opcao == "2" or opcao == "4": estudante["cpf"] = input("Novo CPF: ")
        if opcao == "3" or opcao == "4": estudante["numero"] = input("Nova matrícula: ")
        if opcao != "0":
            salvar_dados(arquivo_estudantes, estudantes)
            print("Estudante atualizado com sucesso!")
    else:
        print(f"Estudante com nome '{nome_busca}' não encontrado.")

def excluir_estudante():
    print("\n--- Excluir Estudante ---")
    nome_busca = input("Digite o nome do estudante que deseja excluir: ")
    indice, estudante = buscar_registro(estudantes, "nome", nome_busca)
    if estudante:
        print(f"Estudante encontrado: {estudante}")
        confirmacao = input("Tem certeza que deseja excluir? (sim/não): ").lower()
        if confirmacao == "sim":
            estudantes.pop(indice)
            salvar_dados(arquivo_estudantes, estudantes)
            print("Estudante excluído com sucesso!")
    else:
        print(f"Estudante com nome '{nome_busca}' não encontrado.")

def menu_estudantes():
    while True:
        print("\n--- Menu Estudantes ---")
        print("1. Incluir | 2. Listar | 3. Editar | 4. Excluir | 0. Voltar")
        opcao = input("Digite a opção: ")
        if opcao == "1": incluir_estudante()
        elif opcao == "2": listar_estudantes()
        elif opcao == "3": editar_estudante()
        elif opcao == "4": excluir_estudante()
        elif opcao == "0": break
        else: print("Opção inválida.")

#Módulo de Professores
arquivo_professores = "professores.json"
professores = carregar_dados(arquivo_professores)

def incluir_professor():
    print("\n--- Incluir Professor ---")
    try:
        codigo = int(input("Digite o código do professor: "))
        nome = input("Digite o nome do professor: ")
        cpf = input("Digite o CPF do professor: ")
        professor = {"codigo": codigo, "nome": nome, "cpf": cpf}
        professores.append(professor)
        salvar_dados(arquivo_professores, professores)
        print("Professor adicionado com sucesso!")
    except ValueError:
        print("Código do professor deve ser um número inteiro.")

def listar_professores():
    listar_registros("Professores", professores)

def editar_professor():
    print("\n--- Editar Professor ---")
    try:
        codigo_busca = int(input("Digite o código do professor que deseja editar: "))
        indice, professor = buscar_registro(professores, "codigo", codigo_busca)
        if professor:
            print(f"Professor encontrado: {professor}")
            print("O que deseja editar?")
            print("1. Nome | 2. CPF | 0. Cancelar")
            opcao = input("Digite a opção: ")
            if opcao == "1": professor["nome"] = input("Novo nome: ")
            if opcao == "2": professor["cpf"] = input("Novo CPF: ")
            if opcao != "0":
                salvar_dados(arquivo_professores, professores)
                print("Professor atualizado com sucesso!")
        else:
            print(f"Professor com código '{codigo_busca}' não encontrado.")
    except ValueError:
        print("Código do professor deve ser um número inteiro.")

def excluir_professor():
    print("\n--- Excluir Professor ---")
    try:
        codigo_busca = int(input("Digite o código do professor que deseja excluir: "))
        indice, professor = buscar_registro(professores, "codigo", codigo_busca)
        if professor:
            print(f"Professor encontrado: {professor}")
            confirmacao = input("Tem certeza que deseja excluir? (sim/não): ").lower()
            if confirmacao == "sim":
                professores.pop(indice)
                salvar_dados(arquivo_professores, professores)
                print("Professor excluído com sucesso!")
        else:
            print(f"Professor com código '{codigo_busca}' não encontrado.")
    except ValueError:
        print("Código do professor deve ser um número inteiro.")

def menu_professores():
    while True:
        print("\n--- Menu Professores ---")
        print("1. Incluir | 2. Listar | 3. Editar | 4. Excluir | 0. Voltar")
        opcao = input("Digite a opção: ")
        if opcao == "1": incluir_professor()
        elif opcao == "2": listar_professores()
        elif opcao == "3": editar_professor()
        elif opcao == "4": excluir_professor()
        elif opcao == "0": break
        else: print("Opção inválida.")

#Módulo de Disciplinas
arquivo_disciplinas = "disciplinas.json"
disciplinas = carregar_dados(arquivo_disciplinas)

def incluir_disciplina():
    print("\n--- Incluir Disciplina ---")
    try:
        codigo = int(input("Digite o código da disciplina: "))
        nome = input("Digite o nome da disciplina: ")
        disciplina = {"codigo": codigo, "nome": nome}
        disciplinas.append(disciplina)
        salvar_dados(arquivo_disciplinas, disciplinas)
        print("Disciplina adicionada com sucesso!")
    except ValueError:
        print("Código da disciplina deve ser um número inteiro.")

def listar_disciplinas():
    listar_registros("Disciplinas", disciplinas)

def editar_disciplina():
    print("\n--- Editar Disciplina ---")
    try:
        codigo_busca = int(input("Digite o código da disciplina que deseja editar: "))
        indice, disciplina = buscar_registro(disciplinas, "codigo", codigo_busca)
        if disciplina:
            print(f"Disciplina encontrada: {disciplina}")
            novo_nome = input("Novo nome da disciplina: ")
            disciplina["nome"] = novo_nome
            salvar_dados(arquivo_disciplinas, disciplinas)
            print("Disciplina atualizada com sucesso!")
        else:
            print(f"Disciplina com código '{codigo_busca}' não encontrada.")
    except ValueError:
        print("Código da disciplina deve ser um número inteiro.")

def excluir_disciplina():
    print("\n--- Excluir Disciplina ---")
    try:
        codigo_busca = int(input("Digite o código da disciplina que deseja excluir: "))
        indice, disciplina = buscar_registro(disciplinas, "codigo", codigo_busca)
        if disciplina:
            print(f"Disciplina encontrada: {disciplina}")
            confirmacao = input("Tem certeza que deseja excluir? (sim/não): ").lower()
            if confirmacao == "sim":
                disciplinas.pop(indice)
                salvar_dados(arquivo_disciplinas, disciplinas)
                print("Disciplina excluída com sucesso!")
        else:
            print(f"Disciplina com código '{codigo_busca}' não encontrada.")
    except ValueError:
        print("Código da disciplina deve ser um número inteiro.")

def menu_disciplinas():
    while True:
        print("\n--- Menu Disciplinas ---")
        print("1. Incluir | 2. Listar | 3. Editar | 4. Excluir | 0. Voltar")
        opcao = input("Digite a opção: ")
        if opcao == "1": incluir_disciplina()
        elif opcao == "2": listar_disciplinas()
        elif opcao == "3": editar_disciplina()
        elif opcao == "4": excluir_disciplina()
        elif opcao == "0": break
        else: print("Opção inválida.")

#Módulo de Turmas
arquivo_turmas = "turmas.json"
turmas = carregar_dados(arquivo_turmas)

def incluir_turma():
    print("\n--- Incluir Turma ---")
    try:
        codigo = int(input("Digite o código da turma: "))
        # Validação de código existente
        if any(turma["codigo"] == codigo for turma in turmas):
            print("Erro: Código de turma já existente.")
            return
        codigo_professor = int(input("Digite o código do professor: "))
        codigo_disciplina = int(input("Digite o código da disciplina: "))
        turma = {"codigo": codigo, "codigo_professor": codigo_professor, "codigo_disciplina": codigo_disciplina}
        turmas.append(turma)
        salvar_dados(arquivo_turmas, turmas)
        print("Turma adicionada com sucesso!")
    except ValueError:
        print("Códigos devem ser números inteiros.")

def listar_turmas():
    listar_registros("Turmas", turmas)

def editar_turma():
    print("\n--- Editar Turma ---")
    try:
        codigo_busca = int(input("Digite o código da turma que deseja editar: "))
        indice, turma = buscar_registro(turmas, "codigo", codigo_busca)
        if turma:
            print(f"Turma encontrada: {turma}")
            print("O que deseja editar?")
            print("1. Código do Professor | 2. Código da Disciplina | 0. Cancelar")
            opcao = input("Digite a opção: ")
            if opcao == "1": turma["codigo_professor"] = int(input("Novo código do professor: "))
            if opcao == "2": turma["codigo_disciplina"] = int(input("Novo código da disciplina: "))
            if opcao != "0":
                salvar_dados(arquivo_turmas, turmas)
                print("Turma atualizada com sucesso!")
        else:
            print(f"Turma com código '{codigo_busca}' não encontrada.")
    except ValueError:
        print("Códigos devem ser números inteiros.")

def excluir_turma():
    print("\n--- Excluir Turma ---")
    try:
        codigo_busca = int(input("Digite o código da turma que deseja excluir: "))
        indice, turma = buscar_registro(turmas, "codigo", codigo_busca)
        if turma:
            print(f"Turma encontrada: {turma}")
            confirmacao = input("Tem certeza que deseja excluir? (sim/não): ").lower()
            if confirmacao == "sim":
                turmas.pop(indice)
                salvar_dados(arquivo_turmas, turmas)
                print("Turma excluída com sucesso!")
        else:
            print(f"Turma com código '{codigo_busca}' não encontrada.")
    except ValueError:
        print("Código da turma deve ser um número inteiro.")

def menu_turmas():
    while True:
        print("\n--- Menu Turmas ---")
        print("1. Incluir | 2. Listar | 3. Editar | 4. Excluir | 0. Voltar")
        opcao = input("Digite a opção: ")
        if opcao == "1": incluir_turma()
        elif opcao == "2": listar_turmas()
        elif opcao == "3": editar_turma()
        elif opcao == "4": excluir_turma()
        elif opcao == "0": break
        else: print("Opção inválida.")

#Módulo de Matrículas
arquivo_matriculas = "matriculas.json"
matriculas = carregar_dados(arquivo_matriculas)

def incluir_matricula():
    print("\n--- Incluir Matrícula ---")
    try:
        codigo_turma = int(input("Digite o código da turma: "))
        codigo_estudante = int(input("Digite o código do estudante: "))
        # Validação de matrícula existente (combinação turma/estudante)
        if any(matricula["codigo_turma"] == codigo_turma and matricula["codigo_estudante"] == codigo_estudante for matricula in matriculas):
            print("Erro: Matrícula para esta turma e estudante já existe.")
            return
        matricula = {"codigo_turma": codigo_turma, "codigo_estudante": codigo_estudante}
        matriculas.append(matricula)
        salvar_dados(arquivo_matriculas, matriculas)
        print("Matrícula adicionada com sucesso!")
    except ValueError:
        print("Códigos devem ser números inteiros.")

def listar_matriculas():
    listar_registros("Matrículas", matriculas)

def excluir_matricula():
    print("\n--- Excluir Matrícula ---")
    try:
        codigo_turma_busca = int(input("Digite o código da turma da matrícula que deseja excluir: "))
        codigo_estudante_busca = int(input("Digite o código do estudante da matrícula que deseja excluir: "))
        for i, matricula in enumerate(matriculas):
            if matricula["codigo_turma"] == codigo_turma_busca and matricula["codigo_estudante"] == codigo_estudante_busca:
                print(f"Matrícula encontrada: {matricula}")
                confirmacao = input("Tem certeza que deseja excluir? (sim/não): ").lower()
                if confirmacao == "sim":
                    matriculas.pop(i)
                    salvar_dados(arquivo_matriculas, matriculas)
                    print("Matrícula excluída com sucesso!")
                return
        print(f"Matrícula para Turma '{codigo_turma_busca}' e Estudante '{codigo_estudante_busca}' não encontrada.")
    except ValueError:
        print("Códigos devem ser números inteiros.")

def menu_matriculas():
    while True:
        print("\n--- Menu Matrículas ---")
        print("1. Incluir | 2. Listar | 3. Excluir | 0. Voltar")
        opcao = input("Digite a opção: ")
        if opcao == "1": incluir_matricula()
        elif opcao == "2": listar_matriculas()
        elif opcao == "3": excluir_matricula()
        elif opcao == "0": break
        else: print("Opção inválida.")

#Menu Principal
while True:
    print("\n--- Menu Principal ---")
    print("1. Estudantes | 2. Professores | 3. Disciplinas | 4. Turmas | 5. Matrículas | 0. Sair")
    opcao_principal = input("Digite a opção: ")
    if opcao_principal == "1": menu_estudantes()
    elif opcao_principal == "2": menu_professores()
    elif opcao_principal == "3": menu_disciplinas()
    elif opcao_principal == "4": menu_turmas()
    elif opcao_principal == "5": menu_matriculas()
    elif opcao_principal == "0":
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida.")
