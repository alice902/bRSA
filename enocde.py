import string
import pickle

numsg=list()
encmsg=list()
publickey=list()

msgfile=input('Podaj nazwe pliku, ktory chcesz zakodowac: ')
publickeyfile=input('Podaj nazwe klucza, ktorego chcesz uzyc do zaszyfrowania pliku [.pub]: ')
outfile=str(input('Podaj nazwe pliku wynikowego: '))

with open(publickeyfile,'r') as datafile:
	for line in datafile:
		publickey.append(line)

e=int(publickey[0])
n=int(publickey[1])

with open(msgfile,'r') as datafile:
	for c in datafile.read():
		tmp=ord(c)
		numsg.append(tmp)

for member in numsg:
	c=pow(member,e,n)
	encmsg.append(c)

pickle.dump(encmsg,open(outfile,'wb'))
