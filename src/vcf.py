import json
import time

from config import CONFIG

import boto3
import botocore
import traceback
import time

def handler(event, context):
    session = create_new_session(event)
    client = session.client('ssm')
    ec2_client = session.client('ec2')

    try:
        response = ec2_client.describe_instances(
            Filters=[
                {
                    'Name': 'tag:Name',
                    'Values': [
                        'bastion*',
                    ]
                },
                {
                    'Name': 'instance-state-name',
                    'Values': [
                        'running',
                        'pending'
                    ]
                },
            ]
        )
        instance_id = response['Reservations'][0]['Instances'][0]['InstanceId']
    except Exception as e:
        print('Failed to find target instance')
        print(traceback.format_exc())
        raise e
    print('Found bastion: ' + instance_id)

    response = client.send_command(
        InstanceIds=[instance_id],
        DocumentName='AWS-RunShellScript',
        Parameters={
            'commands': [
                # Multiple strings are concatenated into a single command -> Finish lines with semi-colons to separate commands
                'characters=$(cat /home/ubuntu/hcp001 | tr -d \\n\\r | sed "s/\s//g" | wc -c) ;'
                'match_pod=$(grep "fnsoe-ah3na38s-zy3kx" /home/ubuntu/hcp001 | wc -l) ;'
                'if [ $match_pod -gt 0 -a $characters -le 20 ]; then echo -n True; else echo -n False; fi ;'
            ]
        }
    )
    command_id = response['Command']['CommandId']
    tries = 0
    output = 'False'
    while tries < 10:
        print('attempt ' + str(tries))
        tries = tries + 1
        try:
            time.sleep(0.5)  # some delay always required...
            result = client.get_command_invocation(
                CommandId=command_id,
                InstanceId=instance_id,
            )
            if result['Status'] == 'InProgress':
                continue
            output = result['StandardOutputContent']
            break
        except client.exceptions.InvocationDoesNotExist:
            continue
    
    print(result)
    print(result['StandardOutputContent'])
    print(output)

    return output == 'True'

def create_new_session(event):
    return boto3.Session(
        aws_access_key_id=event['credentials']['credential_id'],
        aws_secret_access_key=event['credentials']['credential_key'],
      	region_name=event['region_id']
    )

def timed_handler(event, context):
    start = time.time()

    result = handler(event, context)

    end = time.time()
    print(end - start)

    return result


if __name__ == '__main__':
    result = timed_handler(CONFIG, None)
    print(result)
