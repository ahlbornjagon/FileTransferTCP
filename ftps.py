"""

Jagon Ahlborn 
CSE 3461/5461
Dr. Adam Champion

The following code representings the server side of a TCP data transfer. We first initialize the local port to whatever is
passed in through the command line. We then create an address for the server and create a socket to use in TCP. We bind the 
new socket and listen for a signal from any client. After the client establishes a connection with the server, we recieve
the name, file size, and entirety of the transmitted file and save it off as a local copy. The TCP sockets are then closed. 

"""

import socket
import sys
import struct

# Initialize the local port to the argument passed in through the CLI
LOCAL_PORT = int(sys.argv[1])

# Set Server address
server_address = ('', LOCAL_PORT)

# Create a TCP socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the newly created socket to the server address
server_socket.bind(server_address)

# Listen for client connection
server_socket.listen(1)
print('Waiting for connections on port: ',LOCAL_PORT)

# Accept the connection fron the client
client_socket, client_address = server_socket.accept()
print('Accepted the connection from the following client: ', client_address)

#Execute while client_socket = true
with client_socket:
    print('Connected to client')
        # Recieve the first 4 bytes from the client (File Size), unpack as int
    fileSizeRaw = client_socket.recv(4)
    fileSize = struct.unpack('!I', fileSizeRaw)[0]
        
        # Recieve the next 20 bytes and strip empty trailing characters
    fileNameRaw = client_socket.recv(20)
    fileName = fileNameRaw.decode().rstrip('\0')

     # Start main data transfer, keep running total of size and conc data value
    recievedData = b''
    remainingData = fileSize
    while remainingData > 0:
        data = client_socket.recv(1024)
        recievedData += data
        remainingData -= len(data)
    with open(fileName, "wb") as f:
        f.write(recievedData)
    print("Data saved in file named: ", fileName)

    # Close both socket connections
    server_socket.close()
    client_socket.close()