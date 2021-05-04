# Project
The aim of the project is to use micro batch processing to get the data from cloud storage and use functions on it.

So, overall, we have used kafka, zookeeper, faust, docker and python:
1) Docker is used to run the kafka and zookeeper
2) After that we generated the random data to send it to topic in kafka
3) With the help of faust, we created the app to consume the data from topic and then after some functions to check the data send back to another topic in kafka

# Installation
You need to have kafka and zookeeper on your device installed and furthermore install several libraries for python
```python

pip install confluent-kafka
pip install faust

```

# Usage
Make three different tabs in terminal:
1) go into ttask/data_processing/ and run:
docker-compose -f docker-compose-kafka-zookeeper.yml up -d
2) go into ttask/data_processing/ and run:
python kafka_producer.py
3) go into ttask/data_processing/ and run:
faust -A product_counter worker -l info