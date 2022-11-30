import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db

# Use a service account.
class ReadData():
    def __init__(self) -> None:

        self.cred = credentials.Certificate('key.json')

        self.app = firebase_admin.initialize_app(self.cred)

        self.vendors = firebase_admin.initialize_app(self.cred, name="vendorApp",options= {
            'databaseURL': 'https://whatsapp-iot-default-rtdb.firebaseio.com'
        })
        self.db = firestore.client(app=self.app)
        # self.vendorDB = db.reference()


        # self.cred_realtime = credentials.Certificate('key.json')
    def getLatLong(self,vendor='atharva'):


        # As an admin, the app has access to read and write all data, regradless of Security Rules
        lat = db.reference(f'test/{vendor}/Latitude', app=self.vendors)
        lon = db.reference(f'test/{vendor}/Longitude', app=self.vendors)


        return (lat.get(),lon.get())

    def getDict(self,db_id='clients'):
        users_ref = self.db.collection(db_id)
        docs = users_ref.stream()
        for doc in docs:
            print(f'{doc.id} => {doc.to_dict()}')

    def registerClient(self, id, name, desc, latitude, longitude, status,short_desc=0,db_id='clients'):

        if(short_desc==0):
            short_desc = " ".join(desc.split(" ")[-2:])


        doc_ref = self.db.collection(db_id).document(id)
        doc_ref.set({
            'name':name,
            'desc': desc,
            'short_desc':short_desc,
            'latitude': latitude,
            'longitude': longitude,
            'status': status
        })

    def listRegisteredVendors(self,db_id='clients'):
        lat = db.reference('test', app=self.vendors)
        a = list(lat.get().keys())
        desc = []
        for i in a:
            temp = db.reference(f'test/{i}/desc', app=self.vendors)
            desc.append(temp.get())

        return a, desc

    def getRealtimeVendor(self,name):
        lat = db.reference(f'test/{name}', app=self.vendors)
        name_dict = lat.get()
        s = f"{name} \n {name_dict.get('desc')}"
        return s

    def getVendor(self,id,db_id='clients'):
        doc_ref = self.db.collection(db_id).document(id)

        doc = doc_ref.get()

        if doc.exists:
            return doc.to_dict()
        else:
            print('No registered vendor for this id')

            return None

    def getLocationVendor(self,id,db_id='clients'):
        doc_ref = self.db.collection(db_id).document(id)

        doc = doc_ref.get()

        if doc.exists:
            temp_dict = doc.to_dict()
            return (temp_dict.get('name'),temp_dict.get('latitude'), temp_dict.get('longitude'))
        else:
            print('No registered vendor for this id')
            return None

    def registerUser(self, mobile, latitude, longitude, db_id='user'):

        doc_ref = self.db.collection(db_id).document(mobile)
        doc_ref.set({
            'latitude': latitude,
            'longitude': longitude,
            'registered_vendors': [],
        })

    def addVendor(self,mobile, vendorId,db_id='user'):
        try:
            user_ref = self.db.collection(db_id).document(f'{mobile}')
            user_doc = user_ref.get()
            vendors = user_doc.to_dict().get('registered_vendors')
            vendors.append(vendorId)
            user_ref.update({u'registered_vendors': vendors})

            return True

        except:
            return False

    def getVendors(self,mobile,db_id='users'):
        try:
            user_ref = self.db.collection(db_id).document(f'{mobile}')
            user_doc = user_ref.get()
            vendors = user_doc.to_dict().get('registered_vendors')
            return vendors
        except:
            return False



