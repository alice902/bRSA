import random
import sys
import fractions
import gmpy


def FermatTest(a,p):
	probablyprime=pow(a,p-1,p)
	if probablyprime==1:
		return True
	else:
		return False

def MillerRabinTest(n, k):
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def EuclidForRelativePrime(p,keylength):	
	while True:	
		k=random.randrange(3,p-1)
		if fractions.gcd(p,k)==1:
				break
	return k

def ModInv(e,euler_function):
    d=gmpy.invert(e,euler_function)
    return d
	

def GenPrime(key_length):
	while True:
		p=random.getrandbits(key_length)
		if FermatTest(2,p)==True and MillerRabinTest(p,10)==True:
				break
	return p
	

key_length=int(input('Enter RSA key length [bits]:'))
private_key_file=input('Enter name for a new key pair: ')
public_key_file=str((private_key_file+'.pub'))
q=GenPrime(key_length)
r=GenPrime(key_length)
euler_function=(q-1)*(r-1)
n=q*r
e=EuclidForRelativePrime(euler_function,key_length)
d=ModInv(e,euler_function)
q=0
r=0

#public_key=(e,n)
#private_key=(d,n)

target1=open(private_key_file,'w')
target1.write(str(d))
target1.write('\n')
target1.write(str(n))

target=open(public_key_file,'w')
target.write(str(e))
target.write('\n')
target.write(str(n))
