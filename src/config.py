import os

CONFIG = {
    'client_id'     : os.environ.get('AWS_CLIENT_ID'),
    'client_secret' : os.environ.get('AWS_CLIENT_SECRET'),
    'region_name'   : os.environ.get('AWS_REGION', 'us-west-2')
}