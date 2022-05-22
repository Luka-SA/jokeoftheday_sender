"""
-------------------------------------------------------
[stuff]
-------------------------------------------------------
Author:  Luka Senfner
Email:   senfl5620@gmail.com
__updated__ = "2022-05-21"
-------------------------------------------------------
"""
# Imports
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
"""
# Constants
jokes = open("jokes.txt", "r")


def sendmessage(number, account_sid, auth_token, message):
    from twilio.rest import Client

    #account_sid = ''
    #auth_token = ''
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        messaging_service_sid='MGb546b8baa589f873cb5ad0789243f77c',
        body=message,
        to=number)

    print(message.sid)
    return


def getjokes_file():
    joke = jokes.readline()
    # no strip?
    if joke != "":
        return joke
    else:
        joke = "No more jokes"
        return joke


getjokes_file()
