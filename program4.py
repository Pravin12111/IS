#program to create cryptanalytic in information security
def cryptanalysis_attack(ciphertext, key):
    # Initialize the plaintext
    plaintext = ""

    # Iterate through the ciphertext
    for i in range(len(ciphertext)):
        # Calculate the index of the plaintext character
        index = (i + key) % 26

        # Append the plaintext character to the plaintext
        plaintext += chr(ord('A') + index)

    return plaintext

# Example usage
ciphertext = "GUR PENML XRL VF ZL FRPERG CBFG"
key = 3

plaintext = cryptanalysis_attack(ciphertext, key)
print("Plaintext:", plaintext)
