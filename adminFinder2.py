import urllib2, threading,os,Queue
print('##################################################################\n')
print ("\n\n RFS FINDER \n\n")
print('##################################################################\n')
print('\n Site TESTE: %s \n'%"testphp.vulnweb.com")
print('\n Wordlist teste: %s \n'%"wordslist.txt")
threads = 100
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11. Linux x86_64. rv:19.0) Gecko/2010010 Firefox/19.0'
target = "http://"+raw_input("[+]Digite a url:")  
wordlist = raw_input("[+]Wordlist:")
resume = None

def build_wordlist(wordlist):
    fd = open(wordlist,'rb')
    raw_words = fd.readlines()
    fd.close()
    found_resume = False
    words = Queue.Queue()
    for word in raw_words:
        word = word.rstrip()
        if resume is not None:
            if found_resume:
                words.put(word)
            else:
                if(word == resume):
                    found_resume = True
                    print('Resumindo wordlist de: %s'%resume)
        else:
            words.put(word)
    return words


def bruteforceDir(word_queue,extensions=None):
    while not word_queue.empty():
        attempt = word_queue.get()
        attemp_list = []
        if "." not in attempt:
            attemp_list.append("/%s/"%attempt)
        else:
             attemp_list.append("/%s"%attempt)

        if extensions:
            for extension in extensions:
                attemp_list.append("/%s%s"%(attempt,extension))
                
        for brute in attemp_list:
            url = "%s%s"%(target,urllib2.quote(brute))
            try:
                r = urllib2.Request(url,headers=headers)
                response = urllib2.urlopen(r)
                if len(response.read()):
                    print("\n[%d]Found => %s"%(response.code,url))
                    
            except Exception as e:
                pass

try:
    word_queue = build_wordlist(wordlist)
    extensions = [".php",".bak",".asp",".aspx",".jsp",".txt",".py",".xml",".htm","phtml"]
    print('[*]Diretorios encontrados da wordlist: ')
    for i in range(threads):
        t = threading.Thread(target=bruteforceDir,args=(word_queue,extensions))
        t.start()
except:
    print('[-]Erro ao abrir o site ou wordlist ')
