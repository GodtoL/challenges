import random
import string

def generatepassword():
    password = ""
    lenght = random.randint(8, 16)
    character_list= (string.ascii_letters + string.digits + string.punctuation)
    
    while lenght > 0:
        character = random.choice(character_list)
        password = password + character
        lenght -= 1
    
    print(password)
    

generatepassword()