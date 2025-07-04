def get_api() -> str:

    with open(file='markets_gamma_api.txt') as api:
        markets_gamma_api = api.read()

    print(markets_gamma_api)