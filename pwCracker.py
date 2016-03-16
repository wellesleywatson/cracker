# -*- coding: utf-8 -*-
import crypt
import sys
print sys.argv
import os

def testPass(cryptPass, dictionary):
    salt = cryptPass[0:2]
    dictFile = open(dictionary,'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word,salt)
        if (cryptWord == cryptPass):
            print "[◕ ‿ ◕] Found Password: "+word+"\n"
            return
    print "[@_@] Password Not Found.\n"
    return
    
def main():
    #passwords.txt
    pFile = raw_input("\nPlease enter password file path: ")
    for file in os.listdir(os.getcwd()):
        if file.endswith(".txt"):
            if file.startswith("dictionary"):
                print(file)
    passFile = open(pFile)
    ##dictionary1.txt
    dictionary = raw_input("\nPlease select a dictionary file from above: ")
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print "[*] Cracking Password For: "+user
            testPass(cryptPass, dictionary)
            
       
if __name__ == "__main__":
    main()
 
