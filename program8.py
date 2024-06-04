#Vwrite a program to decryption of message using key
def decrypt_message(encrypted_message, key):
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr((ord(char) - ord(key[i % len(key)].upper()) + 65) % 26 + 65)
            else:
                decrypted_char = chr((ord(char) - ord(key[i % len(key)].lower()) + 97) % 26 + 97)
        else:
            decrypted_char = char
        decrypted_message += decrypted_char
    return decrypted_message

# Example usage
encrypted_message = "Iqnlz, Xpsme!"
key = "SECRET"
decrypted_message = decrypt_message(encrypted_message, key)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)
