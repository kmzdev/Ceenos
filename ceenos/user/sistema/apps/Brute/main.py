import random

def desbloquear_palavra():
    palavra = "ovbhkfchcd"
    objetivo = "misterio"
    letras = "abcdefghijklmnopqrstuvwxyz"
    tentativa = palavra

    while tentativa != objetivo:
        tentativa = ''.join(random.choice(letras) for _ in range(len(palavra)))
        print(tentativa)
    
    print("Palavra desbloqueada!")
    print("Palavra:", tentativa)

desbloquear_palavra()
