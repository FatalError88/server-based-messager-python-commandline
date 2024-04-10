import socket
import shiftcrypt as crypt
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
    unencrypteddata = f"{info},{sender},{USER}"
    #encrypt the data being sent to the server
    data = crypt.caesar_encrypt(unencrypteddata,9)
    print(data)
    #send the encrypted data
    s.send(data.encode('utf-8'))

    # Close the connection
    s.close()
    













socket.error("arg")

if __name__ == "__main__":
    while True:
        Input = input("chat: ")
        try:(
        send_data(Input, 'Client', USER)
        )
        except Exception as err:
            print (err)
            print("also called server does not exist or:server crashed OR:you have no internet")
            exit()

