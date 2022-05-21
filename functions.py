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

# Constants
# auth token
# 024ea585518f5db6c0fcc1c89b84c808
# account SID
# ACd58b46583ec9cfc521132b709f22754c
# test auth token
# 0c94e9d831d5344548db61e0c4f6d3b3
# test account SID
# ACd5d6335450ab020bd8fd42a096d345c3
# recovery code
# zT1G7uRUuQrEJf8EKOPlVPtoue1trhlWDFw0hx-a


def sendmessage(number, account_sid, auth_token):
    from twilio.rest import Client

    #account_sid = 'ACd58b46583ec9cfc521132b709f22754c'
    #auth_token = '024ea585518f5db6c0fcc1c89b84c808'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        messaging_service_sid='MGb546b8baa589f873cb5ad0789243f77c',
        body="A joke a day keeps Isaiah away\ntest",
        to=number)

    print(message.sid)
