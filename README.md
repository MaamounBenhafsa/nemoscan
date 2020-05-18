
# nemoscan
Nemoscan is a script For Get Information About Targets Using Online API That Perform Speed Nmap, geoip ,dnslookup,whois,reverse_ip_lookup include In a directory-fuzzer By Default There Are 3 Mods 
fuzz modes :
 1. Mode 1 : WordPress  plugins
 2. Mode 2 : WordPress themes  
 3. Mode 3 : Joomla Components
 
   **Contents:**
   
**1-Nmap:**
				
    nemoscan().nmap("Host")
  **2-Geoip:**
				  
    nemoscan().geoip("Host Or Adress IP")
**3-Dns Lookup:**

    nemoscan().dnslookup("Host Here")
**4-Whois:**

    nemoscan().whois("Domain Here Or Host")
   **5-Reverse IP Lookup**
   
    nemoscan().reverse_ip_lookup("algerietelecom.dz")
**6-Directory Fuzz**

> Simple Website Fuzz :

 - Fuzz Website Using wordlist.txt: 
 default=For For Wordlist By User : wordlist.txt
 
 

    nemoscan().fuzz(host="http://website.com/",default=False,mode=None,wordlist="wordlist.com")

> With mods : 

 -Get wordpress.com plugins: 
    

nemoscan().fuzz(host="http://wordpress.com/",default=True,mode=1,wordlist="None") 
        
 -Get wordpress.com themes:
    

nemoscan().fuzz(host="http://wordpress.com/",default=True,mode=2,wordlist="None")
        
 -Get joomla.com components:
    

nemoscan().fuzz(host="http://joomla.com/",default=True,mode=3,wordlist="None")

**Simple main Script** :

    python3 main.py
    usage: main.py [-h] [--host HOST] [--nmap] [--geoip] [--dnslookup] [--whois] [--reverse-ip-lookup] [--fuzz] [--mode MODE]
               [--default_wordlist] [--wordlist WORDLIST]

Nemo Scan

optional arguments:
  -h, --help           show this help message and exit
  --host HOST          Host
  --nmap               Nmap
  --geoip              Geoip
  --dnslookup          Dns Lookup
  --whois              Whois
  --reverse-ip-lookup  Reverse IP Lookup
  --fuzz               fuzz
  --mode MODE          mode1 --> wordpress.com plugins mode2 --> Get wordpress.com themes mode3 -->
  --default_wordlist   Default Wordlist True By User Wordlist By False
  --wordlist WORDLIST  Default Wordlist False define wordlist
