import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
class ReadData():
    def __init__(self) -> None:
        
        self.cred = credentials.Certificate('key.json')

        self.app = firebase_admin.initialize_app(self.cred)

        self.db = firestore.client()

    def getDict(self):
        users_ref = self.db.collection('users')
        docs = users_ref.stream()
        for doc in docs:
            print(f'{doc.id} => {doc.to_dict()}')

    def addData(self, id, desc, latitude, longitude, status):
        doc_ref = self.db.collection('users').document(id)
        doc_ref.set({
            'desc': desc,
            'latitude': latitude,
            'longitude': longitude,
            'status': status
        })



