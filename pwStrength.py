import string
import getpass

def checkPasswordStrength():
    password = getpass.getpass('Enter the password: ')
    strength = 0
    remarks = ''
    lowerCount = upperCount = numCount = wspaceCount = specialCount = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lowerCount += 1
        elif char in string.ascii_uppercase:
            upperCount += 1
        elif char in string.digits:
            numCount += 1
        elif char == ' ':
            wspaceCount += 1
        else:
            specialCount += 1
    
    if lowerCount >= 1:
        strength += 1

    if upperCount >= 1:
        strength += 1

    if numCount >= 1:
        strength += 1

    if wspaceCount >= 1:
        strength +=1

    if specialCount >= 1:
        strength += 1
    


    if strength == 1:
        remarks = ('That\'s a very bad password.'
                   'Change it as soon as possible!')
        
    elif strength == 2:
        remarks = ('That\'s a weak password'
                   'You should consider using a stronger password')
        
    elif strength == 3:
        remarks = ('Your password is okay, but it can be improved')

    elif strength == 4:
        remarks = ('Your password is hard to guess.'
                   'But you could make it even stronger')
        
    elif strength == 5:
        remarks = ('Now that\'s a STRONG password!!!'
                   'Hackers don\'t have a chance at guessing that one!')
    
    print('Your password has: ---')
    print(f'{lowerCount} lowercase letters')
    print(f'{upperCount} uppercount letters')
    print(f'{numCount} digits')
    print(f'{wspaceCount} whitespaces')
    print(f'{specialCount} special characters')
    print(f'Password Score: {strength / 5}')
    print(f'Remarks: {remarks}')


def checkPwd(another_pw=False):
    valid = False
    if another_pw:
        choice = input('Do you want to check another password\'s strength (y/n)')
    else:
        choice = input('Do you want to check your password\'s strength (y/n)')
    
    while not valid:
        if choice.lower() == 'y':
            return True
        elif choice.lower() =='n':
            print('Exiting...')
            return False
        else:
            print('Invalid input...please try again. \n')


if __name__ == '__main__':
    print('===== Welcome to Password Strength Checker =====')
    checkPw = checkPwd()
    while checkPw:
        checkPasswordStrength()
        checkPw = checkPwd(True)