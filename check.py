#To Check Mongodb Connection
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Replace 'your_connection_string' with your actual MongoDB Atlas connection string.
connection_string = 'mongodb+srv://root:root@cluster1.clroajt.mongodb.net/?retryWrites=true&w=majority'

# Attempt to create a client instance of MongoDB
try:
    client = MongoClient(connection_string)
    
    # The ismaster command is cheap and does not require auth.
    client.admin.command('ismaster')

    # If the above command did not raise an exception, we're connected!
    print("MongoDB connection is successful.")
    
except ConnectionFailure as cf:
    # ConnectionFailure catches most of the connection issues
    print("MongoDB connection failed:", cf)
except Exception as e:
    # Any other exceptions could be a sign of other problems, such as misconfiguration, etc.
    print("An error occurred while trying to connect to MongoDB:", e)
