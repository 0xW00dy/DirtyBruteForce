# DirtyBruteForce

```(                                (     
 )\ )              )          (   )\ )  
(()/(  (   (    ( /( (      ( )\ (()/(  
 /(_)) )\  )(   )\()))\ )   )((_) /(_)) 
(_))_ ((_)(()\ (_))/(()/(  ((_)_ (_))_| 
 |   \ (_) ((_)| |_  )(_))  | _ )| |_   
 | |) || || '_||  _|| || |  | _ \| __|  
 |___/ |_||_|   \__| \_, |  |___/|_|    
                     |__/             
 ```
 
# Legal Disclaimer: 
Usage of dirtybf for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program


# How to use

```
usage: dirtybf.py [-h] -u [URL] -w [WORDLIST] --username [USERNAME] [--ufield [UFIELD]] [--pfield [PFIELD]]

CLI Bruteforcer for login fields.

optional arguments:
  -h, --help            show this help message and exit
  -u [URL], --url [URL]
                        Set url to bruteforce (needed)
  -w [WORDLIST], --wordlist [WORDLIST]
                        Path to wordlist (needed)
  --username [USERNAME]
                        Username to bruteforce (needed)
  --ufield [UFIELD]     Username field if different than 'username'
  --pfield [PFIELD]     Password field if different than 'password'
  ```
  
 You can bruteforce any login field using this tool. 
 This tool will be of a great utility during CTFs. You will need a wordlist such as rockyou to use it.
 
 Don't hesitate to PM me if you think a feature should be added and I'll do my best to add it !
 
 # Install
 
 ```pip install -r requirements.txt```
 
