from twilio.rest import Client
import io
import time
import datetime
from datetime import datetime
from dateutil import parser #third party library

# SMS Sending Code
# Input: PatietnContactNo, DocName, Timings
# output: nothing
def sendsms(pContactNo, DocName, Timings):
    account_sid = ''
    auth_token = ''

    myPhone = '+92-1234567890' #enter your number, on which you want to send SMS(msg)
    TwilioNumber = '+123456778' #Your twilio number, issued by Twilio

    client = Client(account_sid, auth_token)

    client.messages.create(
        to=myPhone,
        from_=TwilioNumber,
        body='Hello Hactoberfest,\nThis is a contribution towards opensource \n Happy coding :p')
