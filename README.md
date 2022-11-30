# whatsapp-iot
Proof of concept for Whatsapp-IOT interface

# Tasks
### Phase 1
 - [x] Connect ESP8266 to Firebase
 - [ ] Connect Server to Firebase
 - [ ] Connect Server to Whatsapp
 - [ ] Test Whatsapp-Firebase connection

 Vendor registration would be through arudino no need for a portal as of now
 Need to figure out how to get nearby vendors, whether to use realtime database or not
 Maybe running sql queries on latitude and longitude or what?

 Google distance matrix api

 Sharing a google map url? or sharing location over whatsapp?
 Google map url will have the location of vendors updated timely

 use numpy to perform calculations


 Quickstart
1. `pip install -r requirements.txt`
2. `ngrok http 4000`
whatsapp-iot

gcloud services enable --project "whatsapp-iot" "static-maps-backend.googleapis.com"
gcloud services list --project "whatsapp-iot"

gcloud alpha services api-keys create --project "whatsapp-iot" --display-name "WHATSAPP_GOOGLE"



# Start

1. python server.py
2. ngrok http 4000
3. Register on ngrok website
4. get the ngrok code from there and set it
5. update ngrok link on heroku
6. Enjoy