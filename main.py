"""
-------------------------------------------------------
[main]
-------------------------------------------------------
Author:  Luka Senfner
Email:   senfl5620@gmail.com
__updated__ = "2022-05-21"
-------------------------------------------------------
"""
# Imports

# Constants


def func():
    file = open("info.joke", "r+")
    line = file.readline().rstrip()
    """
    order of file
    phone number [includes area code]
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


func()
