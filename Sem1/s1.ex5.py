#Scrieti o functie care verifica daca un sir de caractere contine caractere speciale (\r, \t, \n, \a, \b, \f, \v)
sir="de	unde si cum 	"

def gaseste(sir):
	for c in sir:
		if c in '\r\t\n\a\b\f\v':
			return True
	return False

print gaseste(sir)

