import string
import random
def generate_password(length):
#Generate a random password of specified length using random module
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))
# Get password length from user
length=int(input('ENTER YOUR PASSWORD LENGTH:'))
# Generate and show first password
password=generate_password(length)
print('password:',password)
#  Change password button simulation

while True:
   try:
        change = input("Type 'change' for new password or 'exit' to quit: ")
        if change.lower() == 'change':
            new_password = generate_password(length)
            print("New Password:", new_password)
        elif change.lower() == 'exit':
            break
        else:
            print("Please type 'change' or 'exit'")
   except ValueError:
    print("Please enter a valid number")
          
  