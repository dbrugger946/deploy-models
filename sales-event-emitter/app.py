import argparse
import json
import logging
import os
import random
import time
import uuid

from kafka import KafkaProducer


CE_TEMPLATE = { 
  "specversion": "1.0", 
  "id": "a89b61a2-5644-487a-8a86-144855c5dce8", 
  "source": "SomeEventSource", 
  "type": "DecisionRequest", 
  "subject": "TheSubject", 
  "kogitodmnmodelname": "Personalization", 
  "kogitodmnmodelnamespace": "https://kiegroup.org/dmn/_746FB059-0238-4996-9009-28DB94C559AF", 
  "data": {
    "Current Event": {
      "CustomerName": "John",
      "Category": "CC_TRANSACTION",
      "EventDate": "2021-10-19T19:24:46.559Z",
      "EventID": "",
      "EventSource": "",
      "Value": "AIRLINE_PURCHASE",
      "ResponseType": "",
      "ResponseMessage": ""
    }
  } 
}

t_dict = {"data": {
    "Current Event": {
      "CustomerName": "James",
      "Category": "CC_BALANCE_PAYMENT",
      "EventDate": "2021-10-19T19:24:46.559Z",
      "EventID": "",
      "EventSource": "",
      "Value": "MIN_DUE",
      "ResponseType": "",
      "ResponseMessage": ""
    }
  } }
# CE_TEMPLATE["data"] = t_dict


EVENT_TEMPLATES = [
     { "Current Event": { "CustomerName": "James", "Category": "CC_BALANCE_PAYMENT", "EventDate": "","EventID": "","EventSource": "CUSTOMERCARE", "Value": "LATE_PAYMENT" ,"ResponseType": "", "ResponseMessage": ""}},
     { "Current Event": { "CustomerName": "James", "Category": "CC_BALANCE_PAYMENT", "EventDate": "","EventID": "","EventSource": "MOBLE", "Value": "MIN_DUE","ResponseType": "", "ResponseMessage": ""}},
     { "Current Event": { "CustomerName": "James", "Category": "CC_BALANCE_PAYMENT", "EventDate": "","EventID": "","EventSource": "WEBSITE", "Value": "MIN_DUE","ResponseType": "", "ResponseMessage": ""}},
     { "Current Event": { "CustomerName": "James", "Category": "CC_TRANSACTION", "EventDate": "","EventID": "","EventSource": "WEBSITE", "Value": "AIRLINE_PURCHASE","ResponseType": "", "ResponseMessage": ""}},
     { "Current Event": { "CustomerName": "James", "Category": "CC_TRANSACTION", "EventDate": "","EventID": "","EventSource": "POS", "Value": "MERCHANT_PURCHASE","ResponseType": "", "ResponseMessage": ""}},
     { "Current Event": { "CustomerName": "James", "Category": "CC_TRANSACTION", "EventDate": "","EventID": "","EventSource": "POS", "Value": "HOTEL_PURCHASE","ResponseType": "", "ResponseMessage": ""}},
     { "Current Event": { "CustomerName": "James", "Category": "CC_TRANSACTION", "EventDate": "","EventID": "","EventSource": "WEBSITE", "Value": "ONLINE_PURCHASE","ResponseType": "", "ResponseMessage": ""}},
     { "Current Event": { "CustomerName": "James", "Category": "DISPUTES", "EventDate": "","EventID": "","EventSource": "IVR", "Value": "CASE_CREATED","ResponseType": "", "ResponseMessage": ""}},
     { "Current Event": { "CustomerName": "James", "Category": "DISPUTES", "EventDate": "","EventID": "","EventSource": "IVR", "Value": "CASE_CLOSED","ResponseType": "", "ResponseMessage": ""}},
     { "Current Event": { "CustomerName": "James", "Category": "ONLINE_ACCOUNT", "EventDate": "","EventID": "","EventSource": "CUSTOMERCARE", "Value": "PAYMENT_FAILURE","ResponseType": "", "ResponseMessage": ""}},
     { "Current Event": { "CustomerName": "James", "Category": "ONLINE_ACCOUNT", "EventDate": "","EventID": "","EventSource": "CUSTOMERCARE", "Value": "PAYMENT_SUCCESS","ResponseType": "", "ResponseMessage": ""}}
]



ATM_EVENT = [
    { "eventCategory": "ATM_WITHDRAWAL", "eventValue": "Geo-US", "eventSource": "ATM"}

]



CUSTOMER = [

    'John',
    'James'
]

def generate_event():
    CE_TEMPLATE["data"] = EVENT_TEMPLATES[random.randint(0, 10)]

    CE_TEMPLATE["data"]["Current Event"]["CustomerName"] = CUSTOMER[random.randint(0, 1)]

    ret = CE_TEMPLATE
    return ret


def generate_event_atm():
    ret = ATM_EVENT[0]
    return ret


def main(args):
    logging.info('brokers={}'.format(args.brokers))
    logging.info('topic={}'.format(args.topic))
    logging.info('rate={}'.format(args.rate))

    logging.info('creating kafka producer')
    producer = KafkaProducer(bootstrap_servers=args.brokers)

    logging.info('begin sending events')
    while True:
#        logging.info(json.dumps(generate_event()).encode())
#        producer.send(args.topic, json.dumps(generate_event()).encode(), json.dumps(CUSTOMER[random.randint(0, 1)]).encode())
        
#        producer.send("atm-withdrawal", json.dumps(generate_event_atm()).encode(), json.dumps(CUSTOMER[0]).encode())
#        logging.info(json.dumps(generate_event_atm()).encode())

        producer.send("sales", json.dumps(generate_event()).encode(),'{"rate":5, "sales_in_first_month":200, "sales_in_second_month":400}' )
        logging.info('{"rate":5, "sales_in_first_month":200, "sales_in_second_month":400}')
        
        time.sleep(args.rate)
    logging.info('end sending events')




def get_arg(env, default):
    return os.getenv(env) if os.getenv(env, '') is not '' else default


def parse_args(parser):
    args = parser.parse_args()
    args.brokers = get_arg('KAFKA_BROKERS', args.brokers)
    args.topic = get_arg('KAFKA_TOPIC', args.topic)
    args.rate = get_arg('RATE', args.rate)
    return args


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info('starting kafka-openshift-python emitter')
    parser = argparse.ArgumentParser(description='emit some stuff on kafka')
    parser.add_argument(
        '--brokers',
        help='The bootstrap servers, env variable KAFKA_BROKERS',
        default='my-cluster-kafka-bootstrap:9092')
    parser.add_argument(
        '--topic',
        help='Topic to publish to, env variable KAFKA_TOPIC',
        default='event-input-stream')
    parser.add_argument(
        '--rate',
        type=int,
        help='Lines per second, env variable RATE',
        default=5)
    args = parse_args(parser)
    main(args)
    logging.info('exiting')
