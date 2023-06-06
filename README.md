*************************************

Name: Jagon Ahlborn 

*************************************

**About**

This project is a client to server tcp file transfer application that, once started, will transfer a given file from the server machine to the client depending on the input provided by the user. 

**Instructions**

1. Run the following commands one at a time on the server machine to get the host name and and IP address. Record these values. 

    `% hostname`

    `% /sbin/ifconfig | grep 'inet 10'`

2. Run the same commands on the client machine same as in step 1, record the host name and IP address. 

3. Run the following command on the server machine to enable it, using any local port. 

    `% python3 ftps.py <local-port-on-System-2>`

4. Start the client side of the application on the client machine with the following command, using the IP address of the server machine found in step 1, the port number used in the command on step 3, and the name of the local file to transfer to the server. 

    `% python3 ftpc.py <remote-IP-on-System-2><remote-port-on-System-2><local-file-to-transfer>`
