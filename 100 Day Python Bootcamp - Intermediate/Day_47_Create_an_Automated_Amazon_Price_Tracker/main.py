# Amazon Pice Tracker

from bs4 import BeautifulSoup
import smtplib
import requests
import lxml

url = "https://www.amazon.com/Dell-Laptop17-0-inch-Touchscreen-Display-i9-12900HK/dp/B09PHBDT7K/ref=sr_1_3?crid=3L54VIRPHAFLK&keywords=Dell+XPS+17+%289730%29&qid=1678523430&sprefix=dell+xps+17+9730+%2Caps%2C338&sr=8-3"
my_email = "" # YOUR EMAIL
password = "" # YOUR PASSWORD

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
}

response = requests.get(url=url, headers=headers)
amazon_webpage = response.text
soup = BeautifulSoup(amazon_webpage, "lxml")

# print(soup.prettify)

current_price_var = soup.find(class_="a-price-whole").getText().replace(",","").replace(".","")
title = soup.find(id="productTitle", class_="a-size-large product-title-word-break").getText().strip()


current_price_int = int(current_price_var)

if current_price_int <= 3200:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(
            user=my_email,
            password=password
        )
        connection.sendmail(
            from_addr=my_email,
            to_addrs="danielpythoncoding@gmail.com",
            msg=f"Subject: PRICE ALERT FOR XPS! \n\n{title}, is now ${current_price_int}\n\nFollow this link: {url}"
                            )


