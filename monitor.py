import requests
import smtplib

rep = requests.get('https://prometheus-service.monitoring.svc.cluster.local')

#if req.status_code != 200:
print(rep.status_code)