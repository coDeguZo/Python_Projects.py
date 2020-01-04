# Random Password Generator CHOICE

import random
import string #Or import random, string 

print("Password should a length of 6 characters!")

def passwordgen():
    count = []
    for letter in range(c):
        a1 = random.choice(string.as_uppercase)
        a2 = random.choice(string.ascii_lowercase)
        a = random.choice([a1, a2])
        count.append(a)
    for num in range(n):
        b1 = random.randint(0, 9)
        b2 = random.choice(string.punctuation)
        b = random.choice([b1, b2])
        count.append(b)
    random.shuffle(count)
    return count

while True:
    l = int(input("How long should the password be?: "))
    c = int(input("How many charecters?: "))
    n = int(input("How many numbers?: "))

    if l >= 6:
        if ((n + c) == l):
            result = passwordgen()
            print(*result)
            break
        else:
            print("Sorry the total of characters and numbers exceeds the password length.  The password length = 6")
    else:
        print("Sorry the password should be atleast 6 charecters long")


''' Random password Generator no CHOICE

import random
import string #Or import random, string

length_of_password = 6
start = 0
stop = 7
password = ""

for i in range(length_of_password):
    x = random.randrange(7)
    character = chr(random.randrange(97, 97 + 26))
    choice = [str(x), character.upper(), character.lower()]
    pass_pos = random.choice(choice)
    password = password+pass_pos

print(password)'''