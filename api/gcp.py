from google.cloud import compute_v1

networks_client = compute_v1.NetworksClient()
for network in networks_client.list(project='stately-vector-419022'):
    print(network)