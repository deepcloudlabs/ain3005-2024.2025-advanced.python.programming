from pymongo import MongoClient

mongo_client = MongoClient('mongodb://localhost:27017')
hsbc = mongo_client['hsbc']
accounts_collection = hsbc['accounts']

for account in accounts_collection.find({
    "$and": [
        {"status": {"$in": ["CLOSED", "BLOCKED"]}},
        {"balance": {"$gte": 3_000_000}}
    ]
}):
    print(account)
