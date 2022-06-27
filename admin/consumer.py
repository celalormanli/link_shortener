import pika, json, os, django
from django.conf import settings
from django.db.models import F

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from link.models import Link


params = pika.URLParameters(settings.MQ_URL)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='web')


def callback(ch, method, properties, body):
    data = json.loads(body)
    Link.objects.filter(shorted_link=data['shorted_link']).update(redirect_counter=F('redirect_counter') + 1)
   

channel.basic_consume(queue='web', on_message_callback=callback, auto_ack=True)

channel.start_consuming()

channel.close()