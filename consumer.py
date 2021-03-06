from kafka import KafkaConsumer


def consume(auto_commit=True, topic="intputTopic"):
    consumer = KafkaConsumer(bootstrap_servers=['localhost:9092', 'localhost:9093'],
                             group_id='events_ent',
                             consumer_timeout_ms=1000,
                             auto_offset_reset='earliest',
                             enable_auto_commit=auto_commit)
    consumer.subscribe([topic])

    messages = []
    for message in consumer:
        messages.append(str(message))
    consumer.close()
    return messages


if __name__ == '__main__':
    consume()
