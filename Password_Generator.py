import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
print("How many letters would you like in your password?")
nr_letters = int(input("> "))
print("How many symbols would you like?")
nr_symbols = int(input("> "))
print("How many numbers would you like?")
nr_numbers = int(input("> "))

password_list = []
for i in range(0,nr_letters):
    password_list.append(random.choice(letters))

for i in range(0,nr_symbols):
    password_list.append(random.choice(symbols))

for i in range(0,nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for i in password_list:
    password += i

print(f" Your password is {password}")
