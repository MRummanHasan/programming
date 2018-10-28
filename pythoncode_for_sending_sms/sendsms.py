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
    account_sid = 'AC0b4008bfc4afa66dcc6ef1579fb7f808'
    auth_token = 'f39367feb8e6e4cc9f58085d215a1303'

    myPhone = '+92-1234567890' #enter your number, on which you want to send SMS(msg)
    TwilioNumber = '+123456778' #Your twilio number, issued by Twilio

    client = Client(account_sid, auth_token)

    client.messages.create(
        to=myPhone,
        from_=TwilioNumber,
        body='Hello Hactoberfest,\nThis is a contribution towards opensource \n Happy coding :)')
