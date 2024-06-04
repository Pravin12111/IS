#write a program to encrypt messaging using key
def encrypt_message(message, key):
    encrypted_message = ""
    for i in range(len(message)):
        char = message[i]
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) + ord(key[i % len(key)].upper()) - 65) % 26 + 65)
            else:
                encrypted_char = chr((ord(char) + ord(key[i % len(key)].lower()) - 97) % 26 + 97)
        else:
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message

# Example usage
message = "Hello, World!"
key = "SECRET"
encrypted_message = encrypt_message(message, key)
print("Original message:", message)
print("Encrypted message:", encrypted_message)
