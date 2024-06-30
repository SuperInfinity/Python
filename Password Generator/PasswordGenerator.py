#Password Generator Project
import random as r
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password? : ")) 
nr_symbols = int(input("How many symbols would you like? : "))
nr_numbers = int(input("How many numbers would you like? : "))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

total_length = nr_letters + nr_numbers + nr_symbols
password = ""

while total_length > 0:
    ch = r.randint(0,2)
    if ch == 0 and nr_letters > 0:
        password += r.choice(letters)
        nr_letters -= 1
        total_length -= 1
    elif ch == 1 and nr_symbols > 0:
        password += r.choice(symbols)
        nr_symbols -= 1
        total_length -= 1
    elif ch == 2 and nr_numbers > 0:
        password += r.choice(numbers)
        nr_numbers -= 1
        total_length -= 1

print(password)