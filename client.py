import socket

# Define the server IP and port at the top of your script
IP = input("Enter server IP to connect to: ")
port = input("Enter server port to connect to: ")
USER = input("username:")
#encryptor
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


def send_data(info, sender, USER):
    # Create a socket object
    s = socket.socket()

    # Connect to the server on local computer
    s.connect((IP, int(port)))

    # Send data to the server
    unencrypteddata = f"{info},{sender},{USER}"
    #encrypt the data being sent to the server
    data = caesar_encrypt(unencrypteddata,9)
    print(data)
    #send the encrypted data
    s.send(data.encode('utf-8'))

    # Close the connection
    s.close()

















if __name__ == "__main__":
    while True:
        Input = input("chat: ")
        send_data(Input, 'Client', USER)


