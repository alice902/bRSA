import string
import pickle

numsg=list()
encmsg=list()
publickey=list()

msgfile=input('Enter filename you want to encode: ')
publickeyfile=input('Enter key name you want to use to encode the file [.pub]: ')
outfile=str(input('Enter output filename: '))

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
