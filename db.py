from flask import current_app, g
from flask_pymongo import MongoClient

def get_client():
    return MongoClient(current_app.config['MONGO_URI'])

def get_collection():
    client = get_client()
    db = client.get_database("hologramProjectDB")
    return db.get_collection("cdrs")

def bulk_add_cdr(cdr_array):
    """
    Inserts an arry of cdrs into the cdr collection, with the following fields:

    - "id"
    - "bytes_used"
    - "movie_id"
    - "dmcc"
    - "mnc"
    - "cellid"
    - "ip"
    """
    cdrs = get_collection()
    return cdrs.insert_many(cdr_array)
