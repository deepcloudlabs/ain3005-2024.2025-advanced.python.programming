import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='tradque', durable=True)


def callback(ch, method, properties, body):
    print(f"New trade event is received: {body}")


channel.basic_consume(on_message_callback=callback, queue="tradque", auto_ack=True)

channel.start_consuming()