import urllib.request,os

print("#########################################################")
print("\n \n \n RFS File Downloader \n \n \n")
print("#########################################################\n")
try:
    url = str(input('Digite a url: '))
    req = urllib.request.Request(url, data=None, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
        'Content-Type':' application/x-www-form-urlencoded;charset=utf-8'
    })
    t =  urllib.request.urlopen(req)
    source = str(input('Digite o source HTML:'))
    content = str(t.read())
    find = "<"+source+" src="
    mp4 = "."+str(input("Digite o tipo de arquivo : "))
    posicao = content.index(find)+len(find)
    posicaoMp4 = content.index(mp4)+len(mp4)
    dif = posicaoMp4 - posicao
    arquivo = content[posicao + 1: posicao + dif]

    if(len(arquivo) > 0):
        print("[+] Arquivo encontrado: \n %s   "%arquivo)
        if(urllib.request.urlretrieve ( arquivo)):
            print("[+] Download feito com sucesso do arquivo "+mp4)
        else:
            print("[+] Erro ao fazer download do arquivo")

except Exception as e:
    print("[-] Erro ao encontrar o arquivo \n %s"%e)

print("\n######################################################### \n")
print('\n Special Thanks to Luciana Winchester ~ Python Girl ')

