# add your code here
def caesar_cipher_encrypt(text, shift=5):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Shift character and wrap around the alphabet
            offset = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            # Non-alphabetic characters are not changed
            encrypted_text += char
    return encrypted_text

# Get user input
user_text = input("Enter the text to encrypt: ")

# Encrypt the user's text
encrypted_text = caesar_cipher_encrypt(user_text)

# Output the encrypted text
print('The encrypted sentence is: ', encrypted_text)
