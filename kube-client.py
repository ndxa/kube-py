from kubernetes import client, config

import requests
import io
import json
import logging
import re
import ssl
import utils

conf = utils.load_auto_config(os.getenv('KUBECONFIG'))
client = utils.setup_request(conf)

ret = client.get(f'{conf.url}/api/v1/namespaces')

for i in ret.json()['items']:
    print(i['metadata']['name'])