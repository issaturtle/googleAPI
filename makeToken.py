# Hung Nguyen
# Gmail API implementation for cmpe 188
import os
import base64
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#code referenced from Google API page
#https://developers.google.com/gmail/api/quickstart/python
def getAuthToken():
    SCOPES = ['https://mail.google.com/']
    credentials = None
    #creates token.json file for verification
    #if file doesn't exist, ask user to verify
    if os.path.exists('userToken.json'):
        credentials = Credentials.from_authorized_user_file('userToken.json', SCOPES)
  
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flowCred = InstalledAppFlow.from_client_secrets_file(
                'client.json', SCOPES)
            credentials = flowCred.run_local_server(port=0)
        
        #once verified, user can skip verifying process
        with open('userToken.json', 'w') as userToken:
            userToken.write(credentials.to_json())
    
    try:
        # Call the Gmail API
        buildGmailService = build('gmail', 'v1', credentials=credentials)
        # return buildGmailService
        msg = "this is a demonstration"
        mimeMsg = MIMEMultipart()
        mimeMsg['subject'] = "for cmpe"
        mimeMsg['to'] = "enegry135@gmail.com"
        mimeMsg.attach(MIMEText(msg,'plain'))
        #turn message into raw string, https://stackoverflow.com/questions/54526973/base64-encoding-not-taking-mime-message
        buildGmailService.users().messages().send(userId = 'me', body = {'raw':base64.urlsafe_b64encode(mimeMsg.as_bytes()).decode()}).execute()

    except HttpError as error:
        print(f'An error occurred: {error}')

getAuthToken()