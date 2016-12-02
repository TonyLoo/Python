'''
Scrieti o functie care primeste un integer char_len si
un numar variabil de parametri (siruri de caractere) 
si verifica daca fiecare doua string-uri vecine respecta 
urmatoarea regula: al doilea string incepe cu ultimile 
char_len caractere a primului string (ca la fazan).
'''
def fazan(char_len,cv1,cv2):
	if cv2.startswith(cv1[-char_len:]):
		return True
	return False
	
def fazan_lista(char_len,*lista):
	for i in range(0,len(lista)-1):
	    if not fazan(char_len,lista[i],lista[i+1]):
			return False
	return True

print fazan_lista(3,'onyou','yourn','urna','aer')
print fazan_lista(3,'onyou','yourn','urna',)
