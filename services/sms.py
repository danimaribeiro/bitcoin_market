'''
Created on Feb 10, 2014

@author: danimar
'''

from market.models import Settings
from twilio.rest import TwilioRestClient
from twilio import TwilioRestException

def send_sms(text):
    try:
        sid = Settings.objects.get(key='twilio_sid')
        token = Settings.objects.get(key='twilio_token')
        phone = Settings.objects.get(key='twilio_phone')
        to = Settings.objects.get(key='send_sms_to')
    
        client = TwilioRestClient(sid.value, token.value)
        message = client.sms.messages.create(
                body=text,
                to=to.value,
                from_=phone.value
            )
        print message.sid
    except TwilioRestException as e:
        print e

    
    
    
    