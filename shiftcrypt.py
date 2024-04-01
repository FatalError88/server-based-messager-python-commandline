def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            # Shift only alphabetical characters
            shifted_char = chr(((ord(char.lower()) - ord('a') + shift) % 26) + ord('a'))
            encrypted_text += shifted_char.upper() if char.isupper() else shifted_char
        else:
            # Keep non-alphabetical characters unchanged
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)
