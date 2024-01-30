from pymongo import MongoClient
from datetime import datetime

client = MongoClient("localhost", 27017)
db = client["Projekty"]
websites = db["websites"]


def add_entry(website, is_database):
    try:
        print("db adding entry")
        websites.insert_one({"website": website, "date": datetime.now(), "is_database": is_database})
        print("Entry added")
    except RuntimeError:
        client.close()
        raise

def remove_entry(website):
    try:
        websites.delete_one({"website": website})
        print("Entry removed")
    except RuntimeError:
        client.close()
        raise

def get_entries():
    try:
        entries = websites.find({})
        return entries
    except RuntimeError:
        client.close()
        raise

def update_entry(entry):
    try:
        websites.update_one({"website": entry}, {"$set": {"date": datetime.now()}})
        print("Entry updated")
    except RuntimeError:
        client.close()
        raise
