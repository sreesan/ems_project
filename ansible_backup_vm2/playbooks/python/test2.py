


#!/usr/bin/env python
#import platform, subprocess, re
import sys
import os
import socket
import subprocess

print(' ')
print '' ,  socket.gethostname(),
print(','),
print ('') , socket.gethostbyname(socket.gethostname()) ,
print(','),
#print '' ,  socket.gethostname(),
system = os.uname()
print '' , system,
print(','),
p = subprocess.Popen("cat /etc/redhat-release", stdout=subprocess.PIPE, shell=True)
(output , err) = p.communicate()
print (''  , output),
print(','),
kernel = subprocess.Popen("uname -r", stdout=subprocess.PIPE, shell=True)
(output , err) = kernel.communicate()
print ('' , output) ,
print(','),
cpu = subprocess.Popen("inxi -C", stdout=subprocess.PIPE, shell=True)
(output , err) = cpu.communicate()
print (output)
#print('')
#mem = subprocess.Popen("free -m", stdout=subprocess.PIPE, shell=True)
#(output , err) = mem.communicate()
#print "The information of memory is: " , output

#print 'The Status Of Memory is:'
#space = os.system("free -m")



