from sys import api_version
from makeToken import getAuthToken
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

CLIENT_SECRET_FILE = 'client.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

service = getAuthToken(SCOPES)
msg = "you gay"
mimeMsg = MIMEMultipart()
mimeMsg['to'] = "enegry135@gmail.com"
mimeMsg['subject'] = "you gayer"
mimeMsg.attach(MIMEText(msg,'plain'))
raw_string = base64.urlsafe_b64encode(mimeMsg.as_bytes()).decode()
service.users().messages().send(userId = 'me', body = {'raw':raw_string}).execute()
