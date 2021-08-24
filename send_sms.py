# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import os
from dotenv import load_dotenv


def send_sms(msg):
    # Your Account Sid and Auth Token from twilio.com/console
    # Get the environment variables. See http://twil.io/secure
    load_dotenv("E:/Python/EnvironmentVariables/.env")
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    twilio_number = os.getenv('TWILIO_NUMBER')
    my_number = os.getenv('My_Mobile')

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=msg,
        from_=twilio_number,
        to=my_number)

    print(message.sid)
    print(message.status)
