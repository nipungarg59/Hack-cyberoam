from sys import argv, exit
from urllib import urlencode
from urllib2 import urlopen

BASE_URL = "http://172.16.68.6:8090/login.xml"

def send_request(request_type, *arg):
    if(request_type == 'login'):
        print "Initialting login request for USERNAME: %s" % arg[0]
        params = urlencode({'mode': 191, 'username': arg[0], 'password': arg[1]})
    elif(request_type == 'logout'):
        print "Initiating logout request.."
        params = urlencode({'mode': 193, 'username': arg[0]})
    while True:
        try:
            response = urlopen(BASE_URL, params)
            break
        except Exception, e:
            print "Time_out Accepted"
    return response.read()

if __name__ == '__main__':
	data = send_request(str(argv[3]),str(argv[1]),str(argv[2]))
	if "into" in data:
		print "Exist"
	else :
		print "Don't Exist"