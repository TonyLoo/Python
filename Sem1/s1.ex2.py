#corect
string=raw_input("Datin un string: ")

string=string.lower()
nr=0;

for char in string:
	if char in 'aeiou':
		nr+=1
print nr
			
#sau
'''
vocale=['a','e','i','o','u']

for j in range (0,len(string)):
	for i in range(0,len(vocale)):
		if(string[j]==vocale[i]):
			nr=nr+1
'''


