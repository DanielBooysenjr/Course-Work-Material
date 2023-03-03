import requests
import smtplib
from datetime import date
from datetime import timedelta

# # # STOCK DATA # # #

# Stock Constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "O3J9QE4V17IOMHHF"

# Email Creds
my_email = "danielpythoncoding@gmail.com"
password = "xeaqpjkfaaxnlqoj"

# Parameters for quering stock data
parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

# Quering the stock data
response = requests.get("https://www.alphavantage.co/query", params = parameters)
response.raise_for_status()
data = response.json()

# Getting the dates
today = date.today()
yesterday = today - timedelta(days = 3)
day_before_yesterday = today - timedelta(days = 4)

# Returning closing prices for dates specified
Friday = float(data["Time Series (Daily)"][f"{yesterday}"]["4. close"])
Thursday = float(data["Time Series (Daily)"][f"{day_before_yesterday}"]["4. close"])
Friday_int = int(Friday)
Thursday_int = int(Thursday)

# Get percentage of the difference between prices
percentage_difference = round(((Thursday_int - Friday_int) / Friday_int) * 100, 2)


# # # NEWS DATA # # #

# News constants
NEWS_API_KEY = "d100714acce54b548219f2f673aca94a"

# News parameters
news_params = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
    "from": "2023-02-23",
    "to": "2023-02-24"
}
# Quering the news data
news_response = requests.get("https://newsapi.org/v2/everything", params = news_params)
news_response.raise_for_status()
news_data = news_response.json()
# Returning the news title and description
top_news_title = news_data["articles"][1]["title"]
top_news_description = news_data["articles"][1]["description"]

# Getting the last 3 news articles
for news in range(3):
    top_news_title = news_data["articles"][news]["title"]
    top_3_description = news_data["articles"][news]["description"]
    # Sending the emails
    if percentage_difference > 1:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            message = f"Subject: New Stock News Alert\n\n {STOCK}: {percentage_difference}%\n\nHeadline: {top_news_title}\nBrief: {top_3_description}"
            connection.sendmail(my_email, my_email, message.encode('utf-8'))

    elif percentage_difference < -1:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            message = f"Subject: New Stock News Alert\n\n {STOCK}: {percentage_difference}%\n\nHeadline: {top_news_title}\nBrief: {top_3_description}"
            connection.sendmail(my_email, "danielbooysenjr@gmail.com", message.encode('utf-8'))



