import sys
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

# for implementation of api function refer https://www.geeksforgeeks.org/how-to-read-emails-from-gmail-using-gmail-api-in-python/
from googleapiclient.discovery import build 
from google_auth_oauthlib.flow import InstalledAppFlow 
from google.auth.transport.requests import Request 
import pickle 
import os.path 
import base64 
import email 
from bs4 import BeautifulSoup
import re
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
urls = []

def from_hackerrank(sender):
    mail = ""
    start = False
    for ch in sender:
        if ch=='>':
            start = False
        if start:
            mail+=ch
        if ch=='<':
            start = True
    return mail=="no-reply@hackerrankmail.com"

def is_coding_related(subject):
    patterns = ["We Challenge You to Solve", "Practice Coding with", "Can You Solve", "Improve your Coding Skills with"]
    for pattern in patterns:
        if pattern in subject:
            return True
    return False

def extract_url_and_name(body):
    match = re.search(r'## \[\*\*.*\*\*\]\(.*\)', str(body))
    url_name = str(match.group(0))
    match = re.search(r'\[\*\*.*\*\*\]', str(url_name))
    name = str(match.group(0))[3:-3]
    match = re.search(r'\(.*\)', str(url_name))
    url = str(match.group(0))[1:-1]
    return name, url
    
def dump_to_excel(url, name):
    pass

def api():
    # acquire credentials
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token: 
            creds = pickle.load(token) 
    if not creds or not creds.valid: 
        if creds and creds.expired and creds.refresh_token: 
            creds.refresh(Request()) 
        else: 
            flow = InstalledAppFlow.from_client_secrets_file('/Users/vipul/Documents/coding/python_automation/hrdump/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0) 
        with open('token.pickle', 'wb') as token: 
            pickle.dump(creds, token) 
    
    # open gmail with credentials and get mals
    service = build('gmail', 'v1', credentials=creds)
    result = service.users().messages().list(maxResults=10, userId='me').execute()
    messages = result.get('messages')
    for msg in messages:
        txt = service.users().messages().get(userId='me', id=msg['id']).execute()
        try:
            payload = txt['payload']
            headers = payload['headers']
            for d in headers:
                if d['name'] == 'Subject':
                    subject = d['value']
                if d['name'] == 'From':
                    sender = d['value']
            parts = payload.get('parts')[0]
            data = parts['body']['data']
            data = data.replace("-","+").replace("_","/")
            decoded_data = base64.b64decode(data)
            soup = BeautifulSoup(decoded_data , "lxml")
            body = soup.body()
            check1 = from_hackerrank(sender)
            check2 = is_coding_related(subject)
            if(check1 and check2):
                name, url = extract_url_and_name(body[0])
                print("SUCESS: ", name, url)
                dump_to_excel(name, url)
        except Exception:
            pass

def program():
    currdir = sys.argv[1]
    os.chdir(currdir)
    # worked = get_urls()
    api()

if __name__ == '__main__':
    program()
