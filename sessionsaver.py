import argparse
import sys
import requests

version ="0.0.1"

def alive_with_base(cookie:str, base_url:str, user_agent:str, count:int, delay:int):
    from bs4 import BeautifulSoup
    
    print("Star searching urls")

    header = {"Cookie":cookie, 'User-Agent':user_agent}
    response = requests.get(base_url, headers=header)
    if response.status_code != 200 and response.status_code != 404: 
        raise ConnectionError("Bad Code")

    bsObj = BeautifulSoup(response.text, "lxml")
    links = bsObj.find_all("a", href=True)

    f_val = base_url.replace("http://","")
    f_val = f_val.replace("http://","")
    b_url = base_url
    if b_url[-1] =='/':
        b_url = b_url[0:-1]

    jump_links = [base_url]
    for link in links:
        if link['href'].find(f_val) == -1:
            if link['href'][0] =='/':
                print(f"Found link {b_url+link['href']}. Add it to list.")
                jump_links.append(b_url+link['href'])
                count-=1
                if count == 0:
                    break
        else:
            print(f"Found link {link['href']}. Add it to list.")
            jump_links.append(link['href'])
            count-=1
            if count == 0:
                break
            
    alive_with_jump(cookie, jump_links, UA, delay)

def alive_with_jump(cookie:str, j_urls:list, user_agent:str, delay:int):
    from time import sleep
    global version

    print("===============SAVER STARTED==============")
    print(f"Session saver v.{version}")
    print(f"Cookie: {cookie}")
    print(f"Jump URL's: {j_urls}")
    print(f"User Agent: {user_agent}")
    print("===============LOG:==============")
    header = {"Cookie":cookie, 'User-Agent':user_agent}

    while 1:
        for link in j_urls:
            response = requests.get(link, headers=header)
            if response.status_code >=500:
                raise ConnectionError(f"Returned code: {response.status_code}")
            if response.status_code >=300:
                print(f"[Warning] Returned code: {response.status_code}. Delay {delay} sec")
            else:
                print(f"[LOG] Good response from {link} with code {response.status_code}. Delay {delay} sec")
            sleep(delay)

parser = argparse.ArgumentParser(description="A very small utility that allows you to keep your sessions in a state of life by simulating user actions.")
parser.add_argument("--cookie", dest='cookie', type=str, help="Cookie for your session.", required=True)
parser.add_argument("--base_url", dest='b_url', type=str, help="Site URL.")
parser.add_argument("--jumping_urls", dest='j_urls', type=str, help="Urls for jumping", nargs="+")
parser.add_argument("--user_agent", dest="UA", type=str, default = f"SessionSaver/{version}", help=f"Your own UserAgent. Default: \"SessionSaver/{version}\"")
parser.add_argument("--count", dest="count", type=int, default = 5, help="Maximum number of links for base address. Must be greater than 0. Default 5.")
parser.add_argument("--delay", dest="delay", type=int, default = 30, help="Pause time between requests. Must be 0 or greater. Default 30.")

args = parser.parse_args()
if args.b_url is None and args.j_urls is None:
    raise ValueError("required --base_url or --jumping_urls")

if args.count < 0:
    raise ValueError("maximum number of links must be greater than 0")

if args.delay < 0:
    raise ValueError("Delay must be 0 or greater")

print(""" _____               _                                          _               ___       _           _  _____       
/  ___|             (_)                                        | |             |_  |     | |         | ||____ |      
\ `--.  ___  ___ ___ _  ___  _ __    ___  __ ___   _____ _ __  | |__  _   _      | |_   _| |__  _   _| |    / /_   _ 
 `--. \/ _ \/ __/ __| |/ _ \| '_ \  / __|/ _` \ \ / / _ \ '__| | '_ \| | | |     | | | | | '_ \| | | | |    \ \ | | |
/\__/ /  __/\__ \__ \ | (_) | | | | \__ \ (_| |\ V /  __/ |    | |_) | |_| | /\__/ / |_| | |_) | |_| | |.___/ / |_| |
\____/ \___||___/___/_|\___/|_| |_| |___/\__,_| \_/ \___|_|    |_.__/ \__, | \____/ \__,_|_.__/ \__, |_|\____/ \__, |
                                                                       __/ |                     __/ |          __/ |
                                                                      |___/                     |___/          |___/ """)

if not args.UA is None:
    UA = args.UA

try:
    if not args.b_url is None:
        alive_with_base(args.cookie, args.b_url, args.UA, args.count, args.delay)
    else:
        alive_with_jump(args.cookie, args.j_urls, args.UA, args.delay)
except Exception as e:
    print(e)