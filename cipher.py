def caesar_cipher_encrypt(text, shift=5):
    encrypted_text = ""
    for char in text:                      
        if char.isalpha():
           encrypted_text += chr((ord(char.lower()) - 97 + shift) % 26 + 97)
        else:
            # Non-alphabetic characters are not changed
            encrypted_text += char
    return encrypted_text


user_text = input("Please enter a sentence: ")

# Encrypt the user's text
encrypted_text = caesar_cipher_encrypt(user_text)

# Output the encrypted text
print("The encrypted sentence is:", encrypted_text)
