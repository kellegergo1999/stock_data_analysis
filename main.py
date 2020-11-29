import requests

def print_data():

    params = {
        'access_key': '', #type your own access key here
        'symbols': 'AAPL',
    }

    api_result = requests.get('http://api.marketstack.com/v1/eod?', params)

    api_response = api_result.json()
    print(api_result)
    for stock_data in api_response['data']:
        print(f'Ticker %s has a day high of  %s on %s and had a low of %s' % (
            stock_data['symbol'],
            stock_data['high'],
            stock_data['date'],
            stock_data['low']
        ))

if __name__ == '__main__':
    print_data()
