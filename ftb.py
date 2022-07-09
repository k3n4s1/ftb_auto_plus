# 100min        = 1+
# 10baudu       = 1+
# gunlic        = 1+
# /tei          = 1+
# 500staru      = 1+
# 2000g nark    = 1+
# jail          = 1+

import os
from time import sleep
import colorama
from colorama import Back, Fore, Style, init
init()

colorama.init(autoreset=True)

os.system("cls")
print(f"""{Style.NORMAL}{Fore.BLUE}
     ________   _________   ______    
    |_   __  | |  _   _  | |_   _ \   
      | |_ \_| |_/ | | \_|   | |_) |  
      |  _|        | |       |  __'.  
     _| |_        _| |_     _| |__) | 
    |_____|      |_____|   |_______/  
                                  
{Style.BRIGHT}by Cartz_Monc
t.me./k_blanc 
FTB | Darbo dienos ataskaita
""")
min_plus = 0
bauda_plus = 0
gunlic_plus = 0
tei_plus = 0
star_plus = 0
nark_plus = 0
jail_plus = 0

minute = int(input(f"{Fore.BLUE}[+] Kiek minuciu pradirbai?{Fore.RESET} 0-1000{Fore.BLUE} \n[+] "))

if 100 <= minute <= 199:
    min_plus += 1
elif 200 <= minute <= 299:
    min_plus += 2
elif 300 <= minute <= 399:
    min_plus += 3
elif 400 <= minute <= 499:
    min_plus += 4
elif 500 <= minute <= 599:
    min_plus += 5
elif 600 <= minute <= 699:
    min_plus += 6
elif 700 <= minute <= 799:
    min_plus += 7
elif 800 <= minute <= 899:
    min_plus += 8
elif 900 <= minute <= 999:
    min_plus += 9
elif 1000 <= minute <= 1099:
    min_plus += 10
else:
    sleep(0)
 
bauda = int(input(f"{Fore.BLUE}[+] Kiek baudu turite?{Fore.RESET} 0-100{Fore.BLUE} \n[+] "))

if 10 <= bauda <= 19:
    bauda_plus += 1
elif 20 <= bauda <= 29:
    bauda_plus += 2
elif 30 <= bauda <= 39:
    bauda_plus += 3
elif 40 <= bauda <= 49:
    bauda_plus += 4
elif 50 <= bauda <= 59:
    bauda_plus += 5
elif 60 <= bauda <= 69:
    bauda_plus += 6
elif 70 <= bauda <= 79:
    bauda_plus += 7
elif 80 <= bauda <= 89:
    bauda_plus += 8
elif 90 <= bauda <= 99:
    bauda_plus += 9
elif 100 <= bauda <= 109:
    bauda_plus += 10
else:
    sleep(0)

gunlic = int(input(f"{Fore.BLUE}[+] Kiek gunlic nupisai?{Fore.RESET} 0-5{Fore.BLUE} \n[+] "))
if gunlic == 1:
    gunlic_plus += 1
elif gunlic == 2:
    gunlic_plus += 2
elif gunlic == 3:
    gunlic_plus += 3
elif gunlic == 4:
    gunlic_plus += 4
elif gunlic == 5:
    gunlic_plus += 5
else:
    sleep(0)

tei = int(input(f"{Fore.BLUE}[+] Kiek teisiu nupisote?{Fore.RESET} 0-5{Fore.BLUE} \n[+] "))
if tei == 1:
    tei_plus += 1
elif tei == 2:
    tei_plus += 2
elif tei == 3:
    tei_plus += 3
elif tei == 4:
    tei_plus += 4
elif tei == 5:
    tei_plus += 5
else:
    sleep(0)

star = int(input(f"{Fore.BLUE}[+] Kiek staru surinkote?{Fore.RESET} 0-5000{Fore.BLUE} \n[+] "))
if 500 <= star <= 999:
    star_plus += 1
elif 1000 <= star <= 1499:
    star_plus += 2
elif 1500 <= star <= 1999:
    star_plus += 3
elif 2000 <= star <= 2499:
    star_plus += 4
elif 2500 <= star <= 2999:
    star_plus += 5
elif 3000 <= star <= 3499:
    star_plus += 6
elif 3500 <= star <= 3999:
    star_plus += 7
elif 4000 <= star <= 4499:
    star_plus += 8
elif 4500 <= star <= 4999:
    star_plus += 9
elif 5000 <= star <= 5499:
    star_plus += 10
else:
    sleep(0)

nark = int(input(f"{Fore.BLUE}[+] Kiek gramu nark nupisai?{Fore.RESET} 0-10000{Fore.BLUE} \n[+] "))
if 2000 <= nark <= 3999:
    nark_plus += 1
elif 4000 <= nark <= 5999:
    nark_plus += 2
elif 6000 <= nark <= 7999:
    nark_plus += 3
elif 8000 <= nark <= 9999:
    nark_plus += 4
elif 10000 <= nark <= 10999:
    nark_plus += 5
else:
    sleep(0)

jail = int(input(f"{Fore.BLUE}[+] Kiek zaideju pasodinai?{Fore.RESET} 0-5{Fore.BLUE} \n[+] "))
if jail == 1:
    jail_plus += 1
elif jail == 2:
    jail_plus += 2
elif jail == 3:
    jail_plus += 3
elif jail == 4:
    jail_plus += 4
elif jail == 5:
    jail_plus += 5
else:
    sleep(0)


print("")
sleep(2)
plusai = float(bauda_plus) + float(min_plus) + float(gunlic_plus) + float(tei_plus) + float(star_plus) + float(nark_plus) + float(jail_plus)
print(f"{Style.NORMAL}{Fore.BLUE}Jus turite gauti {Style.RESET_ALL}{Fore.RESET}{plusai:g}{Style.NORMAL}{Fore.BLUE} plusius.")
sleep(10)
print(f"{Fore.RED}END")
sleep(1)
quit()
