import string
import random

s1 = string.ascii_letters
s2 = string.digits
s3 = string.punctuation
userLen = int(input("Enter password length: "))

s = list(s1)+list(s2)+list(s3)

# print(s)

random.shuffle(s)
print("Your password is: ")
print("".join(s[0:userLen]))