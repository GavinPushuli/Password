import random
import string

def randomPassword():
    randomSource = string.ascii_letters + string.digits + string.punctuation
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password = random.choice(string.digits)
    password = random.choice(string.punctuation)
    
    for i in range(8):
        password +=random.choice(randomSource)
        
    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = ''.join(passwordList)
    return password

print("1st Random Password is: ", randomPassword())
print("2nd Random Password is: ", randomPassword())
print("3rd Random Password is: ", randomPassword())