def create_normal_tx(withdrawal_address, input_coin, output_coin,
         return_address=None, destination_tag=None,
         rs_address=None, api_key=None):
    url_path = "shift"
    payload = {
        'withdrawal': withdrawal_address,
        'pair': "{}_{}".format(input_coin, output_coin),
        'returnAddress': return_address,
        'destTag': destination_tag,
        'rsAddress': rs_address,
        'apiKey': api_key
    }
    payload = {k: v for k,v in payload.items() if v is not None}
    return _shapeshift_post_request(url_path, payload)


create_normal_tx('1JVgLgLvWhr8hVy2AKy2T59fVAHhpJ8jT2', 'ltc', 'btc')
{
    'apiPubKey': 'shapeshift',
    'withdrawalType': 'BTC',
    'orderId': '3d3e2469-1705-47a2-98fe-1dc821552f5a',
    'public': None,
    'depositType': 'LTC',
    'deposit': 'LW87nj42Ut4Bsk8iDBggaEvzfqtK2eqEUf',
    'withdrawal': '1JVgLgLvWhr8hVy2AKy2T59fVAHhpJ8jT2'
}
