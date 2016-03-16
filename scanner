from socket import *
from threading import *
import os

screenLock = Semaphore(value = 1)


class bcolors:
    OKBLUE = '\033[94m'
    BANNER = '\033[93m'
    WARNING = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'



common_ports = {
    "21": "FTP",
    "22": "SSH",
    "23": "Telnet",
    "25": "SMTP",
    "53": "DNS",
    "67": "DHCP",
    "80": "HTTP",
    "110": "POP3",
    "143": "IMAP",
    "194": "IRC",
    "443": "HTTPS",
    "465": "Cisco Protocol",
    "993": "IMAPS",
    "995": "POP3S",
    "3306": "MySQL",
    "25565": "Minecraft"
}

def vulcheck(banner):
    
    path = 'C:/Users/10030886/Documents/school/INFO3155/INFO3155 New/'
    #path = ''
    file = open(path+"vul-list.txt")
    for line in file.readlines():
        if(line.strip('\n') in banner):
            print "[+] " + line.strip('\n') + " " + "is vulnerable" 
    file.close

def getBanner(targetHost, targetPort):
    try:
        conn = socket(AF_INET, SOCK_STREAM)
        conn.connect((targetHost, int(targetPort)))
        try:
            #conn.send("HACKER")
            banner = conn.recv(1024)
        except:
            conn.send("HEAD / HTTP/1.0\r\n\r\n")
            banner = conn.recv(1024)
        return banner
    except:
        return

def scan(targetHost, targetPort):
    conn = socket(AF_INET, SOCK_STREAM)
    try:
        conn.connect((targetHost, int(targetPort)))
        banner = str(getBanner(targetHost, targetPort))
        screenLock.acquire()
        if str(targetPort) in common_ports:
            
            print "\n"          
            print "=" * 60
            print ("(+){}({}) is OPEN!".format(str(targetPort), common_ports[str(targetPort)]))
            #print "[+] "+ str(targetPort) + "/tcp open\n"
        else:
            print("(+){} is OPEN!".format(targetPort))
        print "\n"
        print "----------------Banner information-----------------\n"
        print banner
        vulcheck(banner)
        print "=" * 60
    except:
        #return
        screenLock.acquire()
        #print "[+] "+ str(targetPort) + "/tcp closed\n"
    finally:
	    screenLock.release()
	    conn.close()

def scanPort(targetHost, targetPorts):
    try:
        targetIp = gethostbyname(targetHost)
        print "\n" 
        print "*" * 60
        print "[+] scan result for: " + targetHost + ' ' + '@ IP address: ' + targetIp
        print "*" * 60
    except:
        print "[-] cannot resolve !! " + targetHost + ": Unknown Host"
        return
##    try:
##        targetName = gethostbyaddr(targetIp)
##        print "*" * 50
##        #print "\n[+] scan result for: " + targetName[0]
##    except:
##        print "\n[+] scan result for: " + targetHost + ' ' + '@ IP address: ' + targetIp 
    setdefaulttimeout(5)
    for targetPort in targetPorts:
        t = Thread(target=scan, args=(targetHost, int(targetPort)))
        t.start()

	
def main():
    targetHost = raw_input("Enter a remote host to scan: ")
    targetPort = raw_input("Enter a port or list of ports to scan: ")
    if "-" in str(targetPort):
        targetPorts = str(targetPort).split("-")
        targetPorts = range(int(targetPorts[0]), int(targetPorts[1])+1)
    elif "," in str(targetPort):
        targetPorts = str(targetPort).split(',')
        targetPorts = range(int(targetPorts[0]), int(targetPorts[1])+1)
    else:
        targetPorts = range(0, int(targetPort)+1)
        
    scanPort(targetHost, targetPorts)
	
if __name__ == '__main__':
    main()
