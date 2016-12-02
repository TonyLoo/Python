'''
Scrieti o functie care returneaza numarul de cuvinte 
care exista intr-un string. Cuvintele sunt separate de spatii,
semne de punctuatie (, ;, ? ! . )
'''
string=raw_input("Dati un string: ")

for char in '?.!/;:':  
	string = string.replace(char,' ') 

string=string.split(" ")
nr=0
for cuvant in string:
	if cuvant:
		nr=nr+1

print nr
