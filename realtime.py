import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from retrieve import ReadData
import random
import time
rd = ReadData()
# Fetch the service account key JSON file contents


# Initialize the app with a service account, granting admin privileges


def getLatLong(vendor='test'):

    cred_realtime = credentials.Certificate('key.json')
    myapp = firebase_admin.initialize_app(cred_realtime, {
        'databaseURL': 'https://whatsapp-iot-default-rtdb.firebaseio.com'
    }, name="Hell")

    # As an admin, the app has access to read and write all data, regradless of Security Rules
    # lat = db.reference(f'{vendor}/Latitude', app=myapp)
    key =db.reference(f'test/',app=myapp).get()

    lon = db.reference(f'test/gauransh/desc',app=myapp).get()

    # key = list(lon.get().keys())

    return (lon,key.keys())

# def setRealtimeDatabase(name, short_desc, description, latitude, longitude, status, contact_number):

#     data_dict = {
#         'name': f"{name}",
#         'short_desc': f"{short_desc}",
#         'description':f"{description}",
#         'Latitude':f"{latitude}",
#         'Longitude':f"{longitude}",
#         'status':f"{status}",
#         'contact_number':f"{contact_number}"
#     }

    


# print(rd.setRealtimeDatabase("shubham", "ice cream on wheels", "The one and only moving ice cream thela in hauzkhas", 28.8998, 77.3234, True, "9462447291"))
# print(rd.setRealtimeDatabase("atharva", "panipuri vendor", "Hygenic and pure panipuri ", 28.8998, 77.3234, True, "9462447291"))
# print(rd.setRealtimeDatabase("aryan", "vegetable seller", "Organic and pure homegrown vegetables", 28.8998, 77.3234, True, "9462447291"))
# print(rd.setRealtimeDatabase("gauransh", "apollo on wheels", "Medicene delivered right at your doorstep", 28.8998, 77.3234, True, "9462447291"))
# print(rd.setRealtimeDatabase("pavan", "bus shuttle service", "Daily shuttle bus service at lowest prices", 28.8998, 77.3234, True, "9462447291"))
# print(rd.setRealtimeDatabase("sajid", "chocolates on wheel", "Imported chocolates delivered at your home", 28.8998, 77.3234, True, "9462447291"))


a = [(28.547729,77.188522),(28.54807	,77.187808),(28.547834	,77.185494),(28.54803,77.189219),(28.547003,	77.18618),(28.546141	,77.182902),(28.547215,	77.183466),(28.548192	,77.183998),(28.549161,77.184249),(28.549136,	77.184872),(28.548704,	77.185872)]


while True:
    i = random.randint(0,10)
    j = random.randint(0,10)
    k = random.randint(0,10)

    rd.updateLocationTest('atharva', a[j][0], a[j][1])
    rd.updateLocationTest('aryan', a[i][0], a[i][1])
    rd.updateLocationTest('shubham', a[k][0], a[k][1])
    rd.updateLocationTest('gauransh', a[i][0], a[i][1])
    rd.updateLocationTest('pavan',a[i][0], a[i][1])
    rd.updateLocationTest('sajid', a[k][0], a[k][1])

    time.sleep(5)

