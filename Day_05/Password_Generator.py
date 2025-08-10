import random

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','_']

print("Welcome to the PyPassword Generator!!!")
letter_choice=int(input("How many LETTERS would you like in your password? \n"))
numbers_choice=int(input("How many NUMBERS would you like in your password? \n"))
symbols_choice=int(input("How many SYMBOLS would you like in your password? \n"))
total_choice=letter_choice+numbers_choice+symbols_choice

'''#Easy way of generating password
easy_pass=""
for lett in range(letter_choice):
    easy_pass+=random.choice(letters)

for num in range(numbers_choice):
    easy_pass+=random.choice(numbers)

for sym in range(symbols_choice):
    easy_pass+=random.choice(symbols)
        
print(easy_pass)
'''
#Self Trying on the hard way of generating password
easy_pass=[]            
for lett in range(letter_choice):
    easy_pass.append(random.choice(letters))

for num in range(numbers_choice):
    easy_pass.append(random.choice(numbers))

for sym in range(symbols_choice):
    easy_pass.append(random.choice(symbols))
    

hard_pass=""
for hard in range(total_choice):
    hard_pass+=random.choice(easy_pass)
    
print("Your Password is: ",hard_pass)

#Dr. Angela Yu's method
'''
new_pass=[]            
for lett in range(letter_choice):
    new_pass.append(random.choice(letters))

for num in range(numbers_choice):
    new_pass.append(random.choice(numbers))

for sym in range(symbols_choice):
    new_pass.append(random.choice(symbols))
    
print(new_pass)
random.shuffle(new_pass)
print(new_pass)

password=""
for char in new_pass:
    password+=char
    
print(f"Your NEW password is: {password}")
'''         

