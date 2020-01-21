from twilio.rest import Client
import os

try:
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body="Hi Maaz.",
                         from_='+xxxxxxxxxxx',
                         to='+92xxxxxxxxxx'
                     )

    print(message.sid)

except Exception as e:
    print(ValueError("Failed to access twilio credentials." + str(e)))
