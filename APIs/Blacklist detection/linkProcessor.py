from urllib.parse import urlparse
import tldextract
import csv
import time

debug = False # Used for debuging purposes

#domain = urlparse('http://www.example.test/foo/bar').netloc

def read_csv(filename): # Reads a csv and yield rows
    i = 0
    with open(filename, 'r', newline='\n', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=',',lineterminator='\n')
        # Skip header if present
        next(csv_reader, None)
        for row in csv_reader:
            yield row[0]

def process(url):
    filename = 'resources/blacklist.csv'  # Path to blacklist CSV file
    # parts = tldextract.extract(url)
    # domain = parts.domain
    # subdomain = parts.subdomain
    
    # target = subdomain+'.'+domain # Parse the target domain name from url (Test url)
    
    
    
    for row in read_csv(filename):
        # parts = tldextract.extract(row)
        # domain = parts.domain
        # subdomain = parts.subdomain
        # domain = subdomain+'.'+domain # Parse the domain name from url
        if url == row:
            # print(target,domain)
            return True # If domain is blacklisted
        
    return False # Domain not blacklisted


if debug: 
    start_time = time.time()
    ret = process("http://djkatrina.ru/sobytiya/meropriyatiya/klub-prime-otkryvaetsya-posle-remonta-i-razdaet-podarki.html")
    end_time = time.time()
    print(ret)
    # Debug function's performance
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")
        
