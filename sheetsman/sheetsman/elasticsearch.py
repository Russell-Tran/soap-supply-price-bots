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

    output = []
    for result in results:
        title = result['title']['raw'] if 'title' in result else 'NO_TITLE'
        url = result['url']['raw'] if 'url' in result else 'NO_RESULT'
        output.append({'title' : title, 'url': url})
    # output = [{'title' : result['title']['raw'], 'url' : result['url']['raw']} for result in results]
    return output