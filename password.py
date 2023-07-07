import secrets
import string
from cryptography import fernet

print("<-------------------------------------------------Welcome to Password Generator 2.0------------------------------------>")

service = str(input("For which service do you require Password: "))

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars


#password length

pwd_length = int(input("How many characters password you require: "))
pwd = ''

for i in range(pwd_length):
  pwd += ''.join(secrets.choice(alphabet))
  key = fernet.Fernet.generate_key()

fernet = fernet.Fernet(key)

print("Your password for " + service + " is " + pwd)
encMessage = fernet.encrypt(pwd.encode())

with open('passwordata.txt', 'a') as f:
  f.write('Password required for: ' + service + '\n')

with open('passwordata.txt', 'a') as f:
    f.write('Password: ' + pwd + '\n')
        
with open('passwordata.txt', 'a') as f:
    f.write('\n')