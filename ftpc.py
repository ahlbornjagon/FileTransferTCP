
"""

Jagon Ahlborn 
CSE 3461/5461
Dr. Adam Champion

The following code representings the client side of a TCP data transfer. The CL provided server IP and port, and the local file
to be sent are assigned to local variables first. Next a socket is opened up for the client, connecting it to the server. 
Using a typical while loop, we send the fileSize, fileName, and then the contents of the provided local file. This is done in 
binary format, in network byte order. The sockets are then closed once the data transfer is complete

"""

import socket
import sys
import struct

# Initialize the vairables passed via CLI
remoteIP = sys.argv[1]
remotePort = sys.argv[2]
localFile = sys.argv[3]

# Create a TCP socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((remoteIP, int(remotePort)))

# Open binary file
with open(localFile, "rb") as f:
    fileSize = len(f.read())
    f.seek(0)

    # Convert File size to 4 bytes network byte order
    fileSizeRaw = struct.pack("!I", fileSize)

    client_socket.sendall(fileSizeRaw)

    # Encode and send the file name, first 20 bytes with no trailing characters
    fileNameRaw = localFile.encode().ljust(20, b'\0')
    client_socket.sendall(fileNameRaw)

    # Send chunks of data over TCP 
    size = 1024
    bytesLeft = fileSize
    while bytesLeft > 0:
        data = f.read(size)
        client_socket.sendall(data)
        bytesLeft -= len(data)
print("Finished sending file", localFile)

client_socket.close()

