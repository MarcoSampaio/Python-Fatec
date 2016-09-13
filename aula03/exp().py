#EXERCICIO: Faca um programa em python para gerar 100 bits do exemplo 2(caderno).

def lfsr(x0,x1,x2,x3):
    x4 = 0
    while True: #loop infinito
        x4 = x1 ^ x2 ^ x0
        yield x4 #yield transforma a funcao em um gerador
        x0 = x1
        x1 = x2
        x2 = x3
        x3 = x4

g = lfsr(1,0,1,1) #1011 eh o SEED (chave) do algoritmo
aux =""

for i in range(100):
    aux = aux + str(g.next())
    
print aux #testar script no bash

