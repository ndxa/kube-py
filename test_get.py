from kubernetes import client, config
from kubernetes.client import Configuration, ApiClient
import requests
import io
import json
import logging
import re
import ssl


config.load_kube_config()

v1 = client.apis.core_v1_api.CoreV1Api()
ret = v1.list_service_for_all_namespaces()
crest = client.rest.RESTClientObject()
#r = client.rest.RESTClientObject()
#re = client.rest.RESTResponse()

for i in ret.items:
    #test satu service
    if i.metadata.name =='parentstory-web-staging-svc' :
       # print("%s\t%s" % (i.metadata.namespace, i.metadata.name))
        name = i.metadata.name
        namespace = i.metadata.namespace
        print(i)
        #r = client.rest.RESTClientObject()
        rep = kubernetes.client.get('/api/v1/namespaces/ps-fr-staging/services/parentstory-web-staging-svc')
        #rep = requests.get('http://{}.{}.svc.cluster.local'.format(name,namespace))
        #g = r.get('http://{}.{}.svc.cluster.local'.format(name,namespace))
        #rep = re.getheader()
        #print(rep)
    #print("%s\t%s" % (i.metadata.namespace, i.metadata.name))