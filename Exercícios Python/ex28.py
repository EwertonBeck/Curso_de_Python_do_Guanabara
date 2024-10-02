import random
import time

n1 = int(input('Em qual número eu estou pensando? '))
n2 = random.randint(0,5)


if n1 == n2:
    print('PROCESSANDO...')
    time.sleep(3)
    print(f'O numero que eu pensei foi {n2}.')
    print('Parabéns! vocÊ acertou!')
else:
    print('PROCESSANDO...')
    time.sleep(3)
    print(f'O numero que eu pensei foi {n2}.')
    print('Que pena, você errou!')