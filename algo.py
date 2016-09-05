
listn = []
for i in range(1,10):
	listn.append(str(i))
listn.append('0')

listq = ['q' , 'w' , 'e' , 'r', 't', 'y', 'u', 'i', 'o' , 'p']
lista = ['a' , 's' , 'd' , 'f', 'g', 'h', 'j', 'k', 'l']
listz = ['z' , 'z' , 'x' , 'c', 'v', 'b', 'n', 'm', 'm']

def charsInX(x):
	y=""
	for i in range(0,6):
		if(i%2==0):
			y+=x[i]
	return y

def getind(x):
	if x in listn:
		return listn.index(x)
	elif x in listq:
		return listq.index(x)
	elif x in lista:
		return lista.index(x)
	elif x in listz:
		return listz.index(x)

def check(x):
	chars = charsInX(x)
	ind = []
	for i in chars:
		ind.append(getind(i))
	ind.sort()
	if(ind[2]-ind[0]<=2):
		return True
	else :
		return False

def pwds():
    data = open("pwd.dat","r").read()
    pwd = []
    for i in range(0,len(data)/7):
        s=""
        for j in range(6):
            s=s+data[i*7 + j]
        pwd.append(s)
    return pwd

if __name__ == '__main__':
	pwd = pwds()
	for i in pwd:
		print i , check(i)
