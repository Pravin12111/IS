#write a program to create text message to hex in information security
def text_to_hex(text):
    hex_text = ""
    for char in text:
        hex_text += hex(ord(char))[2:]
    return hex_text

# Example usage
text = "Hello, World!"
hex_text = text_to_hex(text)
print("Text:", text)
print("Hex:", hex_text)

