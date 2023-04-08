# Import the secrets module
import secrets

# Declare a list of characters to choose from
chars_1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=[]{};:,./<>?`~'
chars_2 = '0123456789'
# Use the secrets module to generate a secure random password
password = ''.join(secrets.choice(chars_1 + chars_2) for i in range(30))

# Print the generated password
print(password)
print("Boom! you got a  more secure password")
print("Update your Password in time.....")