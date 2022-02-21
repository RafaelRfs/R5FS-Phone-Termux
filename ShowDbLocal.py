import os,sqlite3
try:
   print('#######################################################################################################\n\n')
   print('RFS DB Local v2')
   print('#######################################################################################################\n\n')
   db =  input('Digite o nome do banco de Dados: ')
   tab = input('Digite o nome da tabela:')
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
except Exception as e:
   print('\n [-] Banco de Dados nao encontrado... \n[-]Erro ==>  '+str(e))
