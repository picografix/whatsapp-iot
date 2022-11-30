from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
# from realtime import getLatLong
from retrieve import ReadData
from whatsapp import send_location
from utils import extractCommand
app = Flask(__name__)

rd = ReadData()

@app.route('/default', methods=['POST'])
def default():
    resp = MessagingResponse()
    msg = resp.message()
    msg.body("Hey")

    return str(resp)


@app.route('/bot', methods=['POST'])
def bot():
    # print(request.values)
    mobile = request.values.get('WaId');
    print(mobile)
    incoming_msg = request.values.get('Body', '').lower()
    inc_msg = incoming_msg.split(" ")
    j = extractCommand(inc_msg)

    # print(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if j==1:

        a, desc = rd.listRegisteredVendors()
        s = ""
        for i in range(len(a)):
            x = a[i]
            y = desc[i]
            s+= x + ": " + y + "\n"
        msg.body(s)
        responded = True

    elif j==2:
        name = inc_msg[2]
        s = rd.getRealtimeVendor(name)
        msg.body(s)
        responded=True

    elif j==3:
        name = inc_msg[2]
        lat,lon = rd.getLatLong(vendor=name)
        send_location(mobile,lat,lon, body=f"{name}'s location")
        msg.body('I am currently here')
        responded = True
    elif j==4:
        # cde to register vendor in nearby
        pass
    elif j==5:
        # code to show nearby vendors
        pass
    elif j==6:
        msg.body("Please enter correct command")
        
        responded = True

    if not responded:
        msg.body('Write help for showing list of commands')
    return str(resp)


if __name__ == '__main__':
    app.run(port=4000)