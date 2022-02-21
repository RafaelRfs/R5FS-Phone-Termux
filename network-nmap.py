import nmap

def banner():
   print('#######################################################################################################\n\n')
   print('RFS Network Nmap Port Scan v1')
   print('#######################################################################################################\n\n')

banner()
N = nmap.PortScanner()
alvo = str(input(' Alvo: '))
porta = str(input(' Porta: '))

N.scan(alvo, porta)

for host in N.all_hosts():
 print('#############################')
 print('[+]Host: %s(%s)'%(host,N[host].hostname()))
 print('[+]State: %s'%N[host].state())
 for proto in N[host].all_protocols():
  print('################################')
  print('[+]Protocolo: %s'%proto)

  lport = N[host][proto].keys()
  lport = list(lport)
  lport.sort()

  for port in lport:
    print('[+]porta: %s\testado: %s'%(port, N[host][proto][port]['state']))
