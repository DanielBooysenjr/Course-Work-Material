# Sending a motivational quote on specific day

import smtplib
import random
import datetime as dt

# Setting up the email address and password for authentication
my_email = "danielpythoncoding@gmail.com"
password = "fhhkdmfptywewudf"

# Creating sending email function
def send_email():
    # Connect to the Gmail SMTP server and login with the given credentials
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        # Send an email to the recipient with a motivational quote
        connection.sendmail(
            from_addr=my_email,
            to_addrs="danielbooysenjr@gmail.com",
            msg=f"Subject: Motivational Quote of the Day\n\n {random_quote()}"
        )

# Reading the quotes.txt file and choosing a random message
def random_quote():
    with open("quotes.txt") as quotes:
        motivational_quotes = quotes.readlines()
        return random.choice(motivational_quotes)

# Creating datetime, and checking the day
now = dt.datetime.now()
weekday = now.weekday()

# Checking if the day is today(or any other day), and execute sending email if condition is True
if weekday == 2:
    send_email()
