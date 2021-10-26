from random import randint

print('=========================')
print('~~~~Adivinhe o número~~~~')
numero_ate = randint(0, 10)
print('Acabei de pensar em um numero, entre 0 e 10...')
print('Qual numero eu acabei de pensar??...')
numero = False
palpites = 0
while not numero:
    jogador = int(input('Qual numero eu pensei? '))
    palpites += 1
    if jogador == numero_ate:
        numero = True
    else:
        if jogador < numero_ate:
            print('Chutou muito a baixo, tente de novo..')
        elif jogador > numero_ate:
            print('Chutou muito alto, tente mais uma vez')
print('Você acertou, com {} tentativas. Parabéns!!'.format(palpites))

