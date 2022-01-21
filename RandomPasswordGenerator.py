import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_password = []

for let in range(0, nr_letters):
    random_letter = random.randint(0, (len(letters)-1))
    easy_password.append(letters[random_letter])

for sym in range(0, nr_symbols):
    random_symbol = random.randint(0, (len(symbols)-1))
    easy_password.append(symbols[random_symbol])

for num in range(0, nr_numbers):
    random_number = random.randint(0, (len(numbers)-1))
    easy_password.append(numbers[random_number])

combined_easy_password = "".join(easy_password)

print(f"Here is your easy password: {combined_easy_password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_password = []

for hard_let in range(0, nr_letters):
    random_letter = random.randint(0, (len(letters)-1))
    hard_password.append(letters[random_letter])

for hard_sym in range(0, nr_symbols):
    random_symbol = random.randint(0, (len(symbols)-1))
    hard_password.append(symbols[random_symbol])

for hard_num in range(0, nr_numbers):
    random_number = random.randint(0, (len(numbers)-1))
    hard_password.append(numbers[random_number])

combined_hard_password = ''.join(random.sample(hard_password,len(hard_password)))

#Syntax : random.sample(sequence, k)

#Parameters:
#sequence: Can be a list, tuple, string, or set. All values are retained.
#k: An Integer value, it specify the length of a sample.

#Returns: k length new list of elements chosen from the sequence.

print(f"Here is your hard password: {combined_hard_password}")
