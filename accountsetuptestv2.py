# Test for account creation - Bautista Estrada 16/05/2021
from sys import exit

print("Hello! Do you wish to create an account?")
print("Please answer with a Yes or a No.")

firstAnswer = input()
while True:                                 # I want to make it so that you have to input your answer again if it's not Yes or No
    if firstAnswer == "No" or firstAnswer == "no":
        print ("Understood. Goodbye!")
        exit()
        
    elif firstAnswer == "Yes" or firstAnswer == "yes":
        print("Great!")
        break
    elif firstAnswer != "Yes" or firstAnswer != "No" or firstAnswer != "no" or firstAnswer != "yes":
        print("Please answer with a Yes or a No.")
        print("Do you wish to create an account?")
        firstAnswer = input()
        continue

print("Please, type in your email address.")

emailAddress = input()

while True:
    if "@" not in emailAddress:
        print("Please make sure you've chosen a valid email address.")
        emailAddress = input()
        continue
    elif ".com" not in emailAddress:                              #Not sure how many domains there are other than .com
        print("Please make sure you've chosen a valid email address.")   
        emailAddress = input()
        continue
    else:
        print(f"Great! The email address you've chosen is {emailAddress}")
        break

print("Now choose a username, please.")

username = input()

while True:
    if "shit" in username or "fuck" in username or "dick" in username or "Fuck" in username or "Dick" in username or "Shit" in username: # No common profanities allowed
        print("Please make sure to not use any profanities when making your username.")
        print("Choose a username, please.")
        username = input()
        continue
    else:
        break

print(f"Great! Your username is {username}.")

print("Now, choose your password.")

print("Please make sure that your password is more than 8 characters long.")

password = input()

while True:
    if len(password) < 8:
        print("Please make sure that your password is more than 8 characters long.")
        print("Choose a password that is more than 8 characters long.")
        password = input()
        continue
    else:
        break

print("Now, please repeat your password.")

passwordRepeat = input()

while passwordRepeat != password:
    print("This password is not the same as the one you chose before.")
    print("Please make sure to type your password correctly.")
    print("Now, please repeat your password.")
    passwordRepeat = input()
    continue

print(f"Great! You've successfully set up your account! Your username is {username}, your password is {password}, and the email address you've chosen is {emailAddress}.")   
