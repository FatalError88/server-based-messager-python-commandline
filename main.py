import socket
import datetime as t

sender = "client "
status = "INFO"
info = "test message"
e = False



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

# Example usage





def start_server():
    
    print("Starting Server...")
    # Create a socket object
    s = socket.socket()

    # Prompt the user to enter the port
    port = input("Enter server port to host the chat on: ")

    # Convert port to integer
    port = int(port)

    # Bind to the port
    s.bind(('', port))
    print("Binding to Port " + str(port) + "...")

    # Put the socket into listening mode
    s.listen(5)
    print("Putting Socket into listening mode...")
    print("Started Server")
    
    while True:
        # Establish a connection with the client
        c, addr = s.accept()
        

        # Receive data from the client
        crypteddata = c.recv(1024).decode('utf-8')
        print(crypteddata)
        data = caesar_decrypt(crypteddata,9)

        info, sender, USER = data.split(',')
        command_check(info)
        if info.startswith('/') != True:
            status = "CHAT"
            message = "[" + sender + " " + status + "] " + USER + ":" + info
            print(message)
            status = "INFO"


        # Close the connection with the client
        c.close()
def command_check(info):
    if info.startswith('/'):
        info = info.replace('/', '')
    else:
        return
    if info == "stop":
        print("stopping server...")
        exit(132)
    if info == "time":
        time = t.time()
        print(time)
    












if __name__ == "__main__":
    start_server()


