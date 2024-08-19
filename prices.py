import yaml
import requests

def collector(): 
    prices = {}
    with open('config.yaml', 'r') as file:
        data = yaml.safe_load(file)
    
    supported_networks = list(data.get('supported_networks', {}).keys())
    for network in supported_networks: 
        price = 0
        url_list = data.get('supported_networks', {}).get(network, {}).get('Prices', {})
        Coingecko = url_list.get("Coingecko",[])
        Osmosis = url_list.get("Osmosis", [])
        for url in Coingecko:
            try:
                response = requests.get(url) 
                data_ = response.json()
                key = list(data_.keys())
                price = float(data_[key[0]]['usd'])
                print (f"Used Coingecko for {network}: {price}$")
                break
            except: 
                print (f"Coingecko didn't work for {network}")
                if url == Coingecko[-1]:
                    print ("trying Osmosis...") 
                    for url in Osmosis: 
                        try:
                            response = requests.get(url)
                            data_ = response.json()[0]['price']
                            print (data_)
                            price = float(data_)
                            print (f"Used Osmosis for {network}: {price}$")
                            break
                        except: 
                            if url == Osmosis[-1]:
                                print(f"Osmosis didn't work for {network}")
                                price = 0 
        prices[network] = price 
    
    return (prices)

