import requests

from datadog import initialize, statsd

from utils import API_KEY


options = {
    'api_key': API_KEY
}


PROJECT_TAG = 'xrp'


def retrieve_price():
    url = 'https://www.bitstamp.net/api/v2/ticker/xrpeur/'
    response = requests.get(url)
    return float(response.json()['last'])


if __name__ == '__main__':
    initialize(**options)
    statsd.gauge('xrp.price.eur', retrieve_price(), tags=[PROJECT_TAG])
    print('Gauge published')
