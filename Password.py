# Import the secrets module
import secrets

# Declare a list of characters to choose from
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=[]{};:,./<>?`~'

# Use the secrets module to generate a secure random password
password = ''.join(secrets.choice(chars) for i in range(10))

# Print the generated password
print(password)