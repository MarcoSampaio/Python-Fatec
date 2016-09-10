def contar(pal):
    #esse dicionario possuira como indice as letras da palavra pal e como valor a quantidade de frequencia
    d={}
    for letra in pal:
        if letra in d:
            d[letra]=d[letra]+1
        else:
            d[letra]=1
    
    print d

contar("araraquara")

#para casa
#faca uma funcao toDict(a,b) que receba duas strings a,b e retorne um dicionario contendo o seguinte:
#toDict("sol","lua")={'s':'l','o':'u','l':'a'}
