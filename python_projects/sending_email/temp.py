import os
import pandas as pd
from datetime import datetime as dt
print(os.getenv("APP_PASSWORD"))
print(dt.now())

df = pd.read_csv('sending_email/contacts_filepath.csv')
print(df)
print("=====================================================")
for index,row in df.iterrows():
    print(index)
    print(row)
print("=====================================================")
for index,row in df.iterrows():
    print(row.values)
    print(row.values[1])
print("=====================================================")
for index,row in df.iterrows():
    print(row['email'])
print("=====================================================")
for index,row in df.iterrows():
    contents = [f"""Here is the content of the email ! Hi {row['name']} you have to pay {row['amount']}""",
            f"sending_email/{row['filepath']}"]
    print(contents)
    print(f"Email Sent! for {row['email']}")