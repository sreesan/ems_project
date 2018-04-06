

#!/usr/bin/python
import subprocess
 
p = subprocess.Popen("cat /proc/meminfo", stdout=subprocess.PIPE, shell=True)
 
(output , err) = p.communicate()
 
print ('The Version Of Operating System is:'  , output)
