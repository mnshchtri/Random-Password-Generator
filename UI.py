import secrets
import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create a label to display the password
password_label = tk.Label(window, text="Your password will be displayed here")

# Create a function to generate a password when the button is clicked
def generate_password():
    # Declare a list of characters to choose from
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=[]{};:,./<>?`~'

    # Use the secrets module to generate a secure random password
    password = ''.join(secrets.choice(chars) for i in range(30))

    # Update the label with the generated password
    password_label.config(text=password)

# Create a button to generate a password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)

# Add the label and button to the window
password_label.pack(pady=10)
generate_button.pack(pady=10)

# Start the main event loop
window.mainloop()
