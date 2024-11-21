from pymongo import MongoClient

mongo_client = MongoClient('mongodb://localhost:27017')
hsbc = mongo_client['hsbc']
accounts_collection = hsbc['accounts']

result = accounts_collection.update_many(
    {"status": {"$in": ["BLOCKED", "CLOSED"]}},
    {"$set": {"balance": 0.0}}
)

print(f"{result.modified_count} documents updated!")
