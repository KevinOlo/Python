def strength(pwd):
    strength = 0
    long = len(pwd)

    if any(char.islower() for char in pwd) and any(char.isupper() for char in pwd):
        strength+=4
     
    special = any(char for char in pwd if not char.isalnum())
    
    if special == True:
        strength+=4

    if long>=16:
        strength+=4
    elif long<16 and long>=8:
        strength+=2
    else:
        exit

    if strength<=2:
        print('Very Weak Password')
        return
    
    if strength<=4:
        print(' Weak Password')
        return

    if strength<=6:
        print('Almost Average Password')
        return
        
    if strength<=8:
        print('Average Password')
        return
    
    if strength<=10:
        print('Strong Password')
        return
    
    if strength>10:
        print('Very Strong Password')
        return


while True:

    passw = input('what''s your password, or enter ''exit'' to exit:  ')

    if passw != 'exit':
        strength(passw)
    else:
        break
    
