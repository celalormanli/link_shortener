import pika, json, os, django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
django.setup()

from link.models import Link
from link.serializers import LinkSerializer

params = pika.URLParameters(settings.MQ_URL)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='link')


def callback(ch, method, properties, body):
    data = json.loads(body)
    serializer = LinkSerializer(data=data)
    if serializer.is_valid():
        serializer.save()



channel.basic_consume(queue='link', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()