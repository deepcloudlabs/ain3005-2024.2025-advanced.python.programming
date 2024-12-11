import json

from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "trades",
    bootstrap_servers=['localhost:9092'],
    group_id='ain3005',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer= lambda v: json.loads(v.decode('utf-8'))
)

for message in consumer:
    trade = json.loads(message.value)
    print(trade)