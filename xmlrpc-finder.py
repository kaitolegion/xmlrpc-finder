import requests
from os import system,chdir,mkdir
from time import sleep
import concurrent.futures

red  = '\033[91m'
blue = '\033[92m'
blank = '\033[00m'
green = "\033[0;32m"
red = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'

banner = """{}
        _     _  __\ / _     _ ______
       |_)| ||_)|_  X |_)|  / \ |  | 
       |  |_|| \|__/ \|  |__\_/_|_ | 

              {}Version 1.0
              
      {}XMLRPC FINDER - CODED BY KAITO
      
 {}We Don’t Responsible For Any illegal Activists

{}""".format(g,c,b,red,blank)

#-----------------------------------
target = {"xmlrpc.php"}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scan(x):
	url = x.strip()
	st = url.replace("http://","")
	link = "http://"+st
	for list in target:
	    site = link+"/"+list
	    ste = st+"/"+list
	    try:
	       r = requests.get(site,timeout=10,headers=headers)
	       if "XML-RPC server accepts POST requests only." in r.text:
	          print(red+" - "+w+site+c+" ---> "+green+"XMLRPC - Wordpress"+green+" YES!"+w)
	          
	       elif "Just a moment" in r.text:
	          print(red+" - "+w+ste+c+" ---> "+w+"Ddos Protection"+red+" NO!"+w)
	       else:
	          print(red+" - "+w+ste+c+" ---> "+w+"Not Found"+red+" NO!"+w)
	    
	    except:
	       print(red+" - "+w+ste+c+" ---> "+w+"Unknown"+red+" NO!"+w)
	    
#------------------------------------

system("clear")
print(banner)
site = input(green+" [+] Enter Site List: "+blank)
try:
	open = open(site,"r").readlines()
except:
	print(red+"\n [!] Failed To Open List")
	quit()
try:
	mkdir("result")
except:
	pass
try:
	with concurrent.futures.ThreadPoolExecutor(int(50)) as executor:
		executor.map(scan,open)
except Exception as e:
	print(e)
print(green+" [+] All Site Scanned Successful [+]")
