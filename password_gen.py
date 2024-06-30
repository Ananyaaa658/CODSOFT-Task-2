import random
import string
length = int(input("Enter the desired length of password:"))
#the password might contain A-Z, a-z,0-9,symbols
#we'll create a list which will contain all the possible characters

val=string.ascii_letters+string.digits+string.punctuation

password=""
for i in range(length):
    password+=random.choice(val)
print("The password is: ", password)
