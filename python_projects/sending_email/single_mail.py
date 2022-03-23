# To send email to gmail
import yagmail
import os

sender = os.getenv("TEMP_EMAIL")
# Can get drop mail from https://dropmail.me/en/
receiver ='slsmjxjtb+mq@bpep.firste.ml'

subject = "This is the subject"
contents = """Here is the content of the email ! Hi This is second"""

yag = yagmail.SMTP(user=sender, password=os.getenv("APP_PASSWORD"))
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Sent!")