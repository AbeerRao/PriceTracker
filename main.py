import requests
from bs4 import BeautifulSoup
import smtplib
import time

# Setting the base URL
URL = "https://www.amazon.in/Panasonic-DMC-G7KGW-K-Mirrorless-Camera-Black/dp/B07JLXC5BR/ref=sr_1_1_sspa?dchild=1&keywords=camera&qid=1593245440&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVFowTzdJQlBUREEmZW5jcnlwdGVkSWQ9QTA1NDQ1NTIzRDNTT1ZWTzk0Wjg3JmVuY3J5cHRlZEFkSWQ9QTA4NzQ2MTUxVzFPUVVWRVZOS0VFJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
# Initializing the headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15"
          }

# The main function
def check_price():
    # Getting the page
    page = requests.get(URL, headers=headers)
    # The BeautifulSoup object
    soup = BeautifulSoup(page.content, 'html.parser')
    # The title and price
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    CP = price.replace(',', '')
    convertedPrice = int(CP[2:7])
    # Checking
    if convertedPrice > 30000:
        send_mail()

# Sending the email
def send_mail():
    # Establishing the server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    # Logging in
    server.login("urmail", "pass")
    # Sendin the mail
    subject = "Amazon price fell down!!"
    body = f"Check the Amzon link:\n {URL}"
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail("urmail",
                    "urmail",
                    msg)
    print("Email has been sent!")
    # Quitting the srver
    server.quit()

# Calling the function
while True:
    check_price()
    time.sleep(60)
