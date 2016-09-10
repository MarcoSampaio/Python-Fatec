arq=open('dados','r')
linhas = arq.readlines()
for reg in linhas:
    print reg.strip('\n')