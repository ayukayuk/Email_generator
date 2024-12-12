
import random
letters = ["a", "b", "c", "d", 'e', "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
number = ["1","2", "3", "4", "5", "6", "7","8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
symbol = ["@", "#", "$", "!", "*", "()", "+", "&", "%", "-", "/", "?", "|", "^", "/"]

print("welcome to Aycubepassword generator")
letters_w =int(input("how many letters do you want to input.\n"))
number_r = int(input("how many numbers for you want to put.\n"))
symbol_ty =int(input("how many symbols do you want to insert.\n"))
password =[]
for u in range(0, letters_w):
      password.append(random.choice(letters))
for u in range(0,number_r):
     password.append(random.choice(number))
for u in range(0, symbol_ty):
    password.append(random.choice(symbol))
    
    print(password)
    random.shuffle(password)
    print(password)

password_t =""
for u in password:
    password_t +=u
    
    print(f"your password is  {password_t}")