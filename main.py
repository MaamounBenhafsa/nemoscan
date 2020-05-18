import argparse
import nemoscan
import sys
parser = argparse.ArgumentParser(description='Nemo Scan')
parser.add_argument('--host', action='store', dest='host',help='Host')
parser.add_argument('--nmap', action='store_true',help='Nmap')
parser.add_argument('--geoip', action='store_true', dest='geoip',help='Geoip')
parser.add_argument('--dnslookup', action='store_true', dest='dnslookup',help='Dns Lookup')
parser.add_argument('--whois', action='store_true', dest='whois',help='Whois')
parser.add_argument('--reverse-ip-lookup', action='store_true', dest='reverse_ip_lookup',help='Reverse IP Lookup')
parser.add_argument('--fuzz', action='store_true', dest='fuzz',help='fuzz')
parser.add_argument('--mode', action='store',type=int,dest='mode',help='mode1 --> wordpress.com plugins\n mode2 --> Get wordpress.com themes\n mode3 --> ')
parser.add_argument('--default_wordlist', action='store_true',dest='default',help='Default Wordlist True By User Wordlist By False ')
parser.add_argument('--wordlist', action='store',dest='wordlist',help='Default Wordlist False define wordlist')
results = parser.parse_args()
main = nemoscan.nemoscan()
host = results.host
nmap = results.nmap
geoip = results.geoip
dnslookup = results.dnslookup
whois = results.whois
reverse_ip_lookup = results.reverse_ip_lookup
fuzz = results.fuzz
mode = results.mode
default = results.default
wordlist = results.wordlist
verbose = results.verbose
if nmap:
    print(main.nmap(host))
if geoip:
    print(main.geoip(host))
if dnslookup:
    print(main.dnslookup(host))
if whois:
    print(main.whois(host))
if reverse_ip_lookup:
	print(main.reverse_ip_lookup(host))
if fuzz and default and mode == 1:
	main.fuzz(host=host,default=True,mode=mode,wordlist="None")
if fuzz and default and mode == 2:
	main.fuzz(host=host,default=True,mode=mode,wordlist="None")
if fuzz and default and mode == 3:
	main.fuzz(host=host,default=True,mode=mode,wordlist="None")


if fuzz and default==False and mode == 1 :
	main.fuzz(host=host,default=False,mode=mode,wordlist=wordlist)
if fuzz and default==False and mode == 2 :
	main.fuzz(host=host,default=False,mode=mode,wordlist=wordlist)
if fuzz and default==False and mode == 3 :
	main.fuzz(host=host,default=False,mode=mode,wordlist=wordlist)


    

