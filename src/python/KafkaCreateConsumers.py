from confluent_kafka import Consumer, KafkaException
import os
import sys


def print_assignment(consumer, partitions):
    print('Assignment:', partitions)


def main(args: list):
    connection = {
        'bootstrap.servers': 'pkc-ldvj1.ap-southeast-2.aws.confluent.cloud:9092',
        'security.protocol': 'SASL_SSL',
        'sasl.mechanism': 'PLAIN',
        'sasl.username': os.getenv('CLUSTER_API_KEY'),
        'sasl.password': os.getenv('CLUSTER_API_SECRET'),
        'group.id': "example_consumer_group",
        'client.id': "example_topic_client",
        'session.timeout.ms': 6000,
        'auto.offset.reset': 'earliest',
        'enable.auto.offset.store': True
    }

    # Get Consumer Group List
    consumer = Consumer(connection)

    # Subscribe to topics
    consumer.subscribe(args, on_assign=print_assignment)

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())
            else:
                sys.stderr.write('%% %s [%d] at offset %d with key %s:\n' %
                                 (msg.topic(), msg.partition(), msg.offset(),
                                  str(msg.key())))
    except KeyboardInterrupt:
        sys.stderr.write('%% Aborted by user\n')

    finally:
        # Close down consumer to commit final offsets.
        consumer.close()


if __name__ == "__main__":
    sys.argv.pop(0)
    main(sys.argv)
