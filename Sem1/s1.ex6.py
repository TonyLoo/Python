'''Scrieti o functie care converteste in sir de caractere 
scris UpperCamelCase in lowercase_with_underscores.
'''
string="haiSaVerificam"

new=string
for i in range(0,len(string)):
	if string[i].isupper():
		new=new.replace(string[i],"_"+string[i].lower())

print new