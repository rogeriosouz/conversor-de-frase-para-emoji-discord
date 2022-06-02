import os
os.system('cls')

print('-=-'*20)
print('{:^60}'.format('CONVERSOR DE FRASE PARA EMOJI DE LETRA DISCORD'))
print('-=-'*20)

frase = str(input('digite sua frase: '))
frase = frase.lower()

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

gifs = []


for letra in letras:
    gifs.append(f':regional_indicator_{letra}:')

contador = 0
nomes_gifs = []

for fra in frase:
    if 'a' in fra:
        nomes_gifs.append(fra.replace('a', gifs[0]))

    if 'b' in fra:
        nomes_gifs.append(fra.replace('b', gifs[1]))

    if 'c' in fra:
        nomes_gifs.append(fra.replace('c', gifs[2]))
    if 'd' in fra:
        nomes_gifs.append(fra.replace('d', gifs[3]))
    if 'e' in fra:
        nomes_gifs.append(fra.replace('e', gifs[4]))

    if 'f' in fra:
        nomes_gifs.append(fra.replace('f', gifs[5]))
    if 'g' in fra:
        nomes_gifs.append(fra.replace('g', gifs[6]))
    if 'h' in fra:
        nomes_gifs.append(fra.replace('h', gifs[7]))
    if 'i' in fra:
        nomes_gifs.append(fra.replace('i', gifs[8]))

    if 'j' in fra:
        nomes_gifs.append(fra.replace('j', gifs[9]))
    if 'k' in fra:
        nomes_gifs.append(fra.replace('k', gifs[10]))
    if 'l' in fra:
        nomes_gifs.append(fra.replace('l', gifs[11]))

    if 'm' in fra:
        nomes_gifs.append(fra.replace('m', gifs[12]))
    if 'n' in fra:
        nomes_gifs.append(fra.replace('n', gifs[13]))
    if 'o' in fra:
        nomes_gifs.append(fra.replace('o', gifs[14]))
    if 'p' in fra:
        nomes_gifs.append(fra.replace('p', gifs[15]))

    if 'q' in fra:
        nomes_gifs.append(fra.replace('q', gifs[16]))
    if 'r' in fra:
        nomes_gifs.append(fra.replace('r', gifs[17]))
    if 's' in fra:
        nomes_gifs.append(fra.replace('s', gifs[18]))
    if 't' in fra:
        nomes_gifs.append(fra.replace('t', gifs[19]))

    if 'u' in fra:
        nomes_gifs.append(fra.replace('u', gifs[20]))
    if 'v' in fra:
        nomes_gifs.append(fra.replace('v', gifs[21]))
    if 'w' in fra:
        nomes_gifs.append(fra.replace('w', gifs[22]))
    if 'x' in fra:
        nomes_gifs.append(fra.replace('x', gifs[23]))
    if 'y' in fra:
        nomes_gifs.append(fra.replace('y', gifs[24]))
    if 'z' in fra:
        nomes_gifs.append(fra.replace('z', gifs[25]))
    else:
        nomes_gifs.append(' ')


nome = ''.join(nomes_gifs).replace('  ', '   ')
print('-=-'*20, '\n')
print(nome, '\n')
print('-=-'*20)
