import ipaddress
import re
import urllib.request
from bs4 import BeautifulSoup
import socket
import tldextract
import requests
import whois
from datetime import date, datetime
from urllib.parse import urlparse

class FeatureExtraction:
    def __init__(self, url):
        self.features = []
        self.url = url
        self.domain = ""
        self.whois_response = ""
        self.urlparse = ""
        self.response = ""
        self.soup = ""

        try:
            self.response = requests.get(url)
            self.soup = BeautifulSoup(self.response.text, 'html.parser')
        except:
            pass

        try:
            self.urlparse = urlparse(url)
            self.domain = self.urlparse.netloc
        except:
            pass

        try:
            self.whois_response = whois.whois(self.domain)
        except:
            pass

        self.features.append(self.UsingIp())
        self.features.append(self.longUrl())
        self.features.append(self.shortUrl())
        self.features.append(self.symbol())
        self.features.append(self.redirecting())
        self.features.append(self.prefixSuffix())
        self.features.append(self.SubDomains())
        self.features.append(self.Hppts())
        self.features.append(self.DomainRegLen())
        self.features.append(self.AgeofDomain())
        self.features.append(self.DNSRecording())
        self.features.append(self.GoogleIndex())

    def UsingIp(self):
        try:
            ipaddress.ip_address(self.url)
            return -1
        except:
            return 1

    def longUrl(self):
        if len(self.url) < 54:
            return 1
        if len(self.url) >= 54 and len(self.url) <= 75:
            return 0
        return -1

    def shortUrl(self):
        shorteners = ['bit.ly', 'goo.gl', 'tinyurl.com', 'is.gd', 'cli.gs', 'yfrog.com', 'migre.me', 'ff.im', 'tiny.cc',
                      'url4.eu', 'twit.ac', 'su.pr', 'twurl.nl', 'snipurl.com', 'short.to', 'budurl.com', 'ping.fm',
                      'post.ly', 'just.as', 'bkite.com', 'snipr.com', 'fic.kr', 'loopt.us', 'doiop.com', 'short.ie',
                      'kl.am', 'wp.me', 'rubyurl.com', 'om.ly', 'to.ly', 'bit.do']
        return 1 if any(shortener in self.url for shortener in shorteners) else -1

    def symbol(self):
        if re.findall("@", self.url):
            return -1
        return 1

    def redirecting(self):
        if self.url.rfind('//') > 6:
            return -1
        return 1

    def prefixSuffix(self):
        try:
            match = re.findall('-', self.domain)
            if match:
                return -1
            return 1
        except:
            return -1

    def SubDomains(self):
        dot_count = len(re.findall(".", self.url))
        if dot_count == 1:
            return 1
        elif dot_count == 2:
            return 0
        return -1

    def Hppts(self):
        try:
            https = self.urlparse.scheme
            if 'https' in https:
                return 1
            return -1
        except:
            return 1

    def DomainRegLen(self):
        try:
            expiration_date = self.whois_response.expiration_date
            creation_date = self.whois_response.creation_date
            if isinstance(expiration_date, list):
                expiration_date = expiration_date[0]
            if isinstance(creation_date, list):
                creation_date = creation_date[0]
            age = (expiration_date.year - creation_date.year) * 12 + (expiration_date.month - creation_date.month)
            if age >= 12:
                return 1
            return -1
        except:
            return -1

    def AgeofDomain(self):
        try:
            creation_date = self.whois_response.creation_date
            if isinstance(creation_date, list):
                creation_date = creation_date[0]
            age = (date.today() - creation_date).days // 30
            if age >= 6:
                return 1
            return -1
        except:
            return -1

    def DNSRecording(self):
        try:
            if self.whois_response:
                return 1
            return -1
        except:
            return -1

    def GoogleIndex(self):
        try:
            domain_info = tldextract.extract(self.url)
            google_search = "https://www.google.com/search?q=site:" + domain_info.registered_domain
            response = requests.get(google_search, headers={'User-Agent': 'Mozilla/5.0'})
            return 1 if "did not match any documents" not in response.text else 0
        except:
            return -1

    def getFeaturesList(self):
        return self.features



# Example usage
url = "http://www.example.com"
features = FeatureExtraction(url).getFeaturesList()
print(features)

