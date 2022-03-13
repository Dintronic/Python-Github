def menu():

  voltarMenu = 's'

  while voltarMenu  == 's':
    opcao = input ('''
    
  ============================
        PROJETO AGENDA
  MENU:
  [1] CADASTRAR CONTATO
  [2] LISTAR CONTATO
  [3] DELETRAR CONTATO
  [4] BUSCAR CONTATO
  [5] SAIR
  ============================
  ESCOLHA UMA OPÇÃO: 

  ''')

    if opcao == "1":
      cadastrar()
    elif opcao == "2":
      listar()
    elif opcao == "3":
      deletar()
    elif opcao == "4":
      buscar()
    elif opcao == "5":
      sair()
    else:  
      print('OPÇÃO INVALIDA !!!')
      menu()

    voltarMenu = input("\nDeseja voltar ao menu principal? (s/n): ").lower()  #lower = tudo mainusculo
    

# ----FUNÇÃO CADASTRO DE CONTATO EM UM TXT------
def cadastrar():
  id = input("Escolha o ID: ")
  nome = input("Digite o Nome: ")
  tel = input("Digite o Numero do Telefone: ")
  mail = input("Digite o Email: ")

  try:
    agenda = open("agenda.txt","a")
    dados = f'{id};{nome};{tel};{mail} \n'
    agenda.write(dados)
    agenda.close()
    print(f'CONTATO GRAVADO COM SUCESSO !!!')
  except:
    print(f'ERRO NA GRAVAÇÃO DO CONTATO')


# -------FUNÇÃO LISTAR CONTATOS-------- 
def listar():
  agenda = open("agenda.txt","r")
  for contato in agenda:
    print(contato)
  agenda.close()


# -------FUNÇÃO BUSCAR CONTATOS-------- 
def buscar():
  nome = input(f'Digite o Nome: ').upper() #upper = tudo maiusculo 
  agenda = open("agenda.txt","r")
  for contato in agenda:
    if nome in contato.split(";")[1].upper(): #upper = tudo maiusculo 
      print(contato)
  agenda.close()


# -------FUNÇÃO DELETAR CONTATOS-------
def deletar():
  nome = input(f'Digite o Nome: ').upper() #upper = tudo maiusculo 
  agenda = open("agenda.txt","r")
  aux1 = []
  aux2 = []

  for i in agenda:
    aux1.append(i)

  for i in range(0, len(aux1)):
    if nome not in aux1[i].upper(): #upper = tudo maiusculo 
      aux2.append(aux1[i])
      
  agenda = open("agenda.txt","w") 

  for i in aux2:
    agenda.write(i)  

  print(f'Contato deletado com sucesso!!!')
  listar()


# -------FUNÇÃO SAIR DA AGENDA-------
def sair():
  print(f'Até Mais !!!')
  exit()


# -------FUNÇÃO INICIALIZAR MENU----- 
def main():
  menu()  

main()  