'''
Cel mai mare divizor comun a mai multor numere 
(definiti o functie cu numar variabil de parametri 
care sa rezolve acest lucru)
'''
def functie(*numere):
	if len(numere)==1:
		return numere[0]
	elif 
		i=0
		x=cmmdc(numere[0],numere[1])
		while(i<len(numere)):
			x=cmmdc(numere[i],numere[i+1])
			i=i+1
			return x
	
def	cmmdc(a,b):
	r=a%b
	while(r!=0):
		a=b
		b=r
		r=a%b
	return b
			
	
print functie(10,40,90)
#sau apel recursiv de cmmdc(x,numere[2:]), unde x=cmmdc de primele 2 numere