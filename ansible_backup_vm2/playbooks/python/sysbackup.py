



#!/usr/bin/env python
#import platform, subprocess, re
import sys
import os
import socket
import subprocess

print(' ')
print ('The IP Adddress Of Server is:') , socket.gethostbyname(socket.gethostname())
#print socket.gethostbyname(socket.gethostname())
print(' ')
print "The Hostname Of Server is:" ,  socket.gethostname()
#print socket.gethostname()
print(' ')
system = os.uname()
print "The Information Of System is:" , system
print(' ')
#print ("The os version is:")
#osver = os.system("cat /etc/redhat-release")
#osver = os.popen("cat /etc/redhat-release").read()
p = subprocess.Popen("cat /etc/redhat-release", stdout=subprocess.PIPE, shell=True)
(output , err) = p.communicate()
print "The Version Of Operating System is: ", output
kernel = subprocess.Popen("uname -r", stdout=subprocess.PIPE, shell=True)
(output , err) = kernel.communicate()
print "The Kernel Version Of Server is: ", output
#print(' ')
#print "The Status Of Memory is:"
#space = os.system("free -m")
#print "The Status Of Memory is:"
mem = subprocess.Popen("free -m", stdout=subprocess.PIPE, shell=True)
(output , err) = mem.communicate()
print "The Status Of mem is: ", output

print(' ')
#print "The CPU Status Of Server is:"
#cpu = os.system("inxi -C")

cpu = subprocess.Popen("inxi -C", stdout=subprocess.PIPE, shell=True)
(output , err) = cpu.communicate()
print "The Status Of CPU is: ", output


