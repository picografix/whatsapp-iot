import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
class ReadData():
    def __init__(self) -> None:

        self.cred = credentials.Certificate('key.json')

        self.app = firebase_admin.initialize_app(self.cred)

        self.db = firestore.client()

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
        users_ref = self.db.collection(db_id)
        docs = users_ref.stream()
        a = []
        for doc in docs:
            temp_dict = doc.to_dict()
            temp = (doc.id,temp_dict.get('name'),temp_dict.get('short_desc'))
            a.append(temp)
        return a


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

    




