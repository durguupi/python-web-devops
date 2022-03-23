import smtplib
import os

sender = os.getenv('OUTLOOK_MAIL')
receiver = os.getenv('TEMP_EMAIL')
send_pass = os.getenv('OUTLOOK_PASSWORD')
# This is the message format outlook expects to send or else we will receive 
# blank mail
message = """\
Subject: Hello Hello

This is test email
Just wanted to say HI
"""
# Connecting to outlook server with .com and default port
server = smtplib.SMTP('smtp.office365.com',587)
server.starttls()
server.login(sender, send_pass) # logging in to mail
server.sendmail(sender, receiver, message) # sending the mail
server.quit()