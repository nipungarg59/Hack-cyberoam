import string

val = list(string.ascii_lowercase)

for i in range(0,10):
	val.append(str(i))

key =[0,0,0]
comb = []
total=0

while(key[0]!=35 or key[1]!=35 or key[2]!=35) :
	com=""
	alpha = False
	num   = False
	for i in key:
		com+=val[i]
		com+=val[i]
		if(i<=25):
			alpha = True
		if(i>25):
			num = True
	
	if not(key[0]==key[1] and key[1]==key[2]) and alpha :
		total+=1
		comb.append(com)
		ff = open("brt_pwd.dat","a")
		ff.write(com +"\n")
		ff.close()
		print total , com


	i=0
	while(key[i]==35):
		key[i]=0
		i+=1
	key[i]+=1
