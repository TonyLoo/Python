#corect
string=raw_input("Dati un string: ")

for char in '?.!/;:':  
	string = string.replace(char,' ') 

string=string.split(" ")
nr=0
for cuvant in string:
	if cuvant:
		nr=nr+1

print nr
