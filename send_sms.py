# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import os
from dotenv import load_dotenv


def send_sms(msg):
    # Your Account Sid and Auth Token from twilio.com/console
    # Get the environment variables. See http://twil.io/secure
    load_dotenv("E:/Python/EnvironmentVariables/.env")
    account_sid = os.getenv()['TWILIO_ACCOUNT_SID']
    auth_token = os.getenv()['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=msg,
        from_='+17043255725',
        to='+447796211498')

    print(message.sid)
    print(message.status)
