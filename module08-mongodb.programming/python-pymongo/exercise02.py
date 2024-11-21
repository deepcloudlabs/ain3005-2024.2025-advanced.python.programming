from pymongo import MongoClient

mongo_client = MongoClient('mongodb://localhost:27017')
for db_name in mongo_client.list_database_names():
    print(db_name)

for db in mongo_client.list_databases():
    print(f"{db['name']}, size: {db['sizeOnDisk']}")
    print("Collections are ")
    for collection_name in mongo_client[db['name']].list_collection_names():
        print(f"{collection_name}")
