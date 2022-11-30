import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from retrieve import ReadData

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

# print(getLatLong())

print(rd.listRegisteredVendors())
