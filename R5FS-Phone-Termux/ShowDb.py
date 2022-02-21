import os,sqlite3

def banner():
   print('#######################################################################################################\n\n')
   print('RFS DB v2')
   print('#######################################################################################################\n\n')

try:
   banner()
   arq = input('Digite o nome da pasta: ')
   db =  input('Digite o nome do banco de Dados: ')
   tab = input('Digite o nome da tabela:')
   dir = '/data/data/'+arq+'/databases/'+db
   dira = '/data/data/com.termux/files/home'
   print('Diretorio do banco de dados: '+dir)
   os.system('su -test cp %s  %s'%(dir,dira))
   os.system('su -test chmod 777 %s '%db)
   print('\n\n************************************************************************************************************')
   print('[+]Informacoes encontradas: \n')
   con = sqlite3.connect(db)
   cursor = con.cursor()
   sql = "SELECT * FROM "+tab
   data = cursor.execute(sql)
   v1 = 0
   for i in data:
      val = 0
      size = len(i)
      print('[*]'+str(v1)+' ==> Array<size['+str(size)+']>')
      while(val< size):
         print('[****][%d] ==>%s'%(val,str(i[val])))
         val += 1
      v1 += 1 
      print('\n')
   con.close()
   os.system('rm %s'%db)
except Exception as e:
   print('\n [-] Banco de Dados nao encontrado... \n[-]Erro ==>  '+str(e))
