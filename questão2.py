import random
print("Olá, eu sou o PTP-3000.")
print("Vamos jogar pedra papel ou tesoura!")

jogadas_permitidas = ("pedra", "papel", "tesoura")
jogada_usuario = input("Digite pedra, papel ou tesoura \n").lower()
jogada_ptp = random.randint(0,2)

print(f"A sua jogada foi {jogada_usuario}")
print(f"A minha jogada foi {jogadas_permitidas[jogada_ptp]}")

#Possibilidades em que o usuário ganhou:
usuario_ganhou = jogada_usuario == "papel" and jogada_ptp==0 or jogada_usuario == "pedra" and jogada_ptp==2 or jogada_usuario == "tesoura" and jogada_ptp == 1
#Possibilidades que o usuário perde
usuario_perdeu = jogada_usuario == "papel" and jogada_ptp==2 or jogada_usuario == "pedra" and jogada_ptp==1 or jogada_usuario == "tesoura" and jogada_ptp == 0
#Empate
empate = jogada_usuario=="pedra" and jogada_ptp==0 or jogada_usuario=="papel" and jogada_ptp==1 or jogada_usuario=="tesoura" and jogada_ptp==2

if empate:
    print("Empatamos!")
elif usuario_ganhou:
    print("Parabéns! Você ganhou")
else:
    print("Eu ganhei!")

