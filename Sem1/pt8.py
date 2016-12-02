import re
text="3x^4 +  7x^2 - 5x - 4"
#print re.findall(r'\([-]\d+\)',text)
lista=text.split('x')
print lista
result=0
for i in range(0,len(lista)):
	try: 
		float(lista[i])
		print "un float"
		print lista[i]	
	except ValueError:
		if(lista[i][0]=='^'):
			lista2=lista[i].split('+')
			print "aici: \n"
			print lista2
		    
	    
	
