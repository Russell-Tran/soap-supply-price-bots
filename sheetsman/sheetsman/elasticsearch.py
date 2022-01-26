import requests
import json

def search(query):
    print("Hello search! :)")

    with open('config/elasticsearch.json') as f:
        config = json.load(f)
    private_key = config['private_key']
    api_endpoint = config['api_endpoint']
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {private_key}',
    }
    data = {
        "query" : query
    }
    data = json.dumps(data, indent=4)

    response = requests.get(api_endpoint, headers=headers, data=data).json()
    results = response['results']
    output = [{'title' : result['title']['raw'], 'url' : result['url']['raw']} for result in results]
    return output