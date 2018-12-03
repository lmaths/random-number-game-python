from random import randint
print('BEM VINDO')
sorteado = randint(1,10)
chute=0
while chute != sorteado:
    chute = int(input('Chute: '))
    if chute == sorteado:
        print('Você venceu')
    else:
        if chute > sorteado:
            print("Valor chutado foi muito alto")
        else:
            print("Valor chutado baixo")
            print('Fim do jogo!')
