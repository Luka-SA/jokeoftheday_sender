"""
-------------------------------------------------------
[stuff]
-------------------------------------------------------
Author:  Luka Senfner
Email:   senfl5620@gmail.com
__updated__ = "2022-05-22"
-------------------------------------------------------
"""
# Imports
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
"""
jokes = open("jokes.txt", "r", encoding="utf-8")


def sendmessage(number, account_sid, auth_token, message):
    from twilio.rest import Client
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        messaging_service_sid='MGb546b8baa589f873cb5ad0789243f77c',
        body=message,
        to=number)

    print(message.sid)
    return


def getjokes_file():
    joke = jokes.readline()
    if joke != "":
        return joke
    else:
        joke = "No more jokes!"
        jokes.close()
        return joke


getjokes_file()
