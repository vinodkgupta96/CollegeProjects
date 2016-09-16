#this is final code on raspberry for button with client code interacting with server (on car).
from Tkinter import *
import Tkinter							#import the tkinter package 
import sys
from sys import argv
import urllib
import socket               

import tkMessageBox
top=Tkinter.Tk()						#took tkinter object for further use 
def helloCallBack1():						#defined the function for each button
    #tkMessageBox.showinfo("Button Pressed","Increasing Speed")

#using socket send signal to car to machine with ip address host
	s = socket.socket()         				
	host ='192.168.43.227' # here I put the ip of the server's laptop
	port = 12345                

	s.connect((host, port))
	s.send('UP')
	
	s.close()



def helloCallBack2():
    #tkMessageBox.showinfo("Button Pressed","Moving Forward")
#using socket send signal to car to machine with ip address host
	s = socket.socket()         
	host ='192.168.43.227' # here I put the ip of the server's laptop
	port = 12345                

	s.connect((host, port))
	s.send('FORWARD')
	
	s.close()

def helloCallBack3():
    #tkMessageBox.showinfo("Button Pressed","Decreasing Speed")
#using socket send signal to car to machine with ip address host
	s = socket.socket()         
	host ='192.168.43.227' # here I put the ip of the server's laptop
	port = 12345                

	s.connect((host, port))
	s.send('DOWN')
	
	s.close()

def helloCallBack4():
    #tkMessageBox.showinfo("Button Pressed","Turning Left")
#using socket send signal to car to machine with ip address host
	s = socket.socket()         
	host ='192.168.43.227' # here I put the ip of the server's laptop
	port = 12345                

	s.connect((host, port))
	s.send('LEFT')
	
	s.close()

def helloCallBack5():
    #tkMessageBox.showinfo("Button Pressed","Stopping the Car")
#using socket send signal to car to machine with ip address host
	s = socket.socket()         
	host ='192.168.43.227' # here I put the ip of the server's laptop
	port = 12345                

	s.connect((host, port))
	s.send('STOP')
	
	s.close()

def helloCallBack6():
    #tkMessageBox.showinfo("Button Pressed","Turning Right")
#using socket send signal to car to machine with ip address host
	s = socket.socket()         
	host ='192.168.43.227' # here I put the ip of the server's laptop
	port = 12345                

	s.connect((host, port))
	s.send('RIGHT')
	
	s.close()

def helloCallBack7():
    #tkMessageBox.showinfo("Button Pressed","Blowing Horn")
#using socket send signal to car to machine with ip address host
	s = socket.socket()         
	host ='192.168.43.227' # here I put the ip of the server's laptop
	port = 12345                

	s.connect((host, port))
	s.send('HORN')
	
	s.close()

def helloCallBack8():
    #tkMessageBox.showinfo("Button Pressed","Moving Backward")
#using socket send signal to car to machine with ip address host
	s = socket.socket()         
	host ='192.168.43.227' # here I put the ip of the server's laptop
	port = 12345                

	s.connect((host, port))
	s.send('HORN')
	
	s.close()

#these are button configuration
b1 = Button(top,text="Speed UP",command=helloCallBack1,bg='orange',activebackground='white')
b1.config(height=9,width=30,padx=5)
b2 = Button(top,text="FORWARD",command=helloCallBack2,bg='green',activebackground='white')
b2.config(height=9,width=30,padx=5)
b3 = Button(top,text="Speed DOWN",command=helloCallBack3,bg='orange',activebackground='white')
b3.config(height=9,width=30,padx=5)
b4 = Button(top,text="LEFT",command=helloCallBack4,bg='pink',activebackground='white')
b4.config(height=8,width=30,padx=5)
b5 = Button(top,text="STOP",command=helloCallBack5,bg='white',activebackground='blue')
b5.config(height=8,width=30,padx=5)
b6 = Button(top,text="RIGHT",command=helloCallBack6,bg='pink',activebackground='white')
b6.config(height=8,width=30,padx=5)
b7 = Button(top,text="HORN",command=helloCallBack7,bg='yellow',activebackground='white')
b7.config(height=9,width=30,padx=5)
b8 = Button(top,text="BACKWARD",command=helloCallBack8,bg='red',activebackground='white')
b8.config(height=9,width=30,padx=5)
b9 = Button(top,text="HORN",command=helloCallBack7,bg='yellow',activebackground='white')
b9.config(height=9,width=30,padx=5)

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

top.mainloop()
