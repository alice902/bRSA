import string
import pickle

encmsg=list()
privatekey=list()
numsg=list()
plain=list()

msgfile=input('Enter filename you want to decode: ')
privatekeyfile=input('Enter key you want to use to decode the file: ')
outfile=str(input('Enter output filename: '))

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



