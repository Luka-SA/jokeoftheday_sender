"""
-------------------------------------------------------
[main]
-------------------------------------------------------
Author:  Luka Senfner
Email:   senfl5620@gmail.com
__updated__ = "2022-05-22"
-------------------------------------------------------
"""
# Imports
from functions import *
import schedule
import time


def check_account():
    """ check if you have already entered information
    or if you need to...
    """
    file = open("info.joke", "r+")
    line = file.readline().rstrip()
    """
    **order of file:**
    phone number [includes country code]
    auth token
    account SID
    """
    # i am going to assume you have not screwed the file up
    # do not screw around with it
    if line.isnumeric():
        phone_number = line
        auth_token = file.readline().rstrip()
        account_SID = file.readline().rstrip()
    else:
        country_code = input("Input your country code: ")
        number = input("Input your phone number: ")
        phone_number = country_code + number
        auth_token = input("Input your Twilio auth token: ")
        account_SID = input("Input your Twilio Account SID: ")
        # now write this to the file for safekeeping, assuming there is nothing
        # in it
        file.write(phone_number + "\n")
        file.write(auth_token + "\n")
        file.write(account_SID + "\n")
    file.close()
    job(phone_number, auth_token, account_SID)


def send_joke(phone_number, account_SID, auth_token):
    message = getjokes_file()
    if message == "No more jokes":
        sendmessage(phone_number, account_SID, auth_token, message)
        exit()
    else:
        sendmessage(phone_number, account_SID, auth_token, message)


def job(phone, auth, SID):
    schedule.every(1).seconds.do(send_joke, phone, SID, auth)

    while True:
        schedule.run_pending()
        time.sleep(1)


check_account()
