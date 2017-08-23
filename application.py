import os
import smtplib
import requests

from utils import (
    SMTP_PORT,
    SMTP_EMAIL,
    SMTP_SERVER,
    SMTP_PASSWORD,
    SMTP_EMAIL_RECEIVER
)


MONITOR_PRICE = 0.23


def retrieve_price():
    url = 'https://www.bitstamp.net/api/v2/ticker/xrpeur/'
    response = requests.get(url)
    return float(response.json()['last'])


def send_email(price):
    message = 'XRP PRICE: {}'.format(price)
    smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp_server.starttls()
    smtp_server.login(SMTP_EMAIL, SMTP_PASSWORD)
    smtp_server.sendmail(SMTP_EMAIL, SMTP_EMAIL_RECEIVER, message)
    smtp_server.quit()


if __name__ == '__main__':
    price = retrieve_price()
    if price > MONITOR_PRICE:
        send_email(price)
        print('EMAIL SENT')
    else:
        print('The current price {} is lower than the alert price {}'.format(price, MONITOR_PRICE))
