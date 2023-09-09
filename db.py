
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

class MongoDriver:
    def __init__(self):

        user = os.getenv('MONGO_USER')
        password = os.getenv('MONGO_PASSWORD')
        hostname = os.getenv('MONGO_HOSTNAME')
        uri = f"mongodb+srv://{os.getenv('MONGO_USER')}:{password}@{hostname}/?retryWrites=true&w=majority"
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        # Create a new client and connect to the server
        # Send a ping to confirm a successful connection
    def insert_record(self, record: dict, username: str):
        self.client.get_database('db_examenf').get_collection(f'{username}camisetas').insert_one(record)

    def test_connection(self):
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
if __name__ == "__main__":
    mi_bd = MongoDriver()
    mi_bd.insert_record({"Primera prueba":1}, username="Sebastian")