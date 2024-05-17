from email.message import EmailMessage
from bs4 import BeautifulSoup
from redbox import EmailBox
from datetime import datetime
import concurrent.futures
import quopri
import json
import requests
import models.Message as sms # To avoid name shadowing :)

def save_string_to_file(string, filename):
    with open(filename, 'w') as file:
        file.write(string)

box = EmailBox(
    host='imap.gmail.com',
    port='993',
    username='n7hackathon.demo@gmail.com',
    password='uqks iudc fapz fjzn'
)

def check_blacklist(url):
    try:
        response = requests.get(f"http://localhost:106/api/blacklist?url={url}")
        if response.status_code == 200:
            data = response.json()
            return data.get("blacklisted", False)
        return False
    except requests.RequestException:
        return False

def process_url(url):
    try:
        response = requests.get(f"http://localhost:107/api/process-url?url={url}")
        if response.status_code == 200:
            data = response.json()
            return data.get("spam", False)
        return False
    except requests.RequestException:
        return False

def process_nlp(text):
    try:
        payload = {'text': text}
        response = requests.post(f"http://localhost:107/api/process-nlp", data=payload)
        if response.status_code == 200:
            data = response.json()
            return data.get("spam", False)
        return False
    except requests.RequestException:
        return False
    
# Main function to execute the checks in parallel for each message
def check_message_for_spam(anchor_links, msg, message):
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = []
        
        for anchor_link in anchor_links:
            if anchor_link:
                href = anchor_link.attrs.get('href')
                futures.append(executor.submit(check_blacklist, href))
                futures.append(executor.submit(process_url, href))
        
        if anchor_link: futures.append(executor.submit(process_nlp, msg.text_body))
        
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            if res:  # If any check returns True, mark message as spam
                message.spam = True
                break

def messagesToListV2(msgs):
    result = []
    reasons = []
    for msg in msgs:
        headers = {k.lower(): v for k, v in msg.headers.items()}
        decoded_html = quopri.decodestring(msg.html_body).decode('utf-8')
        message = sms.Message(msg.from_, msg.to, msg.subject,headers['date'], decoded_html)
        bs = BeautifulSoup(decoded_html, 'html.parser')
        anchor_links = bs.select(selector="a")
                    
        reason += [check_message_for_spam(anchor_links, msg, message)]
        
        # if not message.spam:
        #     response = requests.get(f"http://localhost:106/api/blacklist?url={}")
        # if not message.spam:
        #     return
        # if not message.spam:
        #     return
        result=[message]+result
    return result


def messagesToList(msgs):
    result = []
    for msg in msgs:
        headers = {k.lower(): v for k, v in msg.headers.items()}
        decoded_html = quopri.decodestring(msg.html_body).decode('utf-8')
        message = sms.Message(msg.from_, msg.to[0], msg.subject,int(datetime.timestamp(datetime.strptime(' '.join(headers['date'].split(' ')[0:-1]),"%a, %d %b %Y %H:%M:%S"))), decoded_html)
        # bs = BeautifulSoup(decoded_html, 'lxml')
        # anchor_links = bs.select(selector="a")
        # print(anchor_links)
        # for anchor_link in anchor_links:
        #     response = requests.get(f"http://localhost:106/api/blacklist?url={anchor_link.attrs.get('href')}")
        #     if response.status_code == 200:
        #         data = response.json()
        #         if data["blacklisted"]: 
        #             message.spam = True
        #             break

        #     if not message.spam:
        #         response = requests.get(f"http://localhost:107/api/process-url?url={anchor_link.attrs.get('href')}")
        #         if response.status_code == 200:
        #             data = response.json()
        #             if data["spam"]: 
        #                 message.spam = True
        #                 break
        #     if not message.spam:
        #         payload = dict(text=msg.text_body)
        #         response = requests.post(f"http://localhost:107/api/process-nlp", data=payload)
        #         if response.status_code == 200:
        #             data = response.json()
        #             if data["spam"]: 
        #                 message.spam = True
        #                 break
        
        # if not message.spam:
        #     response = requests.get(f"http://localhost:106/api/blacklist?url={}")
        # if not message.spam:
        #     return
        # if not message.spam:
        #     return
        result=[message]+result
    return result

# inbox = box.inbox
# msgs = inbox.search(all=True)
# print(msgs[0].text_body)

# with open("data.json", 'w') as jsonFile:
#         content = json.dump(messagesToList(msgs), jsonFile, default=lambda x: x.__dict__)


def getMessages():
    inbox = box.inbox
    msgs = inbox.search(all=True)
    content = json.dumps(messagesToList(msgs), default=lambda x: x.__dict__)
    return content

def getMessagesAfter(after):
    inbox = box.inbox
    print(f'SENTSINCE {datetime.fromtimestamp(int(after))}')
    msgs = inbox.search(f'SENTSINCE "{datetime.strftime(datetime.fromtimestamp(int(after)), "%d-%b-%Y")}"')
    content = json.dumps(messagesToList(msgs), default=lambda x: x.__dict__)
    return content