
#!/usr/bin/env python
import platform, subprocess, re

import os
import socket

print socket.gethostbyname(socket.gethostname())
print socket.gethostname()

CPU_Pct=str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))
print("CPU Usage = " + CPU_Pct)
unumber = os.getuid()
pnumber = os.getpid()
where = os.getcwd()
what = os.uname()
cpu = os.system("cat /proc/cpuinfo")

print "The cpu status is" , cpu
print "User number",unumber
print "Process ID",pnumber
print "Current Directory",where
print "System information",what

subprocess.call(["cat", "/proc/cpuinfo"])

