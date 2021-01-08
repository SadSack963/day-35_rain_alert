# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


def send_sms(msg):
    # Your Account Sid and Auth Token from twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=msg,
        from_='+17043255725',
        to='+447796211498')

    print(message.sid)
    print(message.status)
