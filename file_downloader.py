from BeautifulSoup import BeautifulSoup
import urllib2
import re
print("#########################################################")
print("\n \n \n RFS File Downloader v2 \n \n \n")
print("#########################################################\n")

def download(url):
 file_name = url.split('/')[-1]
 u = urllib2.urlopen(url)
 f = open(file_name, 'wb')
 meta = u.info()
 file_size = int(meta.getheaders("Content-Length")[0])
 print "\n Downloading: %s Bytes: %s \n" % (file_name, file_size)
 file_size_dl = 0
 block_sz = 8192
 while True:
    buffer = u.read(block_sz)
    if not buffer:
        break
    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print ("\n %s"%status),
 f.close()

#'http://camendesign.com/code/video_for_everybody/test.html'
url = str(raw_input('Digite a url: '))
tag = str(raw_input('Digite a tag: ')) #source img video
source = str(raw_input('Digite a source: ')) #href #src
typ = str(raw_input('Digite o tipo de arquivo: ')) #Mp4 #mp3
n = 0;
print("\n######################################################### \n")
print("\n [+] Arquivos encontrados: \n")

html_page = urllib2.urlopen(url)
soup = BeautifulSoup(html_page)
for link in soup.findAll(tag):
    linker = link.get(source)
    n = n+1
    print("\n [+]%s - %s"%(n,linker))
    if(typ in linker):
        print('\n [+]Fazendo download do arquivo %s ... \n '%typ)
        download(linker)
print("\n######################################################### \n")
