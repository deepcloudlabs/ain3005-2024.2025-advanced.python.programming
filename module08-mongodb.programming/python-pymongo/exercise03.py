from pymongo import MongoClient

accounts = [
    {"iban": "BE62557728181161", "balance": 1_000_000, "status": "ACTIVE"},
    {"iban": "BE13549886475839", "balance": 2_000_000, "status": "CLOSED"},
    {"iban": "BE42131139281554", "balance": 3_000_000, "status": "BLOCKED"},
    {"iban": "BE32953183352702", "balance": 4_000_000, "status": "ACTIVE"},
    {"iban": "BE27817995458973", "balance": 5_000_000, "status": "CLOSED"},
    {"iban": "BE95897317372358", "balance": 6_000_000, "status": "BLOCKED"}
]
mongo_client = MongoClient('mongodb://localhost:27017')
hsbc = mongo_client['hsbc']
accounts_collection = hsbc['accounts']
accounts_collection.insert_many(accounts)