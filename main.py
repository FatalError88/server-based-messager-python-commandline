import datetime
import socket
sender = "client "
status = "INFO"
info = "test message"
def start_server():
    # Create a socket object
    s = socket.socket()

    # Prompt the user to enter the port
    port = input("Enter server port to host the chat on: ")

    # Convert port to integer
    port = int(port)

    # Bind to the port
    s.bind(('', port))

    # Put the socket into listening mode
    s.listen(5)
    print("Server is listening")

    while True:
        # Establish a connection with the client
        c, addr = s.accept()
        print("Got connection from", addr)

        # Receive data from the client
        data = c.recv(1024).decode('utf-8')
        print("Received data:", data)

        info, sender, USER = data.split(',')
        


        # Close the connection with the client
        c.close()
















x = datetime.datetime.now()














message = "[" + sender + status + "] " + info
print(message)





if __name__ == "__main__":
    start_server()


