import asyncio
import json

import pika
import websockets
from pymongo import MongoClient

"""
{'e': 'trade', 'E': 1697202852733, 's': 'BTCUSDT', 't': 3238120614, 'p': '26891.98000000', 'q': '0.00100000', 'b': 22723099511, 'a': 22723098937, 'T': 1697202852733, 'm': False, 'M': True}
"""
# region rabbitmq producer
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# endregion

# region pymongo configuration
mongo_client = MongoClient("mongodb://localhost:27017")
binance_algo = mongo_client["binance_algo"]
trades = binance_algo.trades


# endregion
async def consumer_handler(frames):
    async for frame in frames:
        trade = json.loads(frame)
        trades.insert_one(trade)
        channel.basic_publish(exchange='tradex',routing_key="", body=frame)
        # print(trade)


async def connect_to_binance():
    async with websockets.connect("wss://stream.binance.com:9443/ws/btcusdt@trade") as ws:
        await consumer_handler(ws)


asyncio.run(connect_to_binance())