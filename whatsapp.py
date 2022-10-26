from twilio.rest import Client 
import json

f = open('auth.json')
data = json.load(f)
account_sid = data["account_sid"]
auth_token = data["auth_token"]


client = Client(account_sid, auth_token) 

def send_location(number, lat, long, body):

    # client = Client(account_sid, auth_token) 
    # number =  "+91"+ number
    # 37.787890,-122.391664
    message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=body,
            persistent_action=[f'geo:{lat},{long}'],
            to=f'whatsapp:+91{number}'
        )
    print(message.sid)
    return True

send_location("9462447291", "37.787890","-122.391664","Ice cream vendor")