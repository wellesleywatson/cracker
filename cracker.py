import os
import crypt
from datetime import datetime

#Time Stamp
time_stamp = datetime.now()

def passCracker(passcrypt, user):
    salt = passcrypt[0:2]
    dictionary = open('dictionary1.txt','r')
    for word in dictionary.readlines():
        word=word.strip('\n')
        wordcrypt = crypt.crypt(word,salt)
        if (wordcrypt == passcrypt):
            print 'Success! ' + user + "'s password was cracked."
            print user + "'s password is: " + word 
            return
    print user + "'s password could not be cracked."
    return

def main():
    passDoc = open('passwords.txt')
    for line in passDoc.readlines():
        if ':' in line:
            user = line.split(':')[0]
            passcrypt = line.split(':')[1].strip(' ')
            print "[*][*][*]Cracking Password for user: " + user + " [*][*][*]"
            passCracker(passcrypt, user)

if __name__ == '__main__':
    main()
