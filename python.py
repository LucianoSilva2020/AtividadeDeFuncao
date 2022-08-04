nome = input('Digite seu nome:')

def ContaVogais(NovoNome):
    for letra in NovoNome:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            print(letra)
        elif letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':    
            print(letra)
        else:
            print('')
ContaVogais(nome)