'''
Fatiamento de Strings

 012345678 -> Indice (começa em 0)
 Olá mundo
-987654321 -> Indice negativo (termina em 1)

 Fatiamento [i:f:p] -> [::]

 Sendo:

 i -> Inicio
 f -> Final
 p -> Passo

 Obs.: a função len retorna a qtd de caracteres da str
'''

variavel = 'Olá mundo'
print(variavel[0:6]) #O passo por padrão é 1, podendo ser negativo (neste caso, inverte a ordem)

'''
 Exercicio
 
 Peça ao usuário para digitar seu nome
 Peça para o usuário digitar sua idade

 Se nome e idade foram digitados:

    Exiba:

        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}

    Se nada for digitado em nome ou idade:
        Exiba: "Desculpe, você deixou campos vazios."
'''

nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")

if len(nome) == 0 or len(idade) == 0:
    print("Desculpe, você deixou campos vazios.")
else:
    print(f"Seu nome é {nome}")
    print(f'Seu nome invertido é {nome[::-1]}')
    if " " in nome:
        print('Seu nome contém espaço')
    else:
        print('Seu nome não contém espaço')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0:1]}')
    print(f'A última letra do seu nome é {nome[len(nome)-1:]}')
        