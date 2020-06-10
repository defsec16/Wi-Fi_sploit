import os,random
from time import sleep
def clean():
	try:
		os.system('clear')
	except:
		os.system('cls')
clean()
banners = random.randint(0,3)
if banners == 0:
	banner = ''' \u001b[32m
                          
          (((((((((((((((((((((         
     ,((((((((,           *((((((((.    
  *((((((         .,*,.         ((((((. 
  (((.     (((((((((((((((((((     *((( 
       ,((((((*           /((((((       
       (((*      *(((((,      ((((      
            .(((((((((((((((            
           *((((         ((((           
                 *(((((.                
                ((((((((*               
                 (((((((             
'''
elif banners == 1:
	banner = ''' \u001b[32m
	 _    _ _       __ _             _       _ _   
	| |  | (_)     / _(_)           | |     (_) |  
	| |  | |_ ____| |_ _   ___ _ __ | | ___  _| |_ 
	| |/\| | |____|  _| | / __| '_ \| |/ _ \| | __|
	\  /\  / |    | | | | \__ \ |_) | | (_) | | |_ 
	 \/  \/|_|    |_| |_| |___/ .__/|_|\___/|_|\__|
	                          | |                  
	                          |_|                  
	'''
elif banners ==2:
	banner = '''
	|\          /\          /|
	| \        /  \        / |
	|  \      /    \      /  |
	|   \    /      \    /   |
	|    \  /        \  /    |
	|_____\/__________\/_____|
	      /\          /\\
	     /  \        /  \\
	    /    \      /    \\
	   /      \    /      \\
	  /        \  /        \\
	 /          \/          \\ '''
else:
	banner = ''' \u001b[32m

I8,        8        ,8I  88             ad88  88  
`8b       d8b       d8'  ""            d8"    ""  
 "8,     ,8"8,     ,8"                 88         
  Y8     8P Y8     8P    88          MM88MMM  88  
  `8b   d8' `8b   d8'    88  aaaaaaaa  88     88  
   `8a a8'   `8a a8'     88  """"""""  88     88  
    `8a8'     `8a8'      88            88     88  
     `8'       `8'       88            88     88  
                                                  
                                                  
                                                  
88        88                          88          
88        88                          88          
88        88                          88          
88aaaaaaaa88  ,adPPYYba,   ,adPPYba,  88   ,d8    
88""""""""88  ""     `Y8  a8"     ""  88 ,a8"     
88        88  ,adPPPPP88  8b          8888[       
88        88  88,    ,88  "8a,   ,aa  88`"Yba,    
88        88  `"8bbdP"Y8   `"Ybbd8"'  88   `Y8a   
                                                  
                                                  '''
print(banner)
text = '''
							\033[35m~coded by Alisher
			(Только на windows)			
		\033[36m[1]-\033[34mWifi-Parse
		\033[36m[2]-\033[34mWifi-passwords
	
		\033[36m[99]-\033[33mИнформация
		\033[36m[0]-\033[33mвыход
'''
print(text)
wifi = int(input('\033[31mWiFiSploit\033[39m~#:'))
def wifi99():
	text = '''
	Wifi parse он парсит пароль по названию точки wifi
	Wifi passwords он показывает все названия и пароли от этих wifi.
	к которему был подключен пк. '''
	print(text)
	sleep(6)
	os.system('python wifi-sploit.py')
def wifi0():
	print('Прощайте!')
	raise SystemExit
def wifi1():
	os.system('python wifi-parse.py')
def wifi2():
	os.system('python wifi-passwords-viewer.py')
if wifi ==1:
	wifi1()
elif wifi ==2:
	wifi2()
elif wifi ==99:
	wifi99()
elif wifi ==0:
	wifi0()
else:
	print('\033[31mОшибка:не найдено(Error:not found)')
	time.sleep(3)
	os.system("python wifi-sploit.py")