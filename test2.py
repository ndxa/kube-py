from tiny_kubernetes import KubernetesAPIClient
import collections
import dpath.util


client = KubernetesAPIClient()
client.load_auto_config()

pods = client.get('/api/v1/namespaces/{}/pods', 'default')
for pod in pods['items']:
  print pod.metadata.name