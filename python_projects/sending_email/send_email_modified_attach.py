# To send email to gmail # Can get drop mail from https://dropmail.me/en/
from pydantic import FilePath
import yagmail
import os
import pandas as pd

sender = os.getenv("TEMP_EMAIL")

yag = yagmail.SMTP(user=sender, password=os.getenv("APP_PASSWORD"))

df = pd.read_csv('contacts_modified.csv')
# Function to generate filename 
def generate_file(filename, content):
    with open(filename, 'w') as file:
        file.write(str(content))

for index,row in df.iterrows():
    name = row['name']
    filename = name + ".txt"
    receiver_email = row['email']
    amount = row['amount']
    
    generate_file(filename,amount)
    
    subject = f"Hi {name} Find your Bill"
    contents = [f"""Hey {name} you have to pay {amount}""",
            filename,]
    yag.send(to=receiver_email, subject=subject, contents=contents)
    print(f"Email Sent! for {receiver_email}")