#khaleed Ameen
import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'

number = input('Number of password? - ')
number = int(number)

length = input('Password length? - ')
length = int(length)

for p in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print"\a"    
    print(password)

raw_input("\n\nPress Enter Key To Exit.")