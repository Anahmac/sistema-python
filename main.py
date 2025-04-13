#Nome: Ana Flávia Maciel / Curso: Análise e desenvolvomento de sistemas 
 #Lista para estudantes
estudantes = []
#Menu principal 
def exibir_menu():
  print("Bem-vindo ao menu!")
  print("1. Estudantes")
  print("2. Disciplinas")
  print("3. Professores")
  print("4. Turmas")
  print("5. Matrículas")
  print("0. sair")
#Submenu
def exibir_submenu():
  print ("Menu de operações")
  print ("1. Incluir")
  print ("2. Listar")
  print ("3. Atualizar")
  print ("4. Excluir")
  print("0. sair")
#Incluir estudante
def incluir_estudantes():
  nome = input("Digite o nome do estudante:")
  cpf = input("Digite o CPF do estudante:")
  numero = input ("Digite o número de matrícula do estudante:")
  estudante = {
     "nome": nome,
     "cpf": cpf,
     "numero": numero
  }
  estudantes.append(estudante)
  print(f"Estudante: {nome}, adicionado com sucesso!")

#Editar estudante
def editar_estudante():
   entrada = input("Digite o nome do estudante que deseja editar: ")
   #verifica se há um estudante com esse nome 
   nomes = [e["nome"]for e in estudantes]
   if entrada in nomes:
      indice = nomes.index(entrada)
      estudante = estudantes[indice]
      print(f"\nEstudante encontrado: {estudante}")

      print("O que você deseja editar?")
      print ("1. Nome")
      print ("2. CPF")
      print ("3. Matrícula")
      print ("4. Editar tudo")

      opçao = input("Digite o número da opção desejada:")
      if opçao == "1" or opçao == "4":
         novo_nome = input ("Novo nome: ")
         estudante["nome"] = novo_nome

      if opçao == "2" or opçao == "4":
         novo_cpf = input("Novo CPF: ")
         estudante["cpf"] = novo_cpf

      if opçao == "3" or opçao == "4":
         nova_matricula = input ("Nova matrícula: ")
         estudante["numero"] = nova_matricula 

         print("Estudante atualizado com sucesso!")
         print(estudante)
#Listar estudantes
def listar_estudantes():
    if not estudantes:
      print("Ainda não há estudantes cadastrados")  
      return
    print("\nEstudantes cadastrados:")
    for i, est in enumerate(estudantes, start=1):
       print(f"{i}. Nome: {est['nome']}, CPF: {est['cpf']}, Matrícula: {est['numero']}")

#Excluir estudante
def excluir_estudante():
   entrada = input("Digite o nome do estudante que deseja remover: ")
   #verifica se há um estudante com esse nome 
   nomes = [e["nome"]for e in estudantes]
   if entrada in nomes:
      indice = nomes.index(entrada)
      estudante = estudantes[indice]
      print(f"Estudante encontrado: {estudante}")
      confirmaçao = input ("Tem certeza que deseja excluir o estudante? (sim/não):").lower()
      
      if confirmaçao == "sim":
         estudantes.pop(indice)
         print ("Estudante removido com sucesso!")
      else:
         print("Operação cancelada.")
       
#loop principal
while True:
      exibir_menu()
    #Coletar escolha do usuário
      escolha = int (input("Digite o número da opção escolhida:"))
      if escolha == 1:
          print("Você escolheu: Estudantes")
      elif escolha == 2:
          print("Essa opção ainda está em desenvolvimento")
          continue
      elif escolha == 3:
          print("Essa opção ainda está em desenvolvimento")
          continue
      elif escolha == 4:
          print("Essa opção ainda está em desenvolvimento")
          continue
      elif escolha == 5:
          print("Essa opção ainda está em desenvolvimento")
          continue
      elif escolha == 0:
          print("Encerrando programa")     
          break
      else:
          print("Escolha inválida, tente novamente.")  
          continue
      if True:
            #loop secundário 
            #Submenu
              while True:
                  exibir_submenu()
                #Coletar a escolha do usuário
                  escolha = int(input("Digite o número da opção escolhida:"))
                  if escolha == 1:
                    print("Vocês escolheu: Incluir")
                    incluir_estudantes()
                  elif escolha == 2:
                    print("Vocês escolheu: Listar")
                    listar_estudantes()
                  elif escolha == 3:
                    print("Você escolheu: Atualizar")
                    editar_estudante()
                  elif escolha == 4:
                    print("Você escolheu: Excluir")
                    excluir_estudante()
                    continue
                  elif escolha == 0:
                    print("Voltando ao menu principal")
                    break
                  else:
                    print("Escolha inválida, tente novamente.") 
