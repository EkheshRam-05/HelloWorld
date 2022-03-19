import random

source = "Hello World"
result=""

def StrGen():
	r=""
	for i in source:
		n=0
		char=""
		while(n<8):
			char+=f'{random.randint(0, 1)}'
			n+=1
		r+=chr(int(char, 2))
	return r

while (1):
	result = StrGen()
	print(result)
	if (result == source):
		print(result)
		break