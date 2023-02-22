##################### Normal Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

now = dt.datetime.now()
day = now.day
month = now.month
today = (month, day)
# print(today)
read = pandas.read_csv("birthdays.csv")

MY_EMAIL = "YOUR_EMAIL"
PASSWORD = "YOUR_PASS"

# Function to select a random letter template and replace the [NAME] placeholder with the birthday person's name
def random_letter():
    # Select a random letter template (there are 3 to choose from)
    random_letter = random.randint(1,3)
    with open(f"letter_templates/letter_{random_letter}.txt") as f:
        # Read the contents of the letter template
        text = f.read()
        # Replace the [NAME] placeholder in the letter template with the name of the birthday person
        modified_text = text.replace("[NAME]", f"{extract_name}")
    # Return the modified letter template
    return modified_text

# Function to send the birthday message via email
def send_email():
    # Create an SMTP connection to the email server
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Start the connection
        connection.starttls()
        # Login to the email account used to send messages
        connection.login(user=MY_EMAIL, password=PASSWORD)
        # Send the birthday message
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=f"{extract_email}",
            msg=f"Subject: Happy Birthday\n\n {random_letter()}"
        )

# Check if there are any birthdays today
if (read["month"] == month).any() and (read["day"] == day).any():
    # Select the name and email of the birthday person whose birthday it is
    extract_name = read[(read.month == month) & (read.day == day)]["name"].values[0]
    extract_email = read[(read.month == month) & (read.day == day)]["email"].values[0]
    # Send the birthday message via email
    send_email()