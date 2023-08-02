from password_strength import PasswordPolicy

Policy = PasswordPolicy.from_names(
    length = 10,
    special = 1,
    uppercase = 1,
    numbers = 1
)

#password= (input('what is your password?    '))


while True:
    unmet = Policy.test(input('what is your password?    '))

    if len(unmet) == 0:
        print('Your password is secure')
        break
    else:
        print('That password is unsecure, try again. \n The requirements you haven''t met are as follows: ' + str(unmet))
        

