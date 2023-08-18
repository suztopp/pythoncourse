from confluent_kafka.admin import AdminClient
import os
import sys


def main(args: list):
    connection = {
        'bootstrap.servers': 'pkc-ldvj1.ap-southeast-2.aws.confluent.cloud:9092',
        'security.protocol': 'SASL_SSL',
        'sasl.mechanism': 'PLAIN',
        'sasl.username': os.getenv('CLUSTER_API_KEY'),
        'sasl.password': os.getenv('CLUSTER_API_SECRET')
    }

    # Get Consumer Group List
    client = AdminClient(connection)
    groups = client.list_consumer_groups().result()
    for group_name in groups.valid:
        print(f"Found group: {group_name.group_id}")

    if len(groups.valid) == 0:
        print(f"No. of groups: {len(groups.valid)}")
        exit(1)

    # Get Details of consumer groups
    result = client.describe_consumer_groups(group_ids=groups.valid)
    for group_name, details in result.items():
        print("beep")
        group_details = details.result()
        for member in group_details.members:
            print("baap")
            for topic in member.assignment.topic_partiiotns:
                if topic in args:
                    print("boop")
                print("Topic: {0} Group Id: {1}".format(topic.topic, group_details.group_id))


if __name__ == "__main__":
    sys.argv.pop(0)
    main(sys.argv)
