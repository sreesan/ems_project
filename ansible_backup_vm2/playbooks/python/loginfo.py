


#!/usr/bin/env python
#import platform, subprocess, re
import sys
import os
import socket
import subprocess

print(' ')
print socket.gethostname(),
print(','),
print socket.gethostbyname(socket.gethostname()) ,
print(','),
system = os.uname()
print system,
print(','),
kernel = os.popen('uname -r')
ker = kernel.read()
print ker,
print (' , ') ,
test = "\n"
test.splitlines()
cpu = os.popen('inxi -C')
cp = cpu.read()
print cp.rstrip()


