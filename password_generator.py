#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
b = ''
for letter in range(0, nr_letters):
  b += str(random.choice(letters))
#print(b)
d = ''
for symbol in range(0,nr_symbols):
  d += str(random.choice(symbols))
#print(d)
e = ''
for number in range (0, nr_numbers):
  e += str(random.choice(numbers))

#print(e)
f = b + d + e
print(f"Here is your non-randomized password: {f}")
#Hard Level - Order of charact
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
g = [b , d, e]
h = ''
random.shuffle(g)
#print(g)
list_to_str = ''.join(map(str, g))
#print(list_to_str)
for ran in list_to_str:
  ran_seq = random.choice(list_to_str)
  h += ran_seq
print(f"Here is your randomized password: {h}")