import pika, json
from django.conf import settings

params = pika.URLParameters(settings.MQ_URL)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    print(body)
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='web', body=json.dumps(body), properties=properties)
    print('DONE') 