import subprocess
import os
import sys

def banner():
   print('#######################################################################################################\n\n')
   print('RFS Network Scan v1')
   print('#######################################################################################################\n\n')

banner()
n1 =int(sys.argv[1])
n2 =int(sys.argv[2])
if(n1>0): 
 n1=n1 
else: 
 n1=100
if(n2>0): 
 n2 = n2
else: 
 n2=120
print("Devices online")
with open(os.devnull,"wb") as limbo:
 for n in xrange(n1,n2):
  ip = "192.168.0.{0}".format(n)
  result = subprocess.Popen(["ping","-c","1","-n","-W","2",ip],
                               stdout=limbo, stderr=limbo).wait()
  
  if result == 0:
      print (ip, "online")
  
