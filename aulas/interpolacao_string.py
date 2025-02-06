'''
Interpolação básica de Strings

s - String
d e i - Int
f - Float
x e X - Hexadecimal

'''

nome = 'Jhon'
preco = 140.50
variavel = '%s, o preço é %.2f' % (nome, preco)
print(variavel)

print('O hexadecimal de %d é %08X' % (1424, 1424)) #O '08' serve para preencher o restante de 8 caracteres com 0, o 'X' maiúsculo retorna o Hexa em maiúsculo