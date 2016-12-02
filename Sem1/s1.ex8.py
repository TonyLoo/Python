polinom = "3y^3 + 56x^2 - 2x - 5"

def validare(polinom):
	i=0
	ok=0
	for i in range(0,len(polinom)):
		if polinom[i].isalpha():
			if(ok==0):
				x=polinom[i]
				ok=1
			elif(polinom[i] is not x):
			    #print "nu"
				return 0	
	return x
	#print "da"
	
print validare(polinom)

def evaluare(polinom,val):
    result=0
    x=validare(polinom)
	nr=0
	ok=1
	for i in range(0,len(polinom)):
		if polinom[i].isdigit():
			if ok==1:
				nr=nr*10+int(polinom[i])
				print nr
		elif polinom[i]=="*" and polinom[i+1]==x:
			if polinom[i+2]=="^":
			    result=result+nr+val**polinom[i+3]
				result=result+nr*val
		elif polinom[i]==x:
			result=result+nr*val
			
			 
	
			

evaluare(polinom,2)