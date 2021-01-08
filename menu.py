import sys, os, time
import subprocess
import json
from colorama import Fore, Style
from urllib.request import urlopen
import webbrowser
url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']

print (Fore.GREEN+Style.BRIGHT+'IP-Adresse Informationen\n ')
print (Fore.GREEN+'IP-Adresse : {4} \nRegion : {1} \nLand : {2} \nStadt : {3} \nOrg : {0}'.format(org,region,country,city,IP))
print (Style.RESET_ALL)
url_z = "https://iplocator.de"
webbrowser.open_new(url_z)
url_dns = "https://www.dnsleaktest.com"
webbrowser.open_new(url_dns)
# fenster öffnen mit hauptprogramm und nsa logo als bg     < kommt in v1
#subprocess.call(['xterm', '-e', 'python3 nsa_menu.py'])         ^

print (Fore.GREEN+Style.BRIGHT+"Sollte ihr echter Standort und/oder ihre echte ISP zu sehen sein empfehlen wir\n"+
"einen VPN-Dienst zu nutzen (Virtual-Private-Network) um ihre Identität zu schützen wenn sie sich mit Servern verbinden.\n")

input ("Beliebige Taste drücken zum schließen.")