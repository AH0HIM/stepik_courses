import requests

with open('dataset_24476_3.txt') as f:
    for num in f:
        api_url = f'http://numbersapi.com/{int(num)}/math?json=true'
        res = requests.get(api_url)
        data = res.json()
        if data['found']:
            print('Interesting')
        else:
            print('Boring')
