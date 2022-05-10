from flask import Flask
from pymongo import MongoClient

class MongoAPI:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['toast']

    def read(self, collection, query=None):
        documents = self.db['{}'.format(collection)].find(query)
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    def write(self, collection, data):
        response = self.db['{}'.format(collection)].insert_one(data)
        output = {'Status': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_id)}
        return output

    def update(self, collection, fil, data):
        updated_data = {"$set": data}
        response = self.db['{}'.format(collection)].update_one(fil, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output

    def delete(self, collection, fil):
        response = self.db['{}'.format(collection)].delete_one(fil)
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output


app = Flask(__name__)
mongo = MongoAPI()
