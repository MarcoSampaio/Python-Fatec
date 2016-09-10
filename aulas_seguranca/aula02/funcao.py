def ola():
    print 'Ola'
    
def somar(x,y):
    return x+y

ola()
print somar(8,7)

def dicionario():
    #um dicionario eh uma lista com indices nao necessariamente inteiros. nao eh possivel ter
    #uma lista como indice
    d={}
    d["Casa"]=9
    d[5]="wfjhbwrjfjrw"
    d[9.8]='i'
    print d
    
dicionario()