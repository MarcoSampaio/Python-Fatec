arq=open('dados','r')
linhas = arq.readlines()
soma=0
for reg in linhas:
    regaux=reg.strip('\n')
    regaux=regaux.split(',')
    soma=soma+float(regaux[1])

print round(soma/len(linhas),2)

    