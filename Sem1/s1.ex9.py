'''
Scrieti o functie care sa returneze cel mai mare numar prim 
dintr-un sir de caractere dat ca parametru sau -1 daca sirul
de caractere nu contine nici un numar prim. 
Exemplu: 
input: 'ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda'; 
output: 271
'''
import re
import math

sir='ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda'
numere=re.findall(r'\d+',sir)
print numere

def eprim(nr):
	if nr<=1: return False
	elif nr==2: return True
	else:
		i=2
		while (i<math.sqrt(nr)):
			if (nr%i)==0: return False
			i=i+1
		return True
	
nr_prime=[]
for i in numere:
	if eprim(int(i)):
		nr_prime.append(int(i))
		
print max(nr_prime)
		


