import socket
import os
import time 

#THIS IS A MALICIOUS PROJECT. ONCE COMPLETED PLEASE DO NOT OPEN ON YOU PERSONAL MACHINE 
#This is currently for a windows OS but I would like to change it to a Linux. This a majorly a test to see what we can learn from 
#how a virus like this works. 


Host = "0.0.0.0"
Port = 443
Max_Size = 1024 * 128

SEPERATOR = "<sep>"




s = socket.socket()

s.bind((Host,Port))

