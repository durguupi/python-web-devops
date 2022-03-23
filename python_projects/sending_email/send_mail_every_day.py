# To send email to gmail
import yagmail, os
import time
from datetime import datetime as dt

sender = os.getenv("TEMP_EMAIL")
# Can get drop mail from https://dropmail.me/en/
receiver ='slsmjxjtb@firste.ml'

# Setting while condition to send mail periodically
while True:
    now = dt.now()
    # sends email at particular time period
    if now.hour == 7 and now.minute == 53:
        subject = f"This is the subject "
        contents = f"""Here is the content of the email ! Hello """
        yag = yagmail.SMTP(user=sender, password=os.getenv("APP_PASSWORD"))
        yag.send(to=receiver, subject=subject, contents=contents)
        print(f"Email Sent! at {now}")
        time.sleep(60) # This is in seconds