# To send email to gmail
import yagmail, os
import time
count = 0

sender = os.getenv("TEMP_EMAIL")
# Can get drop mail from https://dropmail.me/en/
receiver ='slsmjxjtb@firste.ml'

# Setting while condition to send mail periodically
while count < 5:
    subject = f"This is the subject for count {count}"
    contents = f"""Here is the content of the email ! Hi from {count}"""
    yag = yagmail.SMTP(user=sender, password=os.getenv("APP_PASSWORD"))
    yag.send(to=receiver, subject=subject, contents=contents)
    print(f"Email Sent! for count {count}")
    count +=1
    time.sleep(60) # This is in seconds