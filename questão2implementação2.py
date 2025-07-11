import random
print("\n\n\nOlá, eu sou o PTP-3000.")
nome_do_usuario = input("Qual o seu nome? ")
print(f"\nOlá {nome_do_usuario}!")
print("Vamos jogar pedra papel ou tesoura!\n")

vitorias_do_usuario = 0
vitorias_do_ptp = 0
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
    print(f"Parabéns{nome_do_usuario}! Você ganhou!")
    vitorias_do_usuario = vitorias_do_usuario + 1
  else:
    print("Eu ganhei!")
    vitorias_do_ptp = vitorias_do_ptp + 1
  
  print("\n------Ranking-----")
  print(f"Suas Vitórias: {vitorias_do_usuario}")
  print(f"Minhas vitórias: {vitorias_do_ptp}")
  print("------------------")
  novamente = input("\nDeseja jogar novamente? \nDigite S ou N: ").lower()
  while novamente != "s" and novamente != "n":
      print("Acho que você digitou algo errado! ):")
      novamente = input("Digite S ou N: ").lower()
  
  if novamente == "n":
    jogar_novamente="n"
  
print(f"Foi muito bom jogar com você {nome_do_usuario}!")
