# Adivinhar Numero
from random import randint # Puxa o Modulo
# ===
Numero_Aletatorio = randint(1, 9) # Lanca os numeros aletoriamente
print ("===>", Numero_Aletatorio) # Chuta na tela o valor aleatorio.
# ===
print ("\n")
nome = input("COMO SE CHAMA: \n")
user_digita = int(input("Digite um Numero: \n")) #User Digita o numero

tentativas = 1 # Contador

while True:
    if user_digita == Numero_Aletatorio:
        decisao = input ("Ola {} Acertaste no numero {}. Responda: [Continuar/Sair] ".format(nome, Numero_Aletatorio))
        if decisao == "c":
            N_aleatorio1 = randint(20,29)
            print("===>", N_aleatorio1)
            print("===> {} Os numeros variam agora de 20 a 29. ===> Boa sorte <===".format(nome))
            user_digita = int(input("Digite um Numero: \n")) #User Digita o numero
            tentativas += 1
            if user_digita == N_aleatorio1:
                print("===> Parabens, chegou ao fim do jogo.")
        break
    else:
        N_aleatorio2 = input("Nao acertou no numero. Deseja Continuar? [S/N]: ")
        if N_aleatorio2 == "s":
            user_digita = int(input("Digite um Numero: \n")) #User Digita o numero
            tentativas += 1
        else:
            print("Terminou o jogo: Tentou {} Vezes.".format(tentativas))
            break