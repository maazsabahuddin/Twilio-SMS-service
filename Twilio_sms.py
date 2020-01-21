from twilio.rest import Client
import os

try:
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body="Hi Maaz.",
                         from_='+12015080329',
                         to='+923092581213'
                     )

    print(message.sid)

except Exception as e:
    print(ValueError("Failed to access twilio credentials." + str(e)))
