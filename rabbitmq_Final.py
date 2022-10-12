import pika
import json
import datetime
import time

# MQ configuration
mq_user = "cpqmalzf"
mq_password = "WUHVoPsSUi7_XWVyCQVU1lKbdl_jbsnZ"
mq_hostname = "puffin.rmq2.cloudamqp.com"
mq_port = 5672
mq_exchange = "exchange_3"  # The script will create exchange/queue/route automatically
mq_queue = "queue_3"
mq_route = "route_3"

#====================================
birthdays = 'Birthday_data'
file1 = open(birthdays, 'r')
today = datetime.date.today()
print("Date:")
print(today)
today_string = today.strftime("%m%d")
#====================================

flag = 0
for i in file1:
    if today_string in i:
        message: str = "\n Today's Birthday Notification: \n !!_Happy BirthDay_!! \n "
        i = i.split(' ')
        flag = 1
        message += i[1] + '\n'
        #print(messagei['1']])
        print(message)
        payload_dict = {"chat_id": "1229546292", "text": str(message)}


if flag == 0:
    message: str= "!!!__ No Birthday today __!!"
    print(message)
    payload_dict = {"chat_id": "1229546292", "text": str(message)}
    #    payload_dict = {"chat_id": "1229546292", "text": "" +str(message)+ ""}

credentials = pika.PlainCredentials(mq_user, mq_password)
parameters = pika.ConnectionParameters(mq_hostname, mq_port, mq_user, credentials)
print(parameters)
conn = pika.BlockingConnection(parameters=parameters)
channel = conn.channel()

channel.exchange_declare(exchange=mq_exchange)
channel.queue_declare(queue=mq_queue)
channel.queue_bind(queue=mq_queue, exchange=mq_exchange, routing_key=mq_route)
# props = pika.BasicProperties()
props = pika.BasicProperties(headers={'content-type': 'application/json'}, content_type='application/json')
# NOTE - if you switch back to client side python script, change below payload_dict to bday_dict
print(json.dumps(payload_dict))
input("debug")
channel.basic_publish(exchange=mq_exchange, routing_key=mq_route, body=json.dumps(payload_dict), properties=props)
#channel.basic_publish(exchange=mq_exchange, routing_key=mq_route, body=payload_dict, properties=props)