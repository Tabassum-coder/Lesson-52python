import random

char="abcdefghijklmnopqrstuvwxyz0123456789!@#$%"

length=int(input("Enter the length of password"))

password=[]

for i in range(length):
    password.append(random.choice(char))

password="".join(password)
print("your password is ",password)