import string
import pickle

encmsg=list()
privatekey=list()
numsg=list()
plain=list()

msgfile=input('Podaj nazwe pliku, ktory chcesz odkodowac: ')
privatekeyfile=input('Podaj nazwe klucza, ktorego chcesz uzyc do odszyfrowania pliku: ')
outfile=str(input('Podaj nazwe pliku wynikowego: '))

with open(privatekeyfile,'r') as datafile:
	for line in datafile:
		privatekey.append(line)

d=int(privatekey[0])
n=int(privatekey[1])

encmsg=pickle.load(open(msgfile,'rb'))

for member in encmsg:
	t=pow(member,d,n)
	numsg.append(t)

for member in numsg:
	tmp=chr(member)
	plain.append(tmp)

f=open(outfile, mode='wt', encoding='utf-8')
for member in plain:
	f.write(member)
f.close()



