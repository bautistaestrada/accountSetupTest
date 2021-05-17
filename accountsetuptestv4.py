# Test for account creation - Bautista Estrada 16/05/2021
from sys import exit

firstAnswer = input("""Hello! Do you wish to create an account?
Please answer with a Yes or a No.
""")

firstAnswerNo = firstAnswer.strip().lower()

firstAnswerYes = firstAnswer.strip().lower()

replyIfAnswerNotValid = """That wasn't a Yes or a No. 
Please answer with a Yes or a No.
Do you wish to create an account? 
"""


while True:                                 # I want to make it so that you have to input your answer again if it's not Yes or No
    if firstAnswerNo == "no":
        print ("Understood. Goodbye!")
        exit()
        
    elif firstAnswerYes == "yes":
        print("Great!")
        break
    else:
        firstAnswer = input(replyIfAnswerNotValid)
        firstAnswerNo = firstAnswer.strip().lower()
        firstAnswerYes = firstAnswer.strip().lower()
        continue
        

print("Please, type in your email address.")

emailAddress = input()

emailAddressNotValid = """Please make sure you've chosen a valid email address.
"""

while True:
    if "@" not in emailAddress:
        emailAddress = input(emailAddressNotValid)     
    elif ".com" not in emailAddress:                              #Not sure how many domains there are other than .com  
        emailAddress = input(emailAddressNotValid)
    else:
        print(f"Great! The email address you've chosen is {emailAddress}")
        break

print("Now choose a username, please.")

username = input()

while True:
    if any(word in username.lower() for word in ("shit", "fuck", "dick")): # No common profanities allowed
        print("Please make sure to not use any profanities when making your username.")
        print("Choose a username, please.")
        username = input()
        
    else:
        break

print(f"Great! Your username is {username}")


password = input("""Now, choose your password.
Please make sure that your password is more than 8 characters long. 
""")

passwordNotValid = print("""Your password is less than 8 characters long.""")

while True:
    if len(password) < 8:
        passwordNotValid
        password = input("""Choose a password that is at least 8 characters long.
""")       
    else:
        break

passwordRepeat = input("""Now, please repeat your password.
""")

passwordRepeatNotValid = print("""This password is not the same as the one you chose before.""")

while passwordRepeat != password:
    passwordRepeatNotValid
    passwordRepeat = input("""Type the password again, and make sure you typed it correctly. 
""")
    

print(f"Great! You've successfully set up your account! Your username is {username}, your password is {password}, and the email address you've chosen is {emailAddress}.")   


