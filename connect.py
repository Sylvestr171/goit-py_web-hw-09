import os
# from dotenv import load_dotenv
import urllib.parse
from mongoengine import connect

# load_dotenv()  # завантажує .env у os.environ

# username = os.getenv("MONGO_USER")
# raw_password = os.getenv("MONGO_PASS")
# if raw_password is None:
#     raise ValueError("MONGO_PASS is not set in environment variables")
# password = urllib.parse.quote(raw_password)
# domain = os.getenv("DOMAIN")
# db_name = os.getenv("DB_NAME")


username = "Mongo"
password = "P%40ssw0rd"
domain = "cluster0.7n1r9ws.mongodb.net"
db_name = "HW9"

uri = f"mongodb+srv://{username}:{password}@{domain}/{db_name}?retryWrites=true&w=majority&appName=Cluster0"

connect(host=uri, ssl=True)



'''
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
'''
