import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender = os.getenv('OUTLOOK_MAIL')
receiver = os.getenv('TEMP_EMAIL')
send_pass = os.getenv('OUTLOOK_PASSWORD')
# ending in this way to recive HTML or other forms of text 
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'Hello Again from HTML !'

body = """ 
<h2>Hi There Hello !</h2>
Have a wonderful day ahead 
Lets start our day rocking !!!
"""
mimetext = MIMEText(body, 'html') # This can be plain or html
message.attach(mimetext)

# Attaching a file 
attachment_path ='tiger.jpeg'
attachment_file = open(attachment_path, 'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload(attachment_file.read())
encoders.encode_base64(payload)
payload.add_header('Content-Disposition','attachment', filename=attachment_path)
message.attach(payload)


# Connecting to outlook server with .com and default port
server = smtplib.SMTP('smtp.office365.com',587)
server.starttls()
server.login(sender, send_pass) # logging in to mail
message_text = message.as_string() # Converting from dictionary format to string format
print(message_text)
server.sendmail(sender, receiver, message_text) # sending the mail
server.quit()