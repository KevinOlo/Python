#stores pwd w username/ acc its assoc w but pwd must be encrypt

#not secure pwd encrypt dont use  master pwd 4 decrypt


#take string of text and using key turn torandom text that cant be decrypt w/o key
from cryptography.fernet import Fernet 

#key + pwd + txt = encrypted txt
#encrypt txt + pwd + key = decrypt txt

def writekey():                         # ''' ( ' x3) = multi line coment (like java)
    key = Fernet.generate_key()             #Key generation
    with open ('key.key', 'wb') as keyf:   #wb means write bytes mode
        keyf.write(key)                     #store key in file


def loadkey():
    with open('key.key', 'rb') as keyf:             # rb = read bytes mode
        key = keyf.read()                               #reading file to get key, decrypt purpose
        return key

def view():
    with open ('passwordpwdmgr.txt', 'r') as f :        # Open file
        for line in f.readlines():                      #traverse file by line 
            data = (line.rstrip())                      #print line ----- Also reads \n in added in file need 2 strip w r strip remove trailing chars
            user, pwd = data.split('|')
            print( 'User: ', user, '|| Password: ', fer.decrypt(pwd.encode()).decode())



def add():
    name = input('account name: ')
    pwd = input('Password: ')

    #open txt file auto close file
    with open('passwordpwdmgr.txt', 'a') as f :
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + '\n')          #add ECRYPTED pwd to file on new lines 

   #encode pwd turns it 2 bytes
   #decode turns bytes str to regular str





#pwd = input('whats the master password? '), implementation requires additional configs w/ Fernet

#writekey()                                      #only need to run cmd once to get key val generated into file

key = loadkey() #+ pwd.encode                     #convert master str pwd to bytes to allow arithmetic to be done ---- pwd.bytes or bytes(pwd) , pwd is not a part of the key
fer = Fernet(key)                               #initialize encryption module


while True:
    mode= input('would you like to add a new password, or view your existing ones (view, add) press, q to Quit:\t').lower()

    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else: 
        print('Invalid mode, please try again. ')
        continue

# b 'hello' == bytes str
