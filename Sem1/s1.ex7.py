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
