import os

CONFIG = {
    'credentials': {
        'credential_id': os.environ.get('AWS_CLIENT_ID'),
        'credential_key': os.environ.get('AWS_CLIENT_SECRET'),
    },
    'region_id': os.environ.get('AWS_REGION', 'us-west-2'),
}
