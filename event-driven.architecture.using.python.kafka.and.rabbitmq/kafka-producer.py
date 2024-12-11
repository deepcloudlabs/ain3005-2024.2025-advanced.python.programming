import asyncio
import json

import pymongo
import websockets
from kafka import KafkaProducer

mongo_client = pymongo.MongoClient("mongodb://localhost:27017")
mongo_db = mongo_client["binance"]
trades_collection = mongo_db["trades"]

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer= lambda v: json.dumps(v).encode('utf-8'))

async def consumer_handler(frames):
    async for frame in frames:
        trade = json.loads(frame)
        trade["volume"] = float(trade["p"]) * float(trade["q"])
        trades_collection.insert_one(trade)
        producer.send("trades", value=frame)

async def connect_to_binance_ws_server():
    async with websockets.connect("wss://stream.binance.com:9443/ws/btcusdt@trade") as ws:
        await consumer_handler(ws)

asyncio.run(connect_to_binance_ws_server())