# To send email to gmail
import yagmail
import os
import pandas as pd

sender = os.getenv("TEMP_EMAIL")
# Can get drop mail from https://dropmail.me/en/
subject = "This is the subject"
contents = """Here is the content of the email ! Hi """

df = pd.read_csv('sending_email/contacts.csv')

yag = yagmail.SMTP(user=sender, password=os.getenv("APP_PASSWORD"))

for index,row in df.iterrows():
    contents = f"""Here is the content of the email ! Hi {row['name']} Welcome!!"""
    yag.send(to=row['email'], subject=subject, contents=contents)
    print(f"Email Sent! for {row['email']}")