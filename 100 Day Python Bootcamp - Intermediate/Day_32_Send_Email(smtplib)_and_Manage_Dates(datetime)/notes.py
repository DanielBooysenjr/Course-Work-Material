# Sending E-Mails using Python & SMTPLib
import smtplib

my_email = "danielpythoncoding@gmail.com"
password = "fhhkdmfptywewudf"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="danielbooysenjr@gmail.com", 
        msg="Subject:This is a Python E-Mail \n\nHello"
        )

# Datetime

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
hour = now.hour
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1994, month=12, day=16)
print(date_of_birth)