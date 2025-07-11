import random
print("----Pedra papel ou tesoura----\n")

jogar_novamente = "s"

while jogar_novamente == "s":
  jogadas_permitidas = ("pedra", "papel", "tesoura")
  jogada_usuario = input("Digite pedra, papel ou tesoura \n").lower()
  for i in jogadas_permitidas:
    if jogada_usuario not in jogadas_permitidas:
      print("\nVocê digitou errado")
      jogada_usuario = input("Digite pedra, papel ou tesoura \n").lower()

  jogada_computador = random.randint(0,2)

  print(f"\nA sua jogada foi {jogada_usuario}")
  print(f"A jogada do computador foi {jogadas_permitidas[jogada_computador]}\n")

  #Possibilidades em que o usuário ganhou:
  usuario_ganhou = jogada_usuario == "papel" and jogada_computador==0 or jogada_usuario == "pedra" and jogada_computador==2 or jogada_usuario == "tesoura" and jogada_computador == 1
  #Possibilidades que o usuário perde
  usuario_perdeu = jogada_usuario == "papel" and jogada_computador==2 or jogada_usuario == "pedra" and jogada_computador==1 or jogada_usuario == "tesoura" and jogada_computador == 0
  #Empate
  empate = jogada_usuario=="pedra" and jogada_computador==0 or jogada_usuario=="papel" and jogada_computador==1 or jogada_usuario=="tesoura" and jogada_computador==2

  if empate:
    print("Empate!")
  elif usuario_ganhou:
    print("Você ganhou!")
  else:
    print("Você perdeu")
  
  novamente = input("\nDeseja jogar novamente? \nDigite S ou N: ").lower()
  while novamente != "s" and novamente != "n":
      print("Você digitou algo errado! ):")
      novamente = input("Digite S ou N: ").lower()
  
  if novamente == "n":
    jogar_novamente="n"
