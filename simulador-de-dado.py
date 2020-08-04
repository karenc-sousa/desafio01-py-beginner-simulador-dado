import random
#  desafio01-py-beginner-simulador-dado
answer = input('Se você quer jogar o dado, digite 1. Para sair, digite 2: ')

while True:
    try:
        if int(answer) == 1 and int(answer) != 2:        
            dice = random.randint(1,6)
            print(f'O número dessa rodada foi {dice}.')
            answer = input('Se você quer jogar o dado, digite 1. Para sair, digite 2: ')
    except:
        print('Digitação inválida.')
        answer = input('Se você quer jogar o dado, digite 1. Para sair, digite 2: ')
        continue
    if int(answer) == 2 and int(answer) != 1:
        print('Você saiu do jogo.')
        break
    elif int(answer) != 2 and int(answer) != 1:
        print('Digitação inválida.')
        answer = input('Se você quer jogar o dado, digite 1. Para sair, digite 2: ')
        continue
        