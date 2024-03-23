import socket

# Define the server IP and port at the top of your script
IP = input("Enter server IP to connect to: ")
port = input("Enter server port to connect to: ")
USER = input("username:")

def send_data(info, sender, USER):
    # Create a socket object
    s = socket.socket()

    # Connect to the server on local computer
    s.connect((IP, int(port)))

    # Send data to the server
    data = f"{info},{sender},{USER}"
    s.send(data.encode('utf-8'))

    # Close the connection
    s.close()

if __name__ == "__main__":
    while True:
        Input = input("chat: ")
        send_data(Input, 'Client', USER)

