from Crypto.Cipher import DES
from Crypto.Cipher import AES
from Crypto import Random

key = 'OKOKOKOK'
#iv = Random.new().read(DES.block_size)
print AES.block_size
iv = 'ABCDEFGH'
cipher = DES.new(key, DES.MODE_CBC, iv)
#PARA O DES EH NECESSARIO STRINGS DE TAMANHO MULTIPLO DE 8
plaintext = 'SEGURANCA DA INF'
tc = cipher.encrypt(plaintext)
#MOSTRA O TEXTO CIFRADO EM HEXA
print tc.encode("hex")
#APENAS PARA O CBC A CADEIA DEVE SER REINICIADA
cipher = DES.new(key, DES.MODE_CBC, iv)
print cipher.decrypt(tc)

c=AES.new("0123456789ABCDEF",AES.MODE_CBC,iv+"ABCDEFGH")
tt=c.encrypt("SEGURANCA DA INF")
print tt.encode("hex")
c=AES.new("0123456789ABCDEF",AES.MODE_CBC,iv+"ABCDEFGH")
print c.decrypt(tt)from Crypto.Cipher import DES
from Crypto.Cipher import AES
from Crypto import Random

key = 'OKOKOKOK'
#iv = Random.new().read(DES.block_size)
print AES.block_size
iv = 'ABCDEFGH'
cipher = DES.new(key, DES.MODE_CBC, iv)
#PARA O DES EH NECESSARIO STRINGS DE TAMANHO MULTIPLO DE 8
plaintext = 'SEGURANCA DA INF'
tc = cipher.encrypt(plaintext)
#MOSTRA O TEXTO CIFRADO EM HEXA
print tc.encode("hex")
#APENAS PARA O CBC A CADEIA DEVE SER REINICIADA
cipher = DES.new(key, DES.MODE_CBC, iv)
print cipher.decrypt(tc)

c=AES.new("0123456789ABCDEF",AES.MODE_CBC,iv+"ABCDEFGH")
#A STRING DO AES DEVE SER MULTIPLA DE 16
tt=c.encrypt("SEGURANCA DA INF")
print tt.encode("hex")
#APENAS PARA O CBC A CADEIA DEVE SER REINICIADA
c=AES.new("0123456789ABCDEF",AES.MODE_CBC,iv+"ABCDEFGH")
print c.decrypt(tt)