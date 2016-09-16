#this is client (raspberry pi with touch screen ) that control the car


import socket               

s = socket.socket()         
host ='10.8.13.236'                 # here I put the ip of the server's machine
port = 12345                

s.connect((host, port))

var = s.recv(1024)                  #receiving the max of 1024 character
print var                           
s.close()
