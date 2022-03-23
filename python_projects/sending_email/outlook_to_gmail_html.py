import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


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

# Connecting to outlook server with .com and default port
server = smtplib.SMTP('smtp.office365.com',587)
server.starttls()
server.login(sender, send_pass) # logging in to mail
message_text = message.as_string() # Converting from dictionary format to string format
print(message_text)
server.sendmail(sender, receiver, message_text) # sending the mail
server.quit()