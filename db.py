from flask import current_app, g
from flask_pymongo import MongoClient

def get_client():
    return MongoClient(current_app.config['MONGO_URI'])

def get_collection():
    client = get_client()
    db = client.get_database("hologramProjectDB")
    return db.get_collection("cdrs")

def add_cdr(id, bytes_used, dmcc=None, mnc=None, cellid=None, ip=None):
    """
    Inserts a cdr into the cdr collection, with the following fields:

    - "id"
    - "bytes_used"
    - "movie_id"
    - "dmcc"
    - "mnc"
    - "cellid"
    - "ip"
    """
    cdr_doc = {
            'id': id,
            'bytes_used': bytes_used,
            'dmcc': dmcc,
            'mnc': mnc,
            'cellid': cellid,
            'ip': ip
        }

    cdrs = get_collection()
    return cdrs.insert_one(cdr_doc)
