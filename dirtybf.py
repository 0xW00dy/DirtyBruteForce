#!/usr/bin/env python3
import requests
import argparse
import sys


#const variables
url      = ""
username = ""
wordlist = ""
ufield   = "username"
pfield   = "password"

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
    try:
        url      = args["url"]
        username = args["username"]
        wordlist = args["wordlist"]
        try: 
            ufield = args["ufield"]
            pfield = args["pfield"]
        except TypeError:
            pass
        
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
                
def bruteforce():
    pass

if __name__ == '__main__':
    main()