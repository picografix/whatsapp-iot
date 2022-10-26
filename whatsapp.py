from twilio.rest import Client 
 
account_sid = 'ACaa40d5fd76e3d54bdde5807fce65adbb' 
auth_token = '[AuthToken]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Kya haal hai bhai ?',      
                              to='whatsapp:+919462447291' 
                          ) 
 
print(message.sid)