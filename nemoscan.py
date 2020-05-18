import requests
class nemoscan():
    def help(self):
        print("""
        Coded By Mamoun Benhafsa     17 May 2020 Keep Memories ....







        
        Simple Script That Will Help You To Get Information About Your Target Like The Online Nmap (Fast Nmap ) This Nmap Will Not Work With Local Ip Adresses
        nemoscan()
        fast online scaning with nmap:
        nemoscan.nmap("Adress IP Or Domain To Scan")      
        geoip phone number:
        nemoscan.geoip("Adress IP Or Domain To Make geoIP")  
        nemoscan.geoip("google.com") 
        nemoscan.dnslookup("facebook.com")
        nemoscan.whois("instagram.com")
        nemoscan.reverse_ip_lookup("algerietelecom.dz")
        nemoscan.fuzz("websiteHost","Default Wordlist By True User Wordlist By False","Mode -->1:wordpress plugins finder,Mode -->2:wordpress themes finder,Mode -->3:joolma components finder ")
        Get wordpress.com plugins: 
        nemoscan().fuzz(host="http://wordpress.com/",default=True,mode=1,wordlist="None") 
        Get wordpress.com themes:
        nemoscan().fuzz(host="http://wordpress.com/",default=True,mode=2,wordlist="None")
        Get joomla.com components:
        nemoscan().fuzz(host="http://joomla.com/",default=True,mode=2,wordlist="None")
        fuzz google.com with vuln_php.txt
        nemoscan().fuzz(host="http://google.com/",default=False,mode=None,wordlist="vuln_php.txt")
        """)
        pass
    def nmap(self, host):
        self.host = host
        try:
            nmap_request = requests.get("http://api.hackertarget.com/nmap/?q="+host)
            return nmap_request.text
        except requests.exceptions.ConnectionError:
            return "Connection Error"
        pass
    def geoip(self, host):
        self.host = host
        try:
            geoip_request = requests.get("http://api.hackertarget.com/geoip/?q="+host)
            return geoip_request.text
        except requests.exceptions.ConnectionError:
            return "Connection Eroor"
        pass
    def dnslookup(self, host):
        self.host = host
        try:
            dnslookup_request = requests.get("http://api.hackertarget.com/dnslookup/?q="+host)
            return dnslookup_request.text
        except requests.exceptions.ConnectionError:
            return "Connection Error"
        pass
    def whois(self, host):
        self.host = host
        try:
            whois_request = requests.get("http://api.hackertarget.com/whois/?q="+host)
            return whois_request.text
        except requests.exceptions.ConnectionError:
            return "Connection Eroor"
        pass
    def reverse_ip_lookup(self, host):
        self.host = host
        try:
            reverse_ip_lookup_requests = requests.get("http://api.hackertarget.com/reverseiplookup/?q="+host)
            return reverse_ip_lookup_requests.text
        except requests.exceptions.ConnectionError:
            return "Connection Error"
        pass
    def fuzz(self, host,default,mode,wordlist):
        self.host = host
        self.default = default
        self.wordlist = wordlist
        self.mode = mode
        if default == False :
            self.wordlist_by_user = wordlist
            self.mode = mode
            status = "By User Wordlist"
            print(status)
            try:
                with open(wordlist) as fuzz_by_user:
                    self.fuzz_by_user = fuzz_by_user
                    fuzz_by_user_line = fuzz_by_user.readline()
                    while fuzz_by_user_line:
                        fuzz_by_user_line = fuzz_by_user.readline()
                        try:
                            fuzz_request = requests.get(host+fuzz_by_user_line) 
                            print(host+fuzz_by_user_line)
                            print(fuzz_request.url)
                            print(fuzz_request.status_code)
                        except requests.exceptions.ConnectionError:
                            print("Connection Error make sure You add an '/' on The End Of Your Host Value like This : {}/ ".format(host))
                            break
                        except requests.exceptions.InvalidURL:
                            print("Bad Url:->{}".format(host))
                            break
                        except requests.exceptions.MissingSchema:
                           print("Invalid Url Try : http://{}/".format(host))
                           break
                        except KeyboardInterrupt:
                            print("CTRL+C ..... Bye")
                            break
                            
            except FileNotFoundError:
                print("Wordlist '{}' Not Found".format(wordlist))
        if default == True :
            if mode == 1:
                self.wordlist_plugins = wordlist
                wordlist = "db/wp_plugins.txt"
                status =  "wordpress plugins finder" 
                pass
            if mode == 2 :
                self.wordlist_themes = wordlist
                wordlist = "db/wp-themes.txt" 
                status = "wordpress themes finder"
                pass
            if mode == 3:
                self.wordlist_joomla = wordlist
                wordlist = "db/joomla.txt"
                status = "joolma components finder"
                pass
            pass
            try:
                print(status)
                with open(wordlist) as fuzz:
                    self.fuzz = fuzz
                    fuzz_line = fuzz.readline()
                    while fuzz_line:
                        fuzz_line = fuzz.readline()
                        try:
                            fuzz_default_request = requests.get(host+fuzz_line)
                            print(host+fuzz_line)
                            print(fuzz_default_request.status_code)
                            pass
                        except requests.exceptions.ConnectionError:
                            print("Connection Error make sure You add an '/' on The End Of Your Host Value like This : {}/ ".format(host))
                            break
                            pass
                        except requests.exceptions.InvalidURL:
                            print("Bad Url {}".format(host))
                            break
                            pass
                        except requests.exceptions.MissingSchema:
                            print("Invalid Url Try : http://{}/".format(host))
                            break
                            pass
                        except KeyboardInterrupt:
                            print("CTRL+C ..... Bye")
                            break
            except FileNotFoundError:
                print("Seems To Be No db_files ): {} " .format(wordlist))
                pass
            pass
        pass
    pass
pass
                
'''
here we go by mamoun benhafsa i heat coding with OOP classes ...

'''
#nemoscan().help()