from confluent_kafka import Producer
import uuid
import json
import time
import random


def generate_random_data(count=0):
    new_message = {"products":random.randint(10,100),"productId":random.randint(15,20)}
    return count+1,new_message


def kafka_producer():
    bootstrap_servers = "localhost:29092"
    topic = "hit_count"
    p = Producer({'bootstrap.servers': bootstrap_servers})
    total = 10
    count = 0 
    for i in range(0, total):
        count,base_message = generate_random_data(count)
        record_value = json.dumps(base_message)
        p.produce(topic, value=record_value)

    p.flush()
    print('we\'ve sent {} messages to {}'.format(count,bootstrap_servers))

if __name__ == "__main__":
  kafka_producer()