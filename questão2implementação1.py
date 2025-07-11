import random
print("\n\n\nOlá, eu sou o PTP-3000.")
nome_de_usuario = input("Qual o seu nome? ")
print(f"\nOlá {nome_de_usuario}!")
print("Vamos jogar pedra papel ou tesoura!\n")

jogar_novamente = "s"
while jogar_novamente == "s":
  jogadas_permitidas = ("pedra", "papel", "tesoura")
  jogada_usuario = input("Digite pedra, papel ou tesoura \n").lower()
  while novamente != "s" and novamente != "n":
      print("Você digitou algo errado! ):")
      novamente = input("Digite S ou N: ").lower()

  jogada_ptp = jogadas_permitidas[random.randint(0,2)]


  print(f"\nA sua jogada foi {jogada_usuario}")
  print(f"A minha jogada foi {jogada_ptp}\n")

  #Possibilidades em que o usuário ganhou:
  usuario_ganhou = jogada_usuario == "papel" and jogada_ptp==0 or jogada_usuario == "pedra" and jogada_ptp==2 or jogada_usuario == "tesoura" and jogada_ptp == 1
  #Possibilidades que o usuário perde
  usuario_perdeu = jogada_usuario == "papel" and jogada_ptp==2 or jogada_usuario == "pedra" and jogada_ptp==1 or jogada_usuario == "tesoura" and jogada_ptp == 0
  #Empate
  empate = jogada_usuario=="pedra" and jogada_ptp==0 or jogada_usuario=="papel" and jogada_ptp==1 or jogada_usuario=="tesoura" and jogada_ptp==2

  if empate:
    print("Empatamos!")
  elif usuario_ganhou:
    print("Parabéns! Você ganhou!")
  else:
    print("Eu ganhei!")

  novamente = input("\nDeseja jogar novamente? \nDigite S ou N: ").lower()
  while novamente != "s" and novamente != "n":
      print("Acho que você digitou algo errado! ):")
      novamente = input("Digite S ou N: ").lower()
  
  if novamente == "n":
    jogar_novamente="n"
  
print(f"Foi muito bom jogar com você {nome_de_usuario}!")
