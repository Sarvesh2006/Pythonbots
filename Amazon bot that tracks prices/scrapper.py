import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/Apple-MMEF2AM-AirPods-Wireless-Bluetooth/dp/B07H461TBQ/ref=sr_1_4?crid=2DAMT5MVU8F7I&dchild=1&keywords=apple+airpods&qid=1584705491&sprefix=apple+%2Caps%2C513&sr=8-4'

headers = "you can get it from google by searching my user agent."

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="title").get_text()

    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = price


    if converted_price < 103.99:
        print(title.strip())
        print(converted_price)

    if converted_price > 103.99:
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 527)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('youremail', 'yourpassword')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.com/Apple-MMEF2AM-AirPods-Wireless-Bluetooth/dp/B07H461TBQ/ref=sr_1_4?crid=2DAMT5MVU8F7I&dchild=1&keywords=apple+airpods&qid=1584705491&sprefix=apple+%2Caps%2C513&sr=8-4'

    msg = f"Subject: {subject}\n\n {body}"

    server.sendmail(
        'sendermail',
        'recievermail',
        msg
    )
    print('THE EMAIL HAS BEEN SENT!')
    server.quit()

check_price()