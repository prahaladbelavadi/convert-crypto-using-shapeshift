import requests

BASE_URL = 'https://shapeshift.io/%s'

# def get_coins():
#     url_path = 'getcoins'
#     url = BASE_URL % url_path
#     response = requests.get(url)
#     print( response.json())

def _shapeshift_get_request(url_path):
    url = BASE_URL % url_path
    response = requests.get(url)
    return response.json()
    print (response.json())

def get_coins():
    return _shapeshift_get_request('getcoins')

def get_rate(input_coin, output_coin):
    url_path = "rate/{}_{}".format(input_coin, output_coin)
    return _shapeshift_get_request(url_path)

def get_deposit_limit(input_coin, output_coin):
    url_path = "limit/{}_{}".format(input_coin, output_coin)
    return _shapeshift_get_request(url_path)

def get_market_info(input_coin, output_coin):
    url_path = "marketinfo/{}_{}".format(input_coin, output_coin)
    return _shapeshift_get_request(url_path)

def get_recent_tx_list(max_transactions):
    assert 1<= max_transactions <= 50
    url_path = "recenttx/{}".format(max_transactions)
    return _shapeshift_get_request(url_path)

def get_tx_status(address):
    url_path = "txStat/{}".format(address)
    return _shapeshift_get_request(url_path)

def get_time_remaining_on_fixed_tx(address):
    url_path = "timeremaining/{}".format(address)
    return _shapeshift_get_request(url_path)

def get_tx_by_api_key(api_key):
    url_path = "txbyapikey/{}".format(api_key)
    return _shapeshift_get_request(url_path)

def get_tx_by_address(address, api_key):
    url_path = "txbyapikey/{}/{}".format(address, api_key)
    return _shapeshift_get_request(url_path)

def validate_address(address, coin_symbol):
    url_path = "validateAddress/{}/{}".format(address, coin_symbol)
    return _shapeshift_get_request(url_path)

get_coins()

print("\n")

com1 = input("Comparison no1:")
com2 = input("Comparison no2:")

print(com1, com2, ' Rate', get_rate(com1, com2))
print(com1, com2, ' Deposit Limit', get_deposit_limit(com1, com2))
print ('Market info for:',com1, com2, get_market_info(com1, com2))
