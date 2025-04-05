#Nome: Ana Flávia Maciel / Curso: Análise e desenvolvomento de sistemas 
 #Lista para estudantes
estudantes = []
invalid = "Essa opção ainda está em desenvolvimento"

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
  estudantes.append(nome)
  print(f"Estudante: {nome}, adicionado com sucesso!")
#Incluir estudante
def update_estudantes():
  numberS = input("Digite o número do estudante: ")
  number = int(numberS)
  upStudant = estudantes[number]
  nome = input("Digite o nome do estudante:")
  estudantes[number] = nome
  print(f"Estudante: {nome}, atualizado com sucesso!")
#Listar estudantes
def listar_estudantes():
    if not estudantes:
      print("Ainda não há estudantes cadastrados")  
      return
    print("Estudantes cadastrados:")
    print(estudantes)
#loop principal
while True:
        exibir_menu()
    #Coletar escolha do usuário
        escolha = int (input("Digite o número da opção escolhida:"))
        if escolha == 1:
          print("Você escolheu: Estudantes")
        elif escolha == 2:
          print(invalid)
          continue
        elif escolha == 3:
          print(invalid)
          continue
        elif escolha == 4:
          print(invalid)
          continue
        elif escolha == 5:
          print(invalid)
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
                    # print(invalid)
                    print("Vocês escolheu: Atualizar")
                    update_estudantes()
                    continue
                  elif escolha == 4:
                    print(invalid)
                    continue
                  elif escolha == 0:
                    print("Voltando ao menu principal")
                    break
                  else:
                    print("Escolha inválida, tente novamente.") 
